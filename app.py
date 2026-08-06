import streamlit as st
st.set_page_config(page_title="Credit Card Fraud Detection", layout="wide")
st.title("Credit Card Fraud Detection using Machine Learning")
st.success("Deployment Successful!")
st.write("This application demonstrates a Machine Learning model for detecting fraudulent credit card transactions.")
import streamlit as st

st.set_page_config(page_title="Credit Card Fraud Detection", layout="wide")

st.title("Credit Card Fraud Detection using Machine Learning")

st.success("Deployment Successful!")

st.write("This application demonstrates a Machine Learning model for detecting fraudulent credit card transactions.")

st.subheader("Data Visualization")

st.image("transaction_amount.png", caption="Transaction Amount Distribution")
st.image("time_distribution.png", caption="Transaction Time Distribution")
st.image("fraud_vs_genuine.png", caption="Fraud vs Genuine Transactions")
st.image("confusion_matrix.png", caption="Confusion Matrix")
