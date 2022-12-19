import streamlit as st

st.header('st.button')

if st.button('Say hello'):
  st.write(':smile:')
else:
  st.write('Good bye')
