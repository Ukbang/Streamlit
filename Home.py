import streamlit as st
import pandas as pd

st.set_page_config(
                    page_title = "아이펠에서 배우는 Streamlit",
                    page_icon = "🦏",
                    layout="centered",
)

st.title("(주) 아이펠")

st.write("""
앞으로 여러가지 인공지능 모델을 탑재해 실습을 진행할 예정입니다.
""")


# 로또 번호 추첨기

import numpy as np

col1, col2, col3 = st.columns(3)

lotto_number = list(range(1,46))

winning_number = []

button = col3.button("로또 번호를 뽑아보세요.")

if button:
    winning_number.append(np.random.choice(lotto_number))

col1.write(lotto_number)
col2.write(winning_number)
