import streamlit as st
import pandas as pd

st.title("📊 Actuarial MFE Dashboard")
st.markdown("Explore the training data from the Kaggle competition")

# Load data
df = pd.read_csv("../data/train.csv")

# Show raw data
if st.checkbox("Show raw data"):
    st.write(df.head())

# Summary stats
st.subheader("📌 Summary")
st.write(df.describe())

# Select a column to visualize
col = st.selectbox("Select a feature to visualize", df.columns)

st.bar_chart(df[col].value_counts())
