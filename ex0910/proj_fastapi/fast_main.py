from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UserInput(BaseModel):
    name: str
    age: int


@app.get("/")
def read_root():
    return {"message": "FastAPI 서버가 정상 동작 중입니다."}


@app.post("/predict")
def process_data(data: UserInput):
    # 비즈니스 로직 및 AI 모델 추론 처리 위치
    is_adult = data.age >= 19

    message = f"안녕하세요 {data.name}님! " + (
        "성인입니다." if is_adult else "미성년자입니다."
    )

    return {
        "status": "success",
        "result_message": message,
        "is_adult": is_adult
    }

class ChatInput(BaseModel):
    message: str


@app.post("/chat")
def chat(data: ChatInput):

    user_message = data.message

    print("받은 채팅:", user_message)  # ← 이거 추가

    # 임시 챗봇 응답
    reply = f"입력한 내용은 '{user_message}' 입니다."

    return {
        "reply": reply
    }