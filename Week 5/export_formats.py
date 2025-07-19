import pandas as pd
from sqlalchemy import create_engine
import fastavro
import os
os.makedirs("output", exist_ok=True)


engine = create_engine('sqlite:///source.db')
df = pd.read_sql("SELECT * FROM employee", engine)

df.to_csv("output/employee.csv", index=False)
df.to_parquet("output/employee.parquet", engine='pyarrow')

records = df.to_dict(orient='records')
schema = {
    "type": "record",
    "name": "Employee",
    "fields": [
        {"name": "id", "type": "int"},            # Fix: changed from 'string' to 'int'
        {"name": "name", "type": "string"},
        {"name": "age", "type": "int"}
    ]
}

with open("output/employee.avro", "wb") as out:
    fastavro.writer(out, schema, records)
