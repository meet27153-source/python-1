import streamlit as st
st.set_page_config(page_title='Hello Streamlit',page_icon='⚔',layout='centered')
st.title("Welcomw to Streamlit")
st.header("This is header")
st.subheader("This is subheader")
st.text("st.text() is used for simple fix width text")
st.write("st.write() is more flexible and can display text,numbers,dataframes")
st.markdown("** st.markdown()** let you use markdown for **rich text**")

example= """
def add(a,b):
    return a+b
result=add(5,10)
print(result)"""
st.code(example,language='python')
