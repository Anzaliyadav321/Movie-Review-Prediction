import streamlit as st

import joblib

st.header('Movie Review Prediction')



user_input = st.text_area('Enter your  REVIEW   Here')

col1, col2, col3 = st.columns(3)
with col1:
    pass

with col2:
    button_pressed = st.button('Click to find Review')

with col3:
    pass

if button_pressed:
    model = joblib.load('Sentiment_analysis_model.pkl')
    tf_idf = joblib.load('tf-idf vectorizer.pkl')
    user_input = tf_idf.transform([user_input, ])
    sentiment = model.predict(user_input)
    st.write(f'Sentiment: {sentiment[0]}')

#sentiment = [0, 1]

if (sentiment == 1):
    st.write('Good To Watch')
elif(sentiment == 0):
    st.write('Not So GOOd')
else:
    st.write('')