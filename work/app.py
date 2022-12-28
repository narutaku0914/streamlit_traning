import streamlit as st

st.header('st.checkbox')

# checkboxがcheckedか否かを返す？
check = st.checkbox('Click here')

if check:
  st.write(f"State of the checkbox: {check}")

check2 = st.checkbox("Uncheck to remove cake", value=True)

if check2:
  st.write(f"State of the checkbox: {check2}")
  st.write(":cake:"*102)


