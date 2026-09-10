import streamlit as st
import requests

FASTAPI_URL = "http://127.0.0.1:8000"

st.title("AI 챗봇")

user_message = st.chat_input("메시지를 입력하세요")

if user_message:

    # 사용자 메시지 출력
    with st.chat_message("user"):
        st.write(user_message)

    payload = {
        "message": user_message
    }

    try:
        response = requests.post(
            f"{FASTAPI_URL}/chat",
            json=payload
        )

        if response.status_code == 200:
            result = response.json()

            with st.chat_message("assistant"):
                st.write(result["reply"])

        else:
            st.error(f"오류 발생: {response.status_code}")

    except requests.exceptions.RequestException as e:
        st.error(f"FastAPI 연결 오류: {e}")