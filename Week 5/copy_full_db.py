from sqlalchemy import create_engine, inspect
import pandas as pd

# Create source and destination engines (SQLite in this case)
source_engine = create_engine('sqlite:///source.db')
destination_engine = create_engine('sqlite:///destination.db')

# Use inspector to get all table names
inspector = inspect(source_engine)
table_names = inspector.get_table_names()

# Loop through each table and copy it to the destination
for table in table_names:
    df = pd.read_sql(f"SELECT * FROM {table}", source_engine)
    df.to_sql(table, destination_engine, if_exists="replace", index=False)

print("✅ All tables copied from source.db to destination.db")
