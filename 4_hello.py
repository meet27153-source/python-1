import streamlit as st

st.title("Number Inputs and Slider Demo")

age=st.number_input("Enter your age:",min_value=0,max_value=100,value=25)
rating=st.slider("Rate this session:",min_value=1,max_value=10,value=5)

st.write(f"Your age:{age}")
st.write(f"You rated this session:{rating}/10")
