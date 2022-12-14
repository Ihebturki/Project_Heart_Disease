# -*- coding: utf-8 -*-
"""
Created on Sun May  8 21:01:15 2022

@author: siddhardhan
"""

import pickle
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px 
from streamlit_option_menu import option_menu


"""
<style>
{{
primaryColor = "#d33682"
backgroundColor = "#002b36"
secondaryBackgroundColor = "#586e75"
textColor = "#FF9633"
font-family = "Cooper Black"
font-size:50px
}}
</style>
"""


            
  
# loading the saved model


heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))




# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Heart Disease Prediction System',
                          
                         
                           ['Heart Disease Prediction'],
                          icons=['heart'],
                          default_index=0)
    
    


# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
    
    
    df = pd.read_csv('heart_disease_data.csv')

    
def data_tail():
    st.header('Tail of Dataframe')
    st.write(df.tail())

def data_header():
    st.header('Header of Dataframe')
    st.write(df.head())
    
def displayplot():
    st.header('Plot of Data')
    
    fig, ax = plt.subplots(1,1)
    ax.scatter(x=df['age'], y=df['thalach'])
    ax.set_xlabel('Age')
    ax.set_ylabel('Maximum Heart Rate achieved')
    
    st.pyplot(fig)    
    
    #Sidebar navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select what you want to display:', ['Head', 'Tail', 'Scatter Plot'])
    
if options == 'Tail':
    data_tail()
elif options == 'Head':
    data_header()
elif options == 'Scatter Plot':
    displayplot()    
    
groupby_column = st.selectbox(
        'What would you like to analyse?',
        ('age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg','thalach','exang','oldpeak','slope','ca','thal','target'),
)

# -- GROUP DATAFRAME
output_columns = ['cp', 'fbs']
df_grouped = df.groupby(by=[groupby_column], as_index=False)[output_columns].sum()

# -- PLOT DATAFRAME
fig = px.bar(
      df_grouped,
      x=groupby_column,
      y='cp',
      color='fbs',
      color_continuous_scale=['red', 'yellow', 'green'],
      template='plotly_white',
      title=f'<b>Chest Pain types & Fasting Blood Sugar by {groupby_column}</b>'
)
st.plotly_chart(fig)

 


    
    














