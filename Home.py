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

import streamlit as st
import random

# @st.cache_resource(show_spinner="Loading...")  # 결과를 캐시하기 위해 데코레이터를 사용합니다.
# def generate_lotto_numbers():
#     return sorted(random.sample(range(1, 46), 6))

# st.title('로또 번호 생성기')

# if st.button('번호 생성'):
#     lotto_numbers = generate_lotto_numbers()
#     st.write(f'생성된 로또 번호: {lotto_numbers}')
# else:
#     st.write('번호를 생성하려면 아래 버튼을 클릭하세요.')
