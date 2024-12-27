from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np

# Define the input data schema
class LoanApplication(BaseModel):
    person_age: int
    person_income: float
    person_home_ownership: str
    person_emp_length: float
    loan_intent: str
    loan_grade: str
    loan_amnt: int
    loan_int_rate: float
    loan_percent_income: float
    cb_person_default_on_file: str
    cb_person_cred_hist_length: int

# Mapping for categorical variables
person_home_ownership_map = {"RENT": 2, "OWN": 3, "MORTGAGE": 0, "OTHER": 1}
loan_grade_map = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}
loan_intent_map = {
    "DEBT CONSOLIDATION": 0,
    "HOME IMPROVEMENT": 1,
    "VENTURE": 5,
    "PERSONAL": 4,
    "MEDICAL": 3,
    "EDUCATION":1
}
default_on_file_map = {"Yes": 1, "No": 0}


# Load the trained ML model
def load_light_model():
    try:
        with open("E:\\python\\2.PROJECTS\\loan\\artifacts\\lightgbm_model.pkl", "rb") as f:
            return pickle.load(f)
    except Exception as e:
        raise RuntimeError(f"Error loading model: {e}")

def load_cat_model():
    try:
        with open("E:\\python\\2.PROJECTS\\loan\\artifacts\\CB_classifier.pkl",'rb') as f:
            return pickle.load(f)
    except Exception as e:
        raise RuntimeError(f"Error loading model : {e}")

# Preprocess input data
def preprocess_data(data: dict):
    try:
        input_data = np.array([
            data["person_age"],
            data["person_income"],
            data["person_home_ownership"],
            data["person_emp_length"],
            data["loan_grade"],
            data["loan_intent"],
            data["loan_amnt"],
            data["loan_int_rate"],
            data["loan_percent_income"],
            data["cb_person_default_on_file"],
            data["cb_person_cred_hist_length"]
        ]).reshape(1, -1)
        return input_data
    except KeyError as e:
        raise ValueError(f"Invalid input value: {e}")


# Make prediction
def make_prediction(model, input_data):
    try:
        prediction = model.predict(input_data)
        return prediction.tolist() 
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error making prediction: {e}")
def make_proba(model,input_data):
    try:
        prediction = model.predict_proba(input_data)
        return prediction.tolist() 
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error making prediction: {e}")

# Initialize FastAPI app
app = FastAPI()
model = load_cat_model()

@app.post("/predict")
async def predict_loan_application(data: LoanApplication):
    try:
        # Preprocess the input data
        input_data = preprocess_data(data.dict())  # Convert Pydantic model to dictionary
        # Make prediction
        prediction = make_prediction(model, input_data)
        return {"classification_result": prediction}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")