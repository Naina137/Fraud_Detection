import streamlit as st

st.set_page_config(page_title="Credit Card Fraud Detection", layout="wide")

st.title("Credit Card Fraud Detection using Machine Learning")

st.success("Deployment Successful!")

st.subheader("📊 Fraud vs Genuine Transactions")
st.write("This chart compares the number of genuine and fraudulent transactions.")
st.image("images/fraud_vs_genuine.png")

st.subheader("⏱️ Transaction Time Distribution")
st.write("This graph shows how transactions are distributed over time.")
st.image("images/time_distribution.png")

st.subheader("💳 Transaction Amount Distribution")
st.write("This graph shows the distribution of transaction amounts.")
st.image("images/transaction_amount.png")

st.subheader("🎯 Confusion Matrix")
st.write("This confusion matrix evaluates the model performance.")
st.image("images/confusion_matrix.png")
