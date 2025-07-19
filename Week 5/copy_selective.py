from sqlalchemy import create_engine
import pandas as pd

# Connect to source and destination DBs
engine = create_engine('sqlite:///source.db')
new_engine = create_engine('sqlite:///destination.db')

# Select specific columns from a table
df = pd.read_sql("SELECT id, name FROM users", engine)

# Save as new table in destination DB
df.to_sql("users_backup", new_engine, if_exists="replace", index=False)

print("✅ Selective columns copied to users_backup in destination.db")
