import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="즐거운 Streamlit 실습",
    page_icon="🐣",
    layout="wide"
)

st.title("(주) 아이펠")

st.write("""
앞으로 여러가지 인공지능 모델을 탑재해 실습을 진행할 예정입니다.
""")

# st.line_chart

import streamlit as st
import pandas as pd
import numpy as np

np.random.seed(99)

a = np.arange(1,11)
b = np.arange(1,11)
c = np.arange(1,11)

np.random.shuffle(a)
np.random.shuffle(b)
np.random.shuffle(c)

chart_data = np.array([a,b,c]).T

chart_data = pd.DataFrame(chart_data, columns=["a", "b", "c"])

st.dataframe(chart_data.T)

# chart_data를 line plot으로 시각화
st.line_chart(chart_data)