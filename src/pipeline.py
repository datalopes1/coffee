import subprocess
from pathlib import Path

import dlt
import pandas as pd
from loguru import logger

DATA_DIR = Path("data/raw")
DATABASE_DIR = Path("data/database/db.duckdb")
DBT_DIR = Path("dwh")


@dlt.resource(name="sales", write_disposition="replace")
def sales():
    try:
        logger.info("Inicando a inegstão de dados.")
        for file in sorted(DATA_DIR.glob("*.xlsx")):
            logger.info("Processando o arquivo: {}", file.name)

            df = pd.read_excel(file)
            yield from df.to_dict(orient="records")
    except Exception:
        logger.exception("Erro na ingestão dos dados.")
        raise


def run_dlt():
    try:
        pipeline = dlt.pipeline(
            pipeline_name="sales",
            destination=dlt.destinations.duckdb(str(DATABASE_DIR)),
            dataset_name="raw",
        )

        pipeline.run(sales, write_disposition="replace")
        logger.success("Ingestão de dados concluída.")
    except Exception:
        raise


def run_dbt():
    try:
        subprocess.run(["dbt", "build"], cwd=DBT_DIR, check=True)
    except:
        logger.exception("Erro na transformação dos dados.")


def main():
    """
    Executa o pipeline de ingestão, carregamento e transformação de dados
    """
    try:
        run_dlt()
        run_dbt()
    except Exception:
        raise


if __name__ == "__main__":
    main()
