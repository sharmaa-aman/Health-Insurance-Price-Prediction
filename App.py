import pickle
import streamlit as st


#Loading the saved model
Loaded_Model = pickle.load(open("C:/Users/vinit/Health-Insurance-Price-Prediction/RFR_Model.pkl", 'rb'))