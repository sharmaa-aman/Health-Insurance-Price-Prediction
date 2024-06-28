import pickle
import streamlit as st


#Loading the saved model
Loaded_Model = pickle.load(open("C:/Users/vinit/Health-Insurance-Price-Prediction/RFR_Model.pkl", 'rb'))


# creating a function for Prediction
def Health_Insuranace_Price_Prediction(age, sex, bmi, children, smoker,region):
    
    prediction = Loaded_Model.predict([[age, sex, bmi, children, smoker, region]])
    print(prediction)
    return prediction