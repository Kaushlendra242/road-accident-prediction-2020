import streamlit as st
import pandas as pd
import joblib
import os

# ---------------------------------------------------
# 1. SET PAGE CONFIG (MUST BE FIRST STREAMLIT COMMAND)
# ---------------------------------------------------
st.set_page_config(
    page_title="Road Accident Incident Count Predictor",
    layout="centered"
)

# ---------------------------------------------------
# 2. Load model & load data
# ---------------------------------------------------
MODEL_PATH = "road_accident_count_model.pkl"
DATA_PATH = "Regulatory Affairs of Road Accident Data 2020 India.csv"

@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file '{MODEL_PATH}' not found.")
    return joblib.load(MODEL_PATH)

@st.cache_data
def load_data():
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Data file '{DATA_PATH}' not found.")
    df = pd.read_csv(DATA_PATH)
    df.columns = df.columns.str.strip()
    return df

model = load_model()
df = load_data()

# Prepare dropdown values
cities = sorted(df["Million Plus Cities"].dropna().unique().tolist())
cause_categories = sorted(df["Cause category"].dropna().unique().tolist())
outcomes = sorted(df["Outcome of Incident"].dropna().unique().tolist())

# ---------------------------------------------------
# 3. UI STARTS HERE
# ---------------------------------------------------
st.title("🚦 Road Accident Incident Count Predictor – India 2020")

st.markdown("""
This app uses a **CatBoost ML model** to predict the expected **incident count (`Count`)**  
based on city, cause category, subcategory, and outcome.
""")

# ---------------------------------------------------
# 4. User Form
# ---------------------------------------------------
with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        city = st.selectbox("Million Plus City", cities)
        cause_category = st.selectbox("Cause Category", cause_categories)

    with col2:
        filtered_subcats = df[df["Cause category"] == cause_category]["Cause Subcategory"].dropna().unique()
        filtered_subcats = sorted(filtered_subcats.tolist())

        cause_subcategory = st.selectbox(
            "Cause Subcategory",
            filtered_subcats if len(filtered_subcats) > 0 else df["Cause Subcategory"].dropna().unique()
        )

        outcome = st.selectbox("Outcome of Incident", outcomes)

    submitted = st.form_submit_button("Predict Incident Count")

# ---------------------------------------------------
# 5. Prediction
# ---------------------------------------------------
if submitted:
    input_df = pd.DataFrame({
        "Million Plus Cities": [city],
        "Cause category": [cause_category],
        "Cause Subcategory": [cause_subcategory],
        "Outcome of Incident": [outcome]
    })

    try:
        prediction = model.predict(input_df)[0]
        st.success(f"📊 Predicted Incident Count: **{prediction:.2f}**")
    except Exception as e:
        st.error(f"Prediction error: {e}")
