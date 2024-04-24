
import pandas as pd

def aggregate_user_behavior(df):
    """Aggregate user behavior information."""
    # Group by user and application and aggregate session information
    user_behavior_agg = df.groupby(['MSISDN/Number', 'Bearer Id']).agg({
        'Bearer Id': 'count',                             # Number of xDR sessions
        'Dur. (ms)': 'sum',                               # Session duration
        'Total DL (Bytes)': 'sum',                        # Total download data
        'Total UL (Bytes)': 'sum',                        # Total upload data
        'Social Media DL (Bytes)': 'sum',                 # Social Media download data
        'Social Media UL (Bytes)': 'sum',                 # Social Media upload data
        'Google DL (Bytes)': 'sum',                       # Google download data
        'Google UL (Bytes)': 'sum',                       # Google upload data
        'Email DL (Bytes)': 'sum',                        # Email download data
        'Email UL (Bytes)': 'sum',                        # Email upload data
        'Youtube DL (Bytes)': 'sum',                      # Youtube download data
        'Youtube UL (Bytes)': 'sum',                      # Youtube upload data
        'Netflix DL (Bytes)': 'sum',                      # Netflix download data
        'Netflix UL (Bytes)': 'sum',                      # Netflix upload data
        'Gaming DL (Bytes)': 'sum',                       # Gaming download data
        'Gaming UL (Bytes)': 'sum',                       # Gaming upload data
        'Other DL (Bytes)': 'sum',                        # Other download data
        'Other UL (Bytes)': 'sum'                         # Other upload data
    })

    # Rename columns for clarity
    user_behavior_agg.columns = ['Num_xDR_sessions', 'Session_duration', 'Total_DL', 'Total_UL',
                                 'Social_Media_DL', 'Social_Media_UL', 'Google_DL', 'Google_UL',
                                 'Email_DL', 'Email_UL', 'Youtube_DL', 'Youtube_UL',
                                 'Netflix_DL', 'Netflix_UL', 'Gaming_DL', 'Gaming_UL',
                                 'Other_DL', 'Other_UL']
    
    return user_behavior_agg
