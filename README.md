# 🔐 Phishing URL Detection | End-to-End ML Project (MongoDB + DagsHub + FastAPI+FrontEnd)

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
# Model Deployment on AWS (S3 + Docker + ECR + EC2)

This repository provides a complete workflow to deploy a trained Machine Learning (ML) model on AWS using a CI/CD pipeline.

---

## Tech Stack

- Amazon S3 – Model artifact storage  
- Docker – Containerization  
- Amazon ECR – Docker image registry  
- Amazon EC2 – Model inference hosting  
- CI/CD Pipeline – Automated build and deployment  
  - GitHub Actions 
- IAM – Access and security management  

---

## Architecture Overview

1. Train the ML model locally or in a training environment  
2. Push code changes to the Git repository  
3. CI/CD pipeline triggers automatically  
4. Upload model artifacts to Amazon S3  
5. Build Docker image with inference code  
6. Push Docker image to Amazon ECR  
7. Pull and run the Docker image on Amazon EC2  

---

## CI/CD Pipeline Flow

Code Commit  
→ CI Pipeline Trigger  
→ Upload Model Artifacts to Amazon S3  
→ Build Docker Image  
→ Push Image to Amazon ECR  
→ Deploy Container on Amazon EC2  

---

## **Deployment Flow**

**Model Training → S3 Upload → Docker Build → ECR Push → EC2 Deployment**

---

## **Key AWS Services Used**

* **S3** – Model storage
* **ECR** – Container registry
* **EC2** – Model serving environment
* **IAM** – Secure access control

---

🔗 **S3**:  
https://ap-south-2.console.aws.amazon.com/s3/buckets/networksecuritybusket?region=ap-south-2&tab=objects

🔗 **ECR**:  
https://ap-south-2.console.aws.amazon.com/ecr/repositories/private/087361682596/networksecurity/_/details?region=ap-south-2

🔗 **EC2**:  
https://ap-south-2.console.aws.amazon.com/ec2/home?region=ap-south-2#Instances:
## 📎 Hashtags


