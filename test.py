# 수식 사용하기

import streamlit as st


st.set_page_config(
    page_title="Streamlit 배우기",
    page_icon="🧡",
)

with st.sidebar:
    pass

# markdown과 latex를 이용하면 손쉽게 수식을 작성 할 수 있습니다.

st.markdown(r"피타고라스의 정리 : $a^2+b^2=c^2$")
st.latex(r"a^2+b^2=c^2")

st.markdown(r"근의 공식: $x = -b \pm \frac{\sqrt{b^2-4ac}}{2a}$")
st.latex(r"x = -b \pm \frac{\sqrt{b^2-4ac}}{2a}")


# 다음 공식을 작성해볼까요?
# 시그모이드
st.markdown(r"$sigmoid(x)=\frac{1}{1+e^{-x}}$")
st.latex(r"sigmoid(x)=\frac{1}{1+e^{-x}}")

# 코사인 유사도
st.markdown(r"$cos(\theta)=\frac{A\cdot B}{||{A}|| ||{B}||}$")
st.latex(r"cos(\theta)=\frac{A\cdot B}{||{A}|| ||{B}||}")

# MSE
st.markdown(r"$MSE = \frac{1}{N}\sum_{i=1}^N(y_i- \hat{y_i})^2$")
st.latex(r"MSE = \frac{1}{N}\sum_{i=1}^N(y_i-\hat{y_i})^2")

