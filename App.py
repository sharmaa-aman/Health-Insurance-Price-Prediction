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
    
    with st.sidebar:
        st.title('About')
        st.write('Welcome to the Health Insurance Premium Prediction App!')
        st.write(' This web application is designed to help individuals estimate their health insurance premiums with ease and accuracy. Built using Streamlit, this tool leverages data-driven insights and advanced algorithms to provide reliable predictions tailored to your unique health profile and personal details.')
        
        st.title('Why Choose Our App?')
        st.write('Planning for health insurance can be a complex and daunting task. Our app simplifies this process by providing you with a clear and accurate estimate of your potential insurance premium. This empowers you to make better financial decisions and choose the most suitable insurance plan for your needs.')
        
        st.write('Thank you for using the Health Insurance Premium Prediction App. We hope this tool helps you in your journey towards securing the best possible health insurance coverage.')
        
        
    # code for Prediction
    Price = ''
    
    # creating a button for Prediction
    if st.button('Check Your Premium'):
        Price = Health_Insuranace_Price_Prediction(Age, Sex, BMI, Children, Smoker, Region)
    
    st.success('Your predicted health insurance premium is: {}'. format(Price))    
        
        
if __name__ == '__main__':
    main()