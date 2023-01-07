import streamlit as st

st.title('st.form')

st.header('1. Example of using `with` notation')
st.subheader('Coffee machine')

# with内
with st.form('my_form'):
    st.subheader('**Order your coffee**')

    # 選択した項目を変数に格納
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')


    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('☝️ Place your order!')


# object
st.header('2. Example of object notation')

form = st.form('my_form_2')
coffee_bean_val = form.selectbox('Coffee bean', ['Arabica', 'Robusta'])
coffee_roast_val = form.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
brewing_val = form.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
serving_type_val = form.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
milk_val = form.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
owncup_val = form.checkbox('Bring own cup')
form.form_submit_button('Submit')

st.markdown(f'''
  ☕ You have ordered:
  - Coffee bean: `{coffee_bean_val}`
  - Coffee roast: `{coffee_roast_val}`
  - Brewing: `{brewing_val}`
  - Serving type: `{serving_type_val}`
  - Milk: `{milk_val}`
  - Bring own cup: `{owncup_val}`
  ''')
