import streamlit as st

st.header('st.checkbox')

st.write('What would you like to order?')

# checkboxがcheckedか否かを返す？
icecream = st.checkbox('Ice cream')
coffee = st.checkbox('coffee')
cola = st.checkbox('cola')

if icecream:
  st.write("Great! Here's some more 🍦")

if coffee:
  st.write("Okey, here's some coffee ☕️")

if cola:
  st.write("Here we go 🥤")


