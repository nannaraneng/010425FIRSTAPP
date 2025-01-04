import streamlit as st

# 제목 추가
st.title('나의 첫 Streamlit 프로젝트')

# 간단한 텍스트 출력
st.write('Hello, Streamlit! 👋')

# 사용자 입력받기
user_name = st.text_input('이름을 입력하세요', '홍길동')
st.write(f'{user_name}님, 환영합니다! 😊')

# 버튼 클릭 이벤트
if st.button('클릭하세요!'):
    st.write(f'{user_name}님이 버튼을 클릭했습니다! 🚀')

# 슬라이더 추가
favorite_number = st.slider('좋아하는 숫자를 선택하세요', 0, 100, 50)
st.write(f'선택한 숫자는 {favorite_number}입니다!')
