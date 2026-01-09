import streamlit as st
import pandas as pd

st.title("Displaying the data in streamlit")

data={'Students':['A','B','C','D'],'Marks':[85,92,76,88],'Passed':[True,True,True,True]}
df=pd.DataFrame(data)

st.subheader('st.dataframe() (interactive)')
st.dataframe(df)

st.subheader('st.table() (static)')
st.table(df)

st.subheader('st.json() (structured JSON)')
st.json(data)
