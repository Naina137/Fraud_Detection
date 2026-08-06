st.subheader("📊 Fraud vs Genuine Transactions")
st.write("This chart compares the number of genuine and fraudulent transactions in the dataset.")
st.image("images/fraud_vs_genuine.png", use_container_width=True)

st.subheader("⏱️ Transaction Time Distribution")
st.write("This visualization shows how transactions are distributed over time, helping identify unusual activity patterns.")
st.image("images/time_distribution.png", use_container_width=True)

st.subheader("💳 Transaction Amount Distribution")
st.write("This graph illustrates the distribution of transaction amounts, highlighting the presence of both small and high-value transactions.")
st.image("images/transaction_amount.png", use_container_width=True)

st.subheader("🎯 Confusion Matrix")
st.write("The confusion matrix evaluates the model's performance by comparing actual and predicted transaction classes.")
st.image("images/confusion_matrix.png", use_container_width=True)
