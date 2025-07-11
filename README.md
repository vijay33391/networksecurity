# 🔐 Phishing URL Detection | End-to-End ML Project (MongoDB + DagsHub + FastAPI)

This project demonstrates a complete Machine Learning workflow for phishing website detection using URL-based features. It includes data ingestion from MongoDB, validation, transformation, model training, experiment tracking via DagsHub (with MLflow), and a fully functional FastAPI web interface.

---

## ✅ Project Highlights

- ⬇️ **Data Ingestion** from **MongoDB**
- ✔️ **Data Validation**: Checks for feature existence, numeric validation, and **data drift**
- 🔄 **Data Transformation**: 
  - Handles missing values  
  - Splits target/independent features early to prevent **data leakage**
- 🧠 **Model Training**:
  - Trains multiple models
  - Picks the best one based on **F1-score**
  - Tracked using **MLflow + DagsHub**
- ⚙️ **Pipelines**:
  - Fully automated training and prediction pipelines
- 🌐 **FastAPI Integration**:
  - Real-time and bulk prediction through UI and REST endpoints

---

## 📊 Model Evaluation Metrics

During training and evaluation, the following classification metrics are tracked using MLflow:

- **Precision**
- **Recall**
- **F1-Score** (used to select the best model)
- **Accuracy**
- **Confusion Matrix**

---

## 📈 MLflow + DagsHub Tracking

All experiments, metrics, and model artifacts are tracked using **MLflow**, integrated with **DagsHub**.

🔗 **DagsHub Project Dashboard**:  
[https://dagshub.com/vijay33391/networksecurity](https://dagshub.com/vijay33391/networksecurity)

---

## 📎 Hashtags

