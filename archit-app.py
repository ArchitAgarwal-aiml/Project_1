import  streamlit as st
import pandas as pd
import numpy as np
import time
import pickle


st.title("Benovymed AI Calculator")
st.subheader("Product Category : Heart Disease | Developed by Archit")
st.text("Pls enter the Following Info to know the result:")


#st.image("https://drive.google.com/file/d/1Tqmz-AxxpTxsl-IVwFwX10GHjC_4dMcA/view?usp=sharing", caption='Image')   

model = pickle.load(open('./LogisticRegression.pkl','rb'))
model_1= pickle.load(open('./LogisticRegression_second.pkl','rb'))
#<font color=‘red’>Proceed Further</font>, unsafe_allow_html=True)
#st.write(str(model))
st.markdown(
    '''
<font color=‘red’>Proceed Further</font>
    ''',
    unsafe_allow_html=True
)

age = st.text_input(label="Age")

sex = st.selectbox('Gender',["0","1"])

cp = st.text_input(label="Chest Pain")

trestbps = st.text_input(label="Resting Blood Pressure")

chol = st.text_input(label="Serum Cholestoral in mg/dl")

fbs = st.selectbox("is fasting blood Sugar > 120 mg/dl",["0","1"])



restecg  = st.selectbox(
    'Resting Electrocardiographic Results :',
     ["0","1","2"])

thalach = st.text_input(label="Maximum Heart Rate Achieved")

exang =st.selectbox(
    'exercise induced angina :',
     ["0","1"])

oldpeak  = st.text_input(label="ST depression induced by exercise relative to rest")

slope = st.selectbox(
    'The slope of the peak exercise ST segment :',
     ["0","1","2"])

ca  = st.selectbox("number of major vessels (0-3) colored by flourosopy",["0","1","2","3"])

#: 3 = normal; 6 = fixed defect; 7 = reversable defect
thal = st.selectbox("Thal",["1","2","3","6","7"])

pred = model.predict([[int(age),int(sex),float(cp),int(trestbps),int(chol),int(fbs),int(restecg),int(thalach),int(exang),float(oldpeak),int(slope),int(ca),int(thal) ]])
pred_1 = model_1.predict([[int(age),int(sex),float(cp),int(trestbps),int(chol),int(fbs),int(restecg),int(thalach),int(exang),float(oldpeak),int(slope),int(ca),int(thal) ]])


if st.button("Check The Patient"):
    with st.spinner("Prediction the Result..."):
        time.sleep(1)

    if pred == 0 :
        st.header("Patient has a heart problem")
    else:
        st.header("Patient is healthy")   



st.text("Proceed to advance Diagnostic in case of detected ill Heart")
#st.text("It will remotely Diagnostic about type of your Heart Disease")
if st.button("Check Further"):
    with st.spinner("Evaluating the Second stage of diagnostic..."):
        time.sleep(1)
    if pred_1 == 0 and pred == 0:
        st.header("Class 1")
    elif pred_1 == 1 and pred == 0:
        st.header("Class 2")
    elif pred_1 == 2 and pred == 0:
        st.header("Class 3")
    elif pred_1 == 3 and pred == 0:
        st.header("Class 4")
    elif pred_1 == 0 and pred == 1:
        st.header("You have a healthy Heart. No need to check further")
    elif pred_1 == 1 and pred == 1:
        st.header("You have a healthy Heart. No need to check further")
    elif pred_1 == 2 and pred == 1:
        st.header("You have a healthy Heart. No need to check further")
    else :
        st.header("YYou have a healthy Heart. No need to check further")

hide_st_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)    
