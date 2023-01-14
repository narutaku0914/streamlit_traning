import streamlit as st
import pandas as pd
import requests

st.title('🏥 Coronavirus COVID19 API app')

st.sidebar.header('Input')
country_url = 'https://api.covid19api.com/countries'
country_json_data = requests.get(country_url).json()
countries = [json['Country'] for json in country_json_data]
countries.sort()
selected_country = st.sidebar.selectbox('Select a country',countries)

# selected_type = st.sidebar.selectbox('Select an activity type', ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])
colona_url = f'https://api.covid19api.com/dayone/country/{selected_country}'
colona_json_data = requests.get(colona_url).json()

c1, c2 = st.columns(2)
with c1:
  with st.expander('About this app'):
    st.write('Coronavirus COVID19 API(https://documenter.getpostman.com/view/10808728/SzS8rjbc#intro)の Day OneAPIで取得したデータをそのままテーブルで表示。れからアップデートできれば。')
with c2:
  with st.expander('JSON data'):
    st.write(colona_json_data)

st.header(f'APIから取得した{selected_country}のコロナ感染者テーブル')
# df = pd.read_json(suggested_activity, orient='records')
df = pd.json_normalize(colona_json_data)
st.write(df)
