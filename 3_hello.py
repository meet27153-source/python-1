import streamlit as st
st.title("Text input demo")

name=st.text_input("Enter your name")
comments=st.text_area("Any comments or feedbacks")

st.write("Live Output")

if name:
    st.write(f"Hello,**{name}**🎭")
if comments:
    st.write("Your comments")
    st.write(comments)
