import streamlit as st
import pickle 
pickle_in=open('SalaryPrediction.pkl','rb')
m=pickle.load(pickle_in)

years=st.number_input('Years of Experience')
if st.button('PREDICT'):
  salary=m.predict([[years]])
  st.success(f'SALARY PREDICTED IS {salary}')
