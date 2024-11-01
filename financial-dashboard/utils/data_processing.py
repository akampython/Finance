import pandas as pd

def load_data(file_path):
    """Load data from an Excel file."""
    return pd.read_excel(file_path)

def calculate_summaries(data):
    """Calculate monthly and quarterly summaries for reports."""
    data['Month'] = data['Date'].dt.month
    data['Quarter'] = data['Date'].dt.quarter
    
    monthly_summary = data.groupby(['Month', 'Type']).sum()['Amount'].unstack().fillna(0)
    quarterly_summary = data.groupby(['Quarter', 'Type']).sum()['Amount'].unstack().fillna(0)
    
    return monthly_summary, quarterly_summary
