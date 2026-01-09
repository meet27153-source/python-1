import streamlit as st
from datetime import date,time
import numpy as np
import pandas as pd

st.title("📔Student Marks and Feedback Form")

st.header("1.Student Information")

col1,col2=st.columns([2,2])
with col1:
    enrollment=st.text_input("Enrollment no.")
    name=st.text_input("Student name:")
with col2:
    semester=st.selectbox("Semester",[1,2,3,4,5,6,7,8])
    division=st.text_input("Division")
exam_date=st.date_input("Select exam date:",value=date.today())

st.header("2.Marks entry")

PYTHON=st.number_input("Python-1:",min_value=0,max_value=100,value=0)
FSD=st.number_input("FSD-1:",min_value=0,max_value=100,value=0)
DE=st.number_input("DE:",min_value=0,max_value=100,value=0)

st.header("3.Feedback")

rating=st.slider("How well did you understand the subject?:",min_value=1,max_value=10,value=0)

rate=st.radio("Class participation",['Low','Medium','High'])
