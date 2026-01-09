import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Matplotlib + Streamlit Demo")

x=np.arange(1,11)
y=np.random.randint(50,100,size=10)

#Line chart

st.subheader("Line chart")
plt.figure(figsize=(4,2))
plt.plot(x,y,marker='o')
plt.xlabel('Student index')
plt.ylabel('Marks')
plt.title('Marks of 10 students')
st.pyplot(plt)
plt.clf()

#Bar chart

st.subheader("Bar chart")
plt.figure(figsize=(4,2))
plt.bar(x,y)
plt.xlabel('Student index')
plt.ylabel('Marks')
plt.title('Marks of 10 students')
st.pyplot(plt)
plt.clf()
