# Import necessary libraries
import pandas as pd
from sqlalchemy import create_engine
import numpy as np

database_name = 'telecom'
table_name= 'xdr_data'

connection_params = { "host": "localhost", "user": "postgres", "password": "00000000",
                    "port": "5432", "database": database_name}

engine = create_engine(f"postgresql+psycopg2://{connection_params['user']}:{connection_params['password']}@{connection_params['host']}:{connection_params['port']}/{connection_params['database']}")

# str or SQLAlchemy Selectable (select or text object)
sql_query = 'SELECT * FROM xdr_data '

df = pd.read_sql(sql_query, con= engine)

def replace_outliers_with_mean(data):
    for col in data.select_dtypes(include=np.number).columns:
        Q1 = data[col].quantile(0.25)
        Q3 = data[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        data[col] = np.where((data[col] < lower_bound) | (data[col] > upper_bound), data[col].mean(), data[col])
    return data

def replace_missing(df):
    """Replace missing values with the mean of each numeric column."""
    numeric_columns = df.select_dtypes(include=['number']).columns
    df_numeric = df[numeric_columns]
    df_filled = df_numeric.fillna(df_numeric.mean())
    df[numeric_columns] = df_filled
    return df

# Replace missing values with the mean
df = replace_missing(df)

# Replace outliers with the mean
df = replace_outliers_with_mean(df)

# Define connection parameters
database_name = 'processed_telecom'
table_name = 'xdr_data'

connection_params = {
    "host": "localhost",
    "user": "postgres",
    "password": "00000000",
    "port": "5432",  
    "database": database_name
}

# Create SQLAlchemy engine
engine = create_engine(f"postgresql+psycopg2://{connection_params['user']}:{connection_params['password']}@{connection_params['host']}:{connection_params['port']}/{connection_params['database']}")

# Insert DataFrame into the database
df.to_sql(table_name, engine, if_exists='replace', index=False)

