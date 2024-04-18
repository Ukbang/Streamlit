# 로또 번호 추첨기
import streamlit as st
import numpy as np

# 빈 lotto라는 session_state를 생성
def generate_state():
    if "lotto" not in st.session_state:
        st.session_state["lotto"] = []

# 번호 생성
def generate_lotto_numbers():
    return np.random.randint(1,46)

# session_state 생성
generate_state()

# 사이드바에 버튼을 통한 번호 생성 및 초기화 기능 추가
with st.sidebar:
    button = st.button("번호 생성")
    reset = st.button("초기화")

# 버튼 클릭 시 작동
if button:
    
    # 번호 생성
    number = generate_lotto_numbers()

    # 로또번호를 6개 이상 뽑았을 시 버튼이 작동하지 않도록 설정
    if len(st.session_state["lotto"]) >= 6:
        pass
    # 중복된 번호가 뽑혔을 시 중복 알림
    elif number in st.session_state["lotto"]:
        st.write("중복된 번호입니다.")
    # 뽑은 번호를 업데이트
    else:
        st.session_state["lotto"].append(number)
        st.session_state["lotto"].sort()

# 초기화 버튼을 통한 로또 번호 초기화
if reset:
    st.session_state["lotto"] = []

# 현재 뽑은 로또 번호 출력
st.write(st.session_state["lotto"])