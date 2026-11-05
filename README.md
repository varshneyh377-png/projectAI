# 🏦 Loan Approval Prediction System

A Machine Learning-based Loan Approval Prediction System that predicts whether a loan application is likely to be approved or rejected based on applicant details.

The project uses Logistic Regression, K-Nearest Neighbors (KNN), and Support Vector Machine (SVM) to compare model performance and predict loan approval outcomes. A Streamlit web application is used to provide an interactive user interface.

## 📌 Project Overview

Loan approval is an important process in the banking and finance sector. This project aims to simplify the process by using machine learning techniques to predict loan approval status based on selected applicant information.

The system analyzes applicant details such as marital status, income, loan amount, education, and credit history to generate a prediction.

## 🎯 Objectives

- Predict loan approval status using machine learning.
- Compare multiple classification algorithms.
- Evaluate model performance using accuracy, precision, recall, and F1-score.
- Develop an interactive web application using Streamlit.
- Understand the role of applicant information in loan prediction.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Jupyter Notebook / Google Colab

## 🤖 Machine Learning Models

The following models were implemented:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)

### Model Performance

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| Logistic Regression | 85.5% | 84.3% | 97.7% | 90.5% |
| KNN | 82.3% | 83.7% | 93.2% | 88.2% |
| SVM | 85.5% | 84.3% | 97.7% | 90.5% |

SVM was retained as the final model for the Streamlit application.

## 📊 Features Used

The model uses the following input features:

- Married
- Applicant Income
- Loan Amount
- Education
- Credit History

## 🖥️ Application
<img width="1882" height="893" alt="Screenshot 2026-11-05 100007" src="https://github.com/user-attachments/assets/24bf4406-59e5-4dbd-a68a-0573b7ea3764" />

The Streamlit application allows users to:


- Enter applicant details.
- Submit loan application information.
- Receive a predicted loan approval or rejection result.

## 📂 Project Structure

```text
Loan-Approval-Prediction/
│
├── app.py
├── loan_prediction.ipynb
├── model.pkl
├── scaler.pkl
├── dataset.csv
├── requirements.txt
├── README.md
│
└── screenshots/
    ├── home.png
    ├── prediction.png
    ├── eda.png
    └── model_comparison.png
```

*Note: Update the filenames according to your actual project files.*

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Loan-Approval-Prediction.git
cd Loan-Approval-Prediction
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📈 Results
<img width="1808" height="814" alt="Screenshot 2026-11-05 100045" src="https://github.com/user-attachments/assets/044bde9a-454c-44a1-af14-84a7a2dea0f0" />


Logistic Regression and SVM achieved the highest accuracy of 85.5%, while KNN achieved 82.3%.

The results demonstrate the application of machine learning classification algorithms to loan approval prediction.


## ⚠️ Disclaimer

This project is developed for educational purposes only. Predictions are based on a dataset and do not represent actual financial decisions or guarantee loan approval.

## 👩‍💻 Author

Your Name

## 📄 License

This project is intended for educational and academic purposes.
