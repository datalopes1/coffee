from pathlib import Path

import dlt
import pandas as pd

DATA_DIR = Path("data/raw")
DATABASE_DIR = Path("data/database/db.duckdb")


@dlt.resource(name="sales")
def sales():
    for file in DATA_DIR.glob("*.xlsx"):
        df = pd.read_excel(file)

        yield from df.to_dict(orient="records")


pipeline = dlt.pipeline(
    pipeline_name="sales",
    destination=dlt.destinations.duckdb(str(DATABASE_DIR)),
    dataset_name="dw",
)

load_data = pipeline.run(sales)

print(load_data)
