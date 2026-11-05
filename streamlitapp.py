
import streamlit as st
import requests

# Configuration
st.set_page_config(
    page_title="Loan Prediction System",
    page_icon="🏦",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000/predict/"

# Title
st.title("🏦 Loan Prediction System")
st.subheader("Machine Learning Based Loan Eligibility Prediction")

st.write(
    "Enter your details below to predict your loan approval status."
)

st.divider()

# Input section
st.header("Applicant Details")

col1, col2 = st.columns(2)

with col1:
    married = st.selectbox(
        "Married",
        ["Yes", "No"]
    )

    income = st.number_input(
        "Applicant Income",
        min_value=0,
        value=5000
    )

    education = st.selectbox(
        "Education",
        ["Graduate", "Not Graduate"]
    )

with col2:
    loan_amount = st.number_input(
        "Loan Amount",
        min_value=0,
        value=150
    )

    credit_history = st.selectbox(
        "Credit History",
        [1, 0],
        format_func=lambda x: "Good" if x == 1 else "Poor"
    )

st.divider()

# Prediction button
if st.button("Predict Loan Status"):

    input_data = {
        "x1": 1 if married == "Yes" else 0,
        "x2": income,
        "x3": loan_amount,
        "x4": 0 if education == "Graduate" else 1,
        "x5": credit_history
    }

    try:
        response = requests.post(
            API_URL,
            json=input_data,
            timeout=15
        )

        if response.status_code == 200:

            prediction = response.json()["prediction"]

            st.header("Prediction Result")

            if prediction == 1:
                st.success("✅ Loan Approved!")

            elif prediction == 0:
                st.error("❌ Loan Not Approved!")

            else:
                st.warning(f"Prediction: {prediction}")

        else:
            st.error("API Error: " + response.text)

    except requests.exceptions.ConnectionError:
        st.error("FastAPI server is not running!")

    except Exception as e:
        st.error(f"Error: {e}")

# Footer
st.divider()
st.caption("Developed using Python, Streamlit, FastAPI and Machine Learning")
