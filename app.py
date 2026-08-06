import streamlit as st
import os

st.set_page_config(page_title="Credit Card Fraud Detection", layout="wide")

st.title("💳 Credit Card Fraud Detection using Machine Learning")
st.success("Deployment Successful!")

st.write("""
This project uses Machine Learning to identify fraudulent credit card
transactions and distinguish them from genuine transactions.
""")

st.header(" Project Overview")

st.markdown("""
- **Dataset:** Credit Card Fraud Detection Dataset
- **Model:** Machine Learning Classifier
- **Objective:** Detect fraudulent transactions with high accuracy.
- **Application:** Banking and online payment fraud detection.
""")

def show_image(title, description, filename):
    st.subheader(title)
    st.write(description)

    paths = [
        f"images/{filename}",
        f"models/images/{filename}",
        filename
    ]

    found = False
    for path in paths:
        if os.path.exists(path):
            st.image(path, use_container_width=True)
            found = True
            break

    if not found:
        st.warning(f"Image not found: {filename}")

show_image(
    "Fraud vs Genuine Transactions",
    "Comparison of genuine and fraudulent transactions.",
    "fraud_vs_genuine.png"
)

show_image(
    " Time Distribution",
    "Distribution of transactions over time.",
    "time_distribution.png"
)

show_image(
    " Transaction Amount Distribution",
    "Distribution of transaction amounts.",
    "transaction_amount.png"
)

show_image(
    "Confusion Matrix",
    "Performance of the trained machine learning model.",
    "confusion_matrix.png"
)

st.success("✅ Credit Card Fraud Detection Project Completed Successfully!")