import streamlit as st

st.set_page_config(page_title="Credit Card Fraud Detection", layout="wide")

st.title("💳 Credit Card Fraud Detection using Machine Learning")
st.success("Deployment Successful!")

st.write("""
This project uses Machine Learning techniques to identify fraudulent
credit card transactions and distinguish them from genuine ones.
""")

st.subheader("Project Overview")
st.write("""
- Dataset: Credit Card Transactions
- Algorithm: Machine Learning Classifier
- Objective: Detect fraudulent transactions with high accuracy.
""")

st.subheader("Visualizations")
st.info("Fraud vs Genuine Transactions")
st.info("Time Distribution")
st.info("Transaction Amount Distribution")
st.info("Confusion Matrix")