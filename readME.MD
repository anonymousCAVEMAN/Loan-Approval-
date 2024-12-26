# 🏦 Loan Approval Machine Learning Project

Welcome to the **Loan Approval ML Project**! 🚀 This repository contains a comprehensive pipeline for predicting loan approvals using **CatBoostClassifier** with **Optuna** for hyperparameter tuning. The project also features **Streamlit** and **FastAPI** for user interaction and deployment.

---

## 🧰 Project Structure
```
📂 project-root/
├── 📁 data/              # Dataset directory
├── 📁 models/            # Trained models
├── 📁 notebooks/         # Jupyter Notebooks for experiments
├── 📁 src/               # Source code for ML pipeline
│   ├── dbfeeder.py       # Data ingestion & preprocessing
│   ├── train.py          # Model training with CatBoost & Optuna
│   ├── inference.py      # Inference and prediction
│   └── api.py            # FastAPI integration
├── 📁 reports/           # Model performance reports
└── README.md             # You're here! 
```

---

## 🔍 Key Features
- **Loan Approval Prediction** – Predict loan approval chances with high accuracy.
- **CatBoost Classifier** – Efficient gradient boosting implementation.
- **Optuna Tuning** – Automatic hyperparameter optimization.
- **Model Evaluation** – Accuracy, Precision, Recall, and F1-score metrics.
- **Streamlit & FastAPI** – Interactive dashboards and REST API.

---

## 📦 Requirements
```bash
pip install -r requirements.txt
```

---

## 🚀 Quickstart
1. **Clone the Repository**
   ```bash
   git clone https://github.com/username/loan-approval-ml.git
   cd loan-approval-ml
   ```
2. **Prepare Data**
   ```bash
   python src/dbfeeder.py
   ```
3. **Train the Model (CatBoost + Optuna)**
   ```bash
   python src/train.py
   ```
4. **Run Inference**
   ```bash
   python src/inference.py
   ```
5. **Launch Streamlit App**
   ```bash
   streamlit run app.py
   ```
6. **Start FastAPI Server**
   ```bash
   uvicorn src.api:app --reload
   ```

---

## 📊 Model Performance
| Metric         | Value          |
|----------------|----------------|
| Accuracy       | 95%            |
| Precision      | 0.93           |
| Recall         | 0.91           |
| F1-Score       | 0.92           |

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📧 Contact
For questions or collaboration, reach out at [your-email@example.com](mailto:your-email@example.com).

