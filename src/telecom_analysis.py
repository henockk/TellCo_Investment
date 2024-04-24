
import pandas as pd


def identify_top_handsets(df):
    """Identify the top 10 handsets used by the customers."""
    top_handsets = df['Handset Type'].value_counts().head(10)
    return top_handsets

def identify_top_manufacturers(df):
    """Identify the top 3 handset manufacturers."""
    top_manufacturers = df['Handset Manufacturer'].value_counts().head(3)
    return top_manufacturers

def identify_top_handsets_per_manufacturer(df):
    """Identify the top 5 handsets per top 3 handset manufacturer."""
    top_manufacturers = identify_top_manufacturers(df).index.tolist()
    top_handsets_per_manufacturer = {}
    for manufacturer in top_manufacturers:
        top_handsets = df[df['Handset Manufacturer'] == manufacturer]['Handset Type'].value_counts().head(5)
        top_handsets_per_manufacturer[manufacturer] = top_handsets
    return top_handsets_per_manufacturer

def generate_recommendations():
    """Generate recommendations to marketing teams."""
   
    recommendations = """
    Recommendation 1: 
    Recommendation 2:
    """
    return recommendations


