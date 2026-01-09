import streamlit as st

st.title("Media Displayt Demo")
st.subheader("Image example")
st.image('free.png',use_container_width=True)

st.subheader('Audio sample')
st.audio('sampleaudio.mp3')
         
st.subheader('Video sample')
st.video('samplevideo.mp4')
