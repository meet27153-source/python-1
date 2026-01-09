import streamlit as st
import pandas as pd

if st.button("Click here to generate sample data"):
    df=pd.DataFrame({"Enrollment no.":[1,2,3,4],'Marks':[78,85,92,69]})
    st.write("Generate data")
    st.dataframe(df)
    csv=df.to_csv(index=False).encode('utf-8')
    st.download_button(label='Download as csv',data=csv,file_name='sample.csv',mime='text/csv')
