import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


st.header('Line chart with Altair')

source = pd.DataFrame({
  'x': np.arange(20),
  'a': np.random.randn(20),
})

chart = alt.Chart(source).mark_line().encode(
  x='x',
  y='a'
)

st.altair_chart(chart, use_container_width=True)
