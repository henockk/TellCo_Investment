import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from scipy.stats import describe


def describe_variables(df):
    """Describe relevant variables and data types."""
    variables = df.columns.tolist()
    data_types = df.dtypes
    return dict(zip(variables, data_types))

def analyze_basic_metrics(df):
    """Analyze basic metrics in the dataset."""
    return df.describe()

def non_graphical_univariate_analysis(df):
    """Conduct non-graphical univariate analysis."""
    return df.apply(describe, axis=1)

def graphical_univariate_analysis(df):
    """Conduct graphical univariate analysis."""
    quantitative_vars = df.select_dtypes(include=['float64']).columns
    for var in quantitative_vars:
        plt.figure(figsize=(8, 6))
        sns.histplot(df[var], bins=20, kde=True)
        plt.title(f'Histogram of {var}')
        plt.xlabel(var)
        plt.ylabel('Frequency')
        plt.show()

def bivariate_analysis(df):
    """Conduct bivariate analysis."""
    correlation_matrix = df.corr()
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Correlation Matrix')
    plt.show()

def variable_transformations(df):
    """Perform variable transformations."""
    df['Total Duration Decile'] = pd.qcut(df['Dur. (ms)'], q=10, labels=False)
    total_data_per_decile = df.groupby('Total Duration Decile')['Total UL (Bytes)', 'Total DL (Bytes)'].sum()
    return total_data_per_decile

def correlation_analysis(df):
    """Conduct correlation analysis."""
    relevant_vars = ['Social Media DL (Bytes)', 'Google DL (Bytes)', 'Email DL (Bytes)', 'Youtube DL (Bytes)',
                     'Netflix DL (Bytes)', 'Gaming DL (Bytes)', 'Other DL (Bytes)',
                     'Social Media UL (Bytes)', 'Google UL (Bytes)', 'Email UL (Bytes)', 'Youtube UL (Bytes)',
                     'Netflix UL (Bytes)', 'Gaming UL (Bytes)', 'Other UL (Bytes)']
    correlation_matrix_relevant = df[relevant_vars].corr()
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix_relevant, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Correlation Matrix for Relevant Variables')
    plt.show()

def dimensionality_reduction(df):
    """Perform dimensionality reduction."""
    X = df.dropna().select_dtypes(include=['float64'])
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(X_scaled)
    return pca_result, pca.explained_variance_ratio_, pca.components_


