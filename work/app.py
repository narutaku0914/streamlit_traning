import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

st.subheader('md記法')

st.write('Hello, *world!* :sunglasses:')
st.subheader('')

st.subheader('数値出力')
st.write(1234)
st.subheader('')

st.subheader('表')
df = pd.DataFrame({
  'first column': [1,2,3,4],
  'second column': [10,20,30,40]
})

st.write('コメント',df, 'コメント')
st.subheader('')

st.subheader('バブル？')
df2 =pd.DataFrame(
  np.random.randn(200, 3),
  columns=['a', 'b', 'c'])

c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
