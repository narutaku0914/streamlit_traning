import streamlit as st
import pandas as pd

st.title('st.file_uploader')

st.subheader('Input CSV')
upload_file = st.file_uploader("choose a file")

if upload_file is not None:
  df = pd.read_csv(upload_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('☝️ Upload a CSV file')
