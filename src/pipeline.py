import subprocess
from pathlib import Path

import dlt
import pandas as pd
from loguru import logger

DATA_DIR = Path("data/raw")
DATABASE_DIR = Path("data/database/db.duckdb")
DBT_DIR = Path("dwh")

@dlt.resource(name="sales")
def sales():
    try:
        logger.info("Iniciada a ingestão de dados.")
        for file in DATA_DIR.glob("*.xlsx"):
            logger.info("Processando o arquivo {}.", file.name)
            df = pd.read_excel(file)

            logger.info("Arquivo carregado: {}. {} registros.", file.name, len(df))

            yield from df.to_dict(orient="records")
    except Exception:
        logger.exception("Erro na ingestão dos dados.")
        raise

    
def run_dbt():
    subprocess.run(
            ["dbt", "build"],
            cwd=DBT_DIR,
            check=True
        )

def main():
    """
    Executa o pipeline de ingestão, carregamento e transformação de dados
    """    
    pipeline = dlt.pipeline(
        pipeline_name="sales",
        destination=dlt.destinations.duckdb(str(DATABASE_DIR)),
        dataset_name="raw",
    )

    try:
        pipeline.run(sales)
        logger.success("Ingestão bem sucedida.")
        run_dbt()

    except Exception:
        logger.exception("Erro na ingestão de dados.")
        raise


if __name__ == "__main__":
    main()
