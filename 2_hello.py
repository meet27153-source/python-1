import streamlit as st
st.set_page_config(page_title='Faculty Profile',page_icon='⚔',layout='centered')
st.title("Faculty Profile demo")
st.markdown("This example shows how to use **Sidebars,Columns and Expanders**")

st.sidebar.header("Profile Settings")
name=st.sidebar.text_input("Faculty name","Tejas thakker")
department=st.sidebar.selectbox("Department",['CE','IT','CSE','AIML'])
experience=st.sidebar.slider("Years of Experience",0,40,10)
st.markdown("---")
st.sidebar.write("You can put filter,toggles etc. in sidebar")

col1,col2=st.columns([1,2])
with col1:
    st.subheader("Basic info")
    st.write(f"**Name:** {name}")
    st.write(f"**Department:** {department}")
    st.write(f"**experience:** {experience}years")
with col2:
    st.subheader("About")
    st.markdown("""
    Use this area to show detailed information about the faculty members""")
    
with st.expander("Show courses handled"):
    st.write("Python-1")
    st.write("Python-2")
    st.write("Digital Electronics")
with st.expander("Show Publication"):
    st.write("1. Research paper A(2024)")
    st.write("2. Research paper B(2025)")
