import streamlit as st
import pandas as pd
import plotly.express as px

# Sample data
df = pd.DataFrame({
    "Country": ["USA", "Canada", "Mexico"],
    "Cases": [1000, 500, 700]
})

# Create figure
fig = px.bar(df, x="Country", y="Cases", title="Sample Dashboard")

# Streamlit app
st.title("COVID-19 Dashboard")
st.plotly_chart(fig, use_container_width=True)
