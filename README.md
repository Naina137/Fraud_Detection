# Credit Card Fraud Detection using Machine Learning

## Project Overview

Credit card fraud is one of the most critical challenges in the financial industry, leading to significant financial losses each year. This project focuses on developing a Machine Learning model capable of identifying fraudulent credit card transactions by analyzing transaction patterns and customer behavior.

The dataset used in this project is highly imbalanced, making fraud detection a challenging binary classification problem. To address this, the project evaluates model performance using multiple metrics such as Accuracy, Precision, Recall, F1-Score, Classification Report, and Confusion Matrix rather than relying solely on accuracy.

This project demonstrates an end-to-end Machine Learning workflow, including data preprocessing, exploratory data analysis (EDA), feature scaling, model training, model comparison, evaluation, and model serialization for future deployment.

---

## Project Objectives

- Analyze credit card transaction data.
- Perform data preprocessing and cleaning.
- Handle the highly imbalanced dataset.
- Explore transaction patterns using data visualization.
- Train multiple Machine Learning models.
- Compare Logistic Regression and Random Forest Classifier.
- Evaluate model performance using multiple metrics.
- Save the best-performing model for future predictions.
- Build a foundation for real-time fraud detection systems.

---

## Technologies Used

### Programming Language

- Python

### Data Analysis

- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn

### Machine Learning

- Scikit-learn
  - Train-Test Split
  - StandardScaler
  - Logistic Regression
  - Random Forest Classifier
  - Accuracy Score
  - Precision Score
  - Recall Score
  - F1-Score
  - Classification Report
  - Confusion Matrix

### Development Environment

- Jupyter Notebook
- Visual Studio Code

### Model Serialization

- Pickle

### Version Control

- Git
- GitHub

---

## Project Structure

```text
Fraud_Detection/
│
├── data/
│   └── creditcard.csv
│
├── notebook/
│   └── Fraud_Detection.ipynb
│
├── models/
│   └── fraud_model.pkl
│
├── images/
│   ├── fraud_vs_genuine.png
│   ├── time_distribution.png
│   ├── transaction_amount.png
│   └── confusion_matrix.png
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Project Workflow

1. Load the credit card transaction dataset.
2. Explore and preprocess the dataset.
3. Handle missing values and duplicate records.
4. Analyze the class distribution.
5. Perform Exploratory Data Analysis (EDA).
6. Split the dataset into training and testing sets.
7. Apply feature scaling using StandardScaler.
8. Train Logistic Regression and Random Forest Classifier.
9. Compare both models using multiple evaluation metrics.
10. Save the best-performing model using Pickle.

---

## Exploratory Data Analysis

### Fraud vs Genuine Transactions

![Fraud vs Genuine Transactions](images/fraud_vs_genuine.png)

This visualization highlights the class imbalance between fraudulent and genuine transactions.

---

### Time Distribution of Transactions

![Time Distribution](images/time_distribution.png)

This graph illustrates how transactions are distributed over time.

---

### Transaction Amount by Class

![Transaction Amount by Class](images/transaction_amount.png)

This visualization compares transaction amounts for genuine and fraudulent transactions.

---

## Model Evaluation

Both Logistic Regression and Random Forest models were evaluated using multiple performance metrics.

- Accuracy
- Precision
- Recall
- F1-Score
- Classification Report
- Confusion Matrix

Since fraud detection datasets are highly imbalanced, Accuracy alone is not sufficient. Precision, Recall, and F1-Score provide a more reliable measure of model performance.

### Confusion Matrix

![Confusion Matrix](images/confusion_matrix.png)

The Confusion Matrix illustrates the number of correctly and incorrectly classified transactions, helping evaluate the effectiveness of the trained model.

---

## Future Improvements

- Compare additional Machine Learning algorithms such as XGBoost and LightGBM.
- Perform Hyperparameter Tuning.
- Handle class imbalance using SMOTE.
- Improve feature engineering techniques.
- Deploy the model using Flask or FastAPI.
- Build a real-time credit card fraud detection web application.
- Integrate REST APIs for live transaction prediction.

---

## About the Author

**Naina Kumari**

Computer Science & Engineering (Data Science) student with a strong interest in Data Science, Machine Learning, Artificial Intelligence, and Data Analytics.

I enjoy building practical, real-world projects that solve meaningful problems while continuously improving my technical skills. My goal is to develop impactful AI-driven solutions and contribute to innovative technology.

---

## Connect with the Author

**GitHub**

https://github.com/Naina137

**LinkedIn**

https://www.linkedin.com/in/naina-kumari-06373132b

**Email**

nainakumari32627@gmail.com

If you found this project useful or have any suggestions, feel free to connect. Contributions, feedback, and collaboration are always welcome.

⭐ If you like this project, consider giving it a Star.
