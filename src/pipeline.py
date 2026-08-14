from pathlib import Path
from loguru import logger
import subprocess

import dlt
import pandas as pd

DATA_DIR = Path("data/raw")
DATABASE_DIR = Path("data/database/db.duckdb")
DBT_DIR = Path("dwh")

@dlt.resource(name="sales")
def sales():
    try:
        for file in sorted(DATA_DIR.glob("*.xlsx")):
            logger.info("Processando o arquivo: {}", file.name)

            df = pd.read_excel(file)
            yield from df.to_dict(orient="records")
    except Exception:
        logger.exception("Erro na ingestão dos dados.")
        raise

def run_dlt():
    try:
        logger.info("Inicando a ingestão dos dados.")
        pipeline = dlt.pipeline(
            pipeline_name="sales",
            destination=dlt.destinations.duckdb(str(DATABASE_DIR)),
            dataset_name="raw",
        )

        pipeline.run(sales, write_disposition='replace')
        logger.success("Ingestão de dados concluída.")
    except Exception:
        raise

def run_dbt():
    try:
        subprocess.run(
            ["dbt", "build"],
            cwd=DBT_DIR,
            check=True
        )
    except Exception:
        logger.exception("Erro na transformação dos dados.")
        raise

def main():
    run_dlt()
    run_dbt()

if __name__=="__main__":
    main()