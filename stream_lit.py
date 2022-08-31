import joblib
import streamlit as st

st.write("# Spam Detection Engine")
message_text = st.text_input("Enter a review for Evaluation : ")

model = joblib.load('VerzeoMajorProject')

st.write('## Result : ')

predictions = model.predict([message_text])[0]

if message_text != '':
    if predictions == 0:
        st.write('Negative review')
    else:
        st.write('Positive review')