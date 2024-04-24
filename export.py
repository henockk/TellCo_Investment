import pandas as pd
from sqlalchemy import create_engine

# Database connection parameters
connection_params = {
    "host": "localhost",
    "user": "postgres",
    "password": "00000000",
    "port": "5432",
    "database": "telecom"
}

# Create a SQLAlchemy engine
engine = create_engine(f"postgresql+psycopg2://{connection_params['user']}:{connection_params['password']}@{connection_params['host']}:{connection_params['port']}/{connection_params['database']}")

# SQL query to fetch data from the database
sql_query = "SELECT * FROM xdr_data"

# Read data from the database into a pandas DataFrame
df = pd.read_sql(sql_query, con=engine)

# Path to save the CSV file
csv_file_path = r"C:\Users\User\Desktop\10_Acadamy\Week 1\Datasets\telecom.csv"

# Save the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)

print(f"Data exported to {csv_file_path}")