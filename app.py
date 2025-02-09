import streamlit as st
import pickle
import pandas as pd

st.title('Selling Price Prediction for CAR brands')
st.write('This web app predicts the **Selling Price** for cars')

# to read the model from the pickle file
model=pickle.load(open('Assignment2CAR.pkl','rb'))

# get the input from the user
year=st.number_input('year')
km_driven=st.number_input('km_driven')
transmission=st.number_input('transmission_label_encoded')
seller_type=st.number_input('sellertype_label_encoded')
fuel=st.number_input('fuel_label_encoded')
owner=st.number_input('owner_label_encoded')

# convert the user input to a dataframe
user_data=pd.DataFrame({'year':year,
    'km_driven':km_driven,
    'transmission_label_encoded':transmission,
    'sellertype_label_encoded':seller_type,
    'fuel_label_encoded':fuel,
    'owner_label_encoded': owner,}, index=[0])

# predict the house price
prediction=model.predict(user_data)

if st.button('Predict'):
    st.write(f'The predicted car selling price is {prediction[0]* 100000}')