import streamlit as st
from datetime import date,time
st.title("Date,Time and File Uploader")

exam_date=st.date_input("Select exam date:",value=date.today())
start_time=st.time_input("Exam start time:",value=time(9,0))

upload_file=st.file_uploader("Upload CSV file",type=['CSV'])
st.write(f"Selected Exam date: {exam_date}")
st.write(f"Exam start time: {start_time}")

if upload_file is not None:
    st.success("File uploaded successfully")
    st.write("File name:",upload_file.name)
    st.write("File type:",upload_file.type)
