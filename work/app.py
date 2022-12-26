import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
  'What is your favorite color?',
  # setであることに注意
  ('Blue', 'Red', 'Green'),
  # label_visibility="hidden",
  # disabled=True
)

st.write('Your favorite color is ', option)
