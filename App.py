import pickle
import streamlit as st


#Loading the saved model
Loaded_Model = pickle.load(open("C:/Users/vinit/Health-Insurance-Price-Prediction/RFR_Model.pkl", 'rb'))


# creating a function for Prediction
def Health_Insuranace_Price_Prediction(age, sex, bmi, children, smoker,region):
    
    prediction = Loaded_Model.predict([[age, sex, bmi, children, smoker, region]])
    print(prediction)
    return prediction    
  
def main():
    
    # giving a title
    st.title('Health Insurance Premium Prediction App')
    
    # getting the input data from the user
    Age = st.number_input('Enter your age', min_value=0, max_value=100, step=1, value=None)
    Sex = st.selectbox('Select your Gender: For Male = 0, For Female = 1', [0, 1], index=None, placeholder="Select")
    BMI = st.number_input('Enter your bmi value', min_value=0, max_value=100, step=1, value=None)
    Children = st.selectbox('Select your number of children', [0, 1, 2, 3, 4], index=None, placeholder="Select")
    Smoker = st.selectbox('Select your smoking status:  For No = 0  For Yes = 1', [0, 1], index=None, placeholder="Select")
    Region = st.selectbox('Select your region:  For Northwest = 0,  For Northeast = 1,  For Southeast = 2,  For Southwest = 3', [0, 1, 2, 3], index=None, placeholder="Select")