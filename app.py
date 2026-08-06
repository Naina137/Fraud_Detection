import streamlit as st
import os

st.set_page_config(page_title="Credit Card Fraud Detection", layout="wide")

st.title("💳 Credit Card Fraud Detection using Machine Learning")
st.success("Deployment Successful!")

def show_image(filename, caption):
    if os.path.exists(f"images/{filename}"):
        st.image(f"images/{filename}", use_container_width=True)
    elif os.path.exists(f"models/images/{filename}"):
        st.image(f"models/images/{filename}", use_container_width=True)
    elif os.path.exists(filename):
        st.image(filename, use_container_width=True)
    else:
        st.error(f"❌ {filename} not found.")

st.subheader("📊 Fraud vs Genuine Transactions")
st.write("This chart compares the number of genuine and fraudulent transactions.")
show_image("fraud_vs_genuine.png", "Fraud vs Genuine Transactions")

st.subheader("⏱ Time Distribution")
st.write("This graph shows how transactions are distributed over time.")
show_image("time_distribution.png", "Time Distribution")

st.subheader("💰 Transaction Amount Distribution")
st.write("This graph shows the distribution of transaction amounts.")
show_image("transaction_amount.png", "Transaction Amount Distribution")

st.subheader("📈 Confusion Matrix")
st.write("This confusion matrix evaluates the model's prediction performance.")
show_image("confusion_matrix.png", "Confusion Matrix")
