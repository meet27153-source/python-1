import streamlit as st
import time

st.title("Status Element Demo")

st.success("This is Success Message")
st.warning("This is Warning Message")
st.error("This is Error Message")
st.info("This is Useful information")

st.write("---")
st.subheader('Progress and Spinner Example')

if st.button("Start Long Task"):
    progress=st.progress(0)
    with st.spinner("Progressing..."):
        for i in range(100):
            time.sleep(0.03)
            progress.progress(i+1)
    st.success("Task completed")
