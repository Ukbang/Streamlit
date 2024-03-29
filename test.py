import streamlit as st

# 마크다운 문법 지원 X
st.text("""text : *반갑습니다.* Your Text, Please 사용이 매우,, 간편하지요?""")

# 마크다운 문법 지원 O
st.write("""write : *반갑습니다.* Your Text, Please 사용이 매우,, 간편하지요?""")

# 마크다운 문법 지원 O
st.markdown("""markdown : *반갑습니다.* Your Text, Please 사용이 매우,, 간편하지요?""")

x = 30
y = 20

st.text(f"""text : 물론 변수도 사용이 가능합니다. x는 {x}, y는 {y}, x+y는 {x+y}이죠""")

# 에러 발생 -> text는 인수를 1개만 받습니다.
# st.text("x+y : ", x+y)

st.write(f"""write : 물론 변수도 사용이 가능합니다. x는 {x}, y는 {y}, x+y는 {x+y}이죠""")

# write는 변수를 직접 사용할 수 있습니다.
st.write("x+y : ", x+y)

st.markdown(f"""markdown : 물론 변수도 사용이 가능합니다. x는 {x}, y는 {y}, x+y는 {x+y}이죠""")

# 마크다운은 변수를 직접 사용하지 못합니다.
st.markdown("x+y", x+y)

