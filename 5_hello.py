import streamlit as st

st.title("Selection widget Demo")

course=st.selectbox("Selection Couurse:",['Python','FSD','DE','PS'])
preffere_days=st.multiselect("Prefferd days for extra lectures",['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'])
delievery_mode=st.radio("Preffered deleievery Mode",['Offline','Online','Hybrid'])
subscribe=st.checkbox("Subscribe to course updates")
st.write("---")
st.write(f"**Course:** {course}")
st.write(f"**Preffered days:** {','.join(preffere_days) if preffere_days else None}")
st.write(f"**Deleievery Mode** {delievery_mode}")
st.write(f"**Subscribe:** {'Yes' if subscribe else 'No'}")
