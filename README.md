# 🚦 Road Accident Analysis & Incident Count Prediction – India 2020



### 🔍 Machine Learning + Streamlit Web App  
Predicting road accident incident counts across India's million-plus cities using **CatBoost**, **EDA**, and **interactive deployment**.

---

## 📊 Project Overview

Road accidents pose a serious challenge across Indian metropolitan regions.  
This project analyzes the **2020 accident dataset for million-plus cities** and builds a **Machine Learning model** to predict the number of incidents (`Count`) based on:

- City  
- Cause Category  
- Cause Subcategory  
- Outcome of Incident  

The final model is deployed as a **Streamlit web application** for real-time predictions.

---

## 🎯 Objectives

- Perform **Exploratory Data Analysis (EDA)**  
- Identify high-risk **cities, causes, and outcomes**  
- Train multiple ML models & compare metrics  
- Select **CatBoost Regressor** as the final model  
- Build and deploy a **Streamlit app**  
- Provide actionable insights for policy makers  

---

## 📁 Dataset Description

The dataset contains accident records for India's million-plus cities for the year 2020.

### **Columns:**

- **Million Plus Cities** — name of city  
- **Cause category** — broad category of accident cause  
- **Cause Subcategory** — detailed cause description  
- **Outcome of Incident** — injuries, fatalities, total accidents  
- **Count** — number of incidents  

### **Data Cleaning Steps:**

- Trimmed column names  
- Filled missing `Count` values  
- Removed duplicate rows  
- Standardized categories  

---

## 📈 Exploratory Data Analysis (Highlights)

- Certain cities have significantly higher accident counts (hotspots).  
- Accident causes like **Road Features**, **Impacting Vehicle/Object**, and **Traffic Control** dominate.  
- Outcomes such as **Total Injured** and **Total number of Accidents** are most frequent.  
- Heatmap analysis shows which cause categories relate to more severe outcomes.

---

## 🤖 Machine Learning Approach

### **Problem Type:**  
Regression (predicting `Count`)

### **Models Evaluated:**

- Linear Regression  
- Random Forest Regressor  
- Gradient Boosting Regressor  
- **CatBoost Regressor (Final Model)**  

### **Evaluation Metrics:**
- MAE – Mean Absolute Error  
- RMSE – Root Mean Square Error  
- R² – Explained Variance  

---

## 🏆 Model Performance

| Model               | MAE     | RMSE     | R²     |
|---------------------|---------|----------|--------|
| Linear Regression   | 114.68  | 211.92   | 0.352  |
| Gradient Boosting   | 91.46   | 202.99   | 0.405  |
| Random Forest       | 70.27   | 186.14   | 0.500  |
| **CatBoost Regressor** | **60.08** | **158.34** | **0.638** |

👉 **CatBoost achieved the best accuracy and is used in deployment.**

---

## 🚀 Streamlit Deployment

### **Live App (After Deployment):**  
➡️ *[https://road-accident-prediction-2020-datascientist-kp-singh.streamlit.app/]*

### **To run locally:**

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py

```
**📦 Project Structure**

```
project-folder/
│── streamlit_app.py
│── road_accident_count_model.pkl
│── Regulatory Affairs of Road Accident Data 2020 India.csv
│── requirements.txt
│── README.md
│── Road_Accident_Project_Report.docx
└── *.ipynb (optional)
```
-----

**🌐 Deploying to Streamlit Cloud**

1. Upload all project files to GitHub

2. Go to https://share.streamlit.io

3. Click New App → select GitHub repo

4. Choose main file: streamlit_app.py

5. Click Deploy

Streamlit automatically installs dependencies and hosts the app online.

------

**🧠 Business Impact**

- Helps identify dangerous cities & causes

- Supports traffic authorities with data-driven planning

- Aids in resource allocation and accident prevention

- Useful for policymakers, urban planners, and safety auditors

------

**🔮 Future Enhancements**

- Add multi-year accident data

- Include weather, road length, population, and traffic density

- Create severity classification model

- Build Power BI dashboard

- Add what-if scenario simulators

-------

**🙌 Author** 

*Kaushlendra Pratap Singh*
Data Analyst, Machine Learning & Data sceinist Practitioner
Passionate about building data-driven solutions for meaningful impact.

-----

***⭐ If you found this project helpful
Please ⭐ star the repo & share it on LinkedIn!***
