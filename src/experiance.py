import pandas as pd
from sqlalchemy import create_engine
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def read_data(database_name='processed_telecom', table_name='xdr_data', 
              connection_params={"host": "localhost", "user": "postgres", "password": "00000000",
                                  "port": "5432", "database": database_name}):
    """Read data from the database."""
    engine = create_engine(f"postgresql+psycopg2://{connection_params['user']}:{connection_params['password']}@{connection_params['host']}:{connection_params['port']}/{connection_params['database']}")
    sql_query = f'SELECT * FROM {table_name}'
    df = pd.read_sql(sql_query, con=engine)
    return df

def aggregate_per_customer(df):
    """Aggregate information per customer."""
    aggregated_df = df.groupby('MSISDN/Number').agg({
        'TCP DL Retrans. Vol (Bytes)': 'mean',
        'Avg RTT DL (ms)': 'mean',
        'Handset Type': lambda x: x.mode()[0],
        'Avg Bearer TP DL (kbps)': 'mean'
    }).reset_index()
    return aggregated_df

def top_tcp_values(df, n=10):
    """Compute top TCP DL Retransmission Volume values."""
    top_values = df['TCP DL Retrans. Vol (Bytes)'].nlargest(n)
    return top_values

def bottom_tcp_values(df, n=10):
    """Compute bottom TCP DL Retransmission Volume values."""
    bottom_values = df['TCP DL Retrans. Vol (Bytes)'].nsmallest(n)
    return bottom_values

def most_frequent_tcp_values(df, n=10):
    """Compute most frequent TCP DL Retransmission Volume values."""
    most_frequent_values = df['TCP DL Retrans. Vol (Bytes)'].value_counts().head(n)
    return most_frequent_values

def top_rtt_values(df, n=10):
    """Compute top Avg RTT DL (ms) values."""
    top_values = df['Avg RTT DL (ms)'].nlargest(n)
    return top_values

def bottom_rtt_values(df, n=10):
    """Compute bottom Avg RTT DL (ms) values."""
    bottom_values = df['Avg RTT DL (ms)'].nsmallest(n)
    return bottom_values

def most_frequent_rtt_values(df, n=10):
    """Compute most frequent Avg RTT DL (ms) values."""
    most_frequent_values = df['Avg RTT DL (ms)'].value_counts().head(n)
    return most_frequent_values

def top_throughput_values(df, n=10):
    """Compute top Avg Bearer TP DL (kbps) values."""
    top_values = df['Avg Bearer TP DL (kbps)'].nlargest(n)
    return top_values

def bottom_throughput_values(df, n=10):
    """Compute bottom Avg Bearer TP DL (kbps) values."""
    bottom_values = df['Avg Bearer TP DL (kbps)'].nsmallest(n)
    return bottom_values

def most_frequent_throughput_values(df, n=10):
    """Compute most frequent Avg Bearer TP DL (kbps) values."""
    most_frequent_values = df['Avg Bearer TP DL (kbps)'].value_counts().head(n)
    return most_frequent_values

def throughput_distribution(df):
    """Compute distribution of average throughput per handset type."""
    distribution = df.groupby('Handset Type')['Avg Bearer TP DL (kbps)'].mean()
    return distribution

def tcp_retransmission_per_handset(df):
    """Compute average TCP retransmission per handset type."""
    tcp_retransmission = df.groupby('Handset Type')['TCP DL Retrans. Vol (Bytes)'].mean()
    return tcp_retransmission

def perform_kmeans_clustering(df, features, n_clusters=3):
    """Perform K-means clustering."""
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['cluster'] = kmeans.fit_predict(df[features])
    return df

def preprocess_data(df, features):
    """Preprocess the data."""
    df[features] = df[features].fillna(df[features].mean())
    scaler = StandardScaler()
    X = scaler.fit_transform(df[features])
    return X

if __name__ == "__main__":
    df = read_data()
    aggregated_df = aggregate_per_customer(df)
    print(aggregated_df.head())
    top_tcp = top_tcp_values(df)
    print("Top TCP values:")
    print(top_tcp)
    top_rtt = top_rtt_values(df)
    print("Top RTT values:")
    print(top_rtt)
    top_throughput = top_throughput_values(df)
    print("Top Throughput values:")
    print(top_throughput)
    throughput_dist = throughput
