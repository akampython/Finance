import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_processing import load_data, calculate_summaries

# Load data
data = load_data("input.xlsx")

# Sidebar Filters
st.sidebar.title("Filters")
date_range = st.sidebar.date_input("Select Date Range", [])
selected_month = st.sidebar.selectbox("Select Month", options=range(1, 13))

# Dashboard Title
st.title("Financial Dashboard")

# Reports Section
st.header("Reports")
monthly_summary, quarterly_summary = calculate_summaries(data)
st.subheader("Monthly Summary")
st.dataframe(monthly_summary)
st.subheader("Quarterly Summary")
st.dataframe(quarterly_summary)

# Transaction History Section
st.header("Transaction History")
if date_range:
    start_date, end_date = date_range
    filtered_data = data[(data['Date'] >= pd.to_datetime(start_date)) & (data['Date'] <= pd.to_datetime(end_date))]
else:
    filtered_data = data
st.write(filtered_data)

# Charts and Graphs Section
st.header("Charts and Graphs")

# Bar Chart for Expense Categories
expense_data = data[data['Type'] == 'Expense']
expense_chart = px.bar(expense_data, x='Category', y='Amount', title="Spending by Category")
st.plotly_chart(expense_chart)

# Line Chart for Income and Expenses Over Time
time_series_chart = px.line(data, x='Date', y='Amount', color='Type', title="Income/Expense Over Time")
st.plotly_chart(time_series_chart)
