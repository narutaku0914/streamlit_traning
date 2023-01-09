import streamlit as st
import numpy as np
import pandas as pd
from time import time

st.title('st.cache')

# Using cache
a0 = time()
st.subheader('Using st.cache')

# @st.cache(suppress_st_warning=True)
@st.cache
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  st.write('a')
  return df

  '''
    suppress_st_warning キーワードを @st.cache デコレータに追加したことにお気づきでしょうか。これは、上のキャッシュ関数はStreamlitのコマンドそのものを使っているので（この場合はst.write）、Streamlitがそれを見ると、キャッシュミスがあったときだけコマンドが実行されるという警告が表示されるからです。多くの場合、この警告が表示されるのは、あなたのコードにバグがあることが原因です。しかし、私たちの場合はst.writeコマンドを使ってキャッシュがなくなったときのデモをしているので、Streamlitが警告している動作はまさに私たちが欲しいものなのです。そのため、suppress_st_warning=Trueを渡すことで、その警告を消しています。
  '''

st.write(load_data_a())
a1 = time()
st.info(a1-a0)


# Not using cache
b0 = time()
st.subheader('Not using st.cache')

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_b())
b1 = time()
st.info(b1-b0)
