from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# GET 요청
@app.get("/")
def read_root():
    return {"message": "안녕"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.get("/hello")
def read_hello():
    return {"message": "hello"}


@app.get("/users")
def read_users():
    return {"users": ["Alice", "Bob", "Charlie"]}

# http://127.0.0.1:8000/
# http://127.0.0.1:8000/items/1
# http://127.0.0.1:8000/hello
# http://127.0.0.1:8000/users

# http://127.0.0.1:8000/docs

class User(BaseModel):
    name: str
    age: int


@app.post("/users")
def create_user(user: User):
    return {
        "message": "사용자 생성 완료",
        "name": user.name,
        "age": user.age
    }

# FastAPI 앱 생성
app = FastAPI()


# POST 요청으로 받을 데이터 형식 정의
# BaseModel을 상속하면 FastAPI가 데이터 타입을 자동으로 검사해줌
class User(BaseModel):
    name: str       # 이름은 문자열
    age: int        # 나이는 정수
    email: str      # 이메일은 문자열


# POST 요청
# 주소: http://127.0.0.1:8000/users
@app.post("/users")
def create_user(user: User):

    # user에는 클라이언트가 보낸 JSON 데이터가 들어옴
    # 예:
    # {
    #   "name": "Johnny",
    #   "age": 29,
    #   "email": "johnny@test.com"
    # }

    # 받은 데이터를 다시 응답으로 반환
    return {
        "message": "사용자 생성 완료",
        "name": user.name,
        "age": user.age,
        "email": user.email
    }
# http://127.0.0.1:8000/docs


class Item(BaseModel):
    name: str
    price: int
    desc: str


@app.post("/items/")
async def create_item(item: Item):
    return {
        "msg": "아이템이 성공적으로 생성되었습니다.",
        "received_data": item
    }
# http://127.0.0.1:8000/docs


# PUT 요청
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {
        "msg": "아이템이 성공적으로 수정되었습니다.",
        "item_id": item_id,
        "updated_data": item
    }

# item_id = 1 → 1번 상품 수정
# item_id = 2 → 2번 상품 수정
# item_id = 100 → 100번 상품 수정
# http://127.0.0.1:8000/docs


# DELETE 요청
# 특정 사용자를 삭제할 때 사용
# 예: user_id가 1이면 1번 사용자 삭제
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {
        "message": "사용자 삭제 완료",
        "user_id": user_id
    }


# Swagger Docs 주소
# http://127.0.0.1:8000/docs

# docs에서 확인:
# DELETE /users/{user_id}
#
# 예시 입력:
# user_id = 1

from fastapi import FastAPI, HTTPException

app = FastAPI()

from fastapi import FastAPI, HTTPException

app = FastAPI()


# 임시 사용자 데이터
users = {
    1: "Alice",
    2: "Bob",
    3: "Charlie"
}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    # 사용자 존재 여부 확인
    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="사용자가 존재하지 않습니다."
        )

    # 삭제하면서 삭제된 사용자 이름 저장
    deleted_user = users.pop(user_id)

    return {
        "message": "사용자 삭제 완료",
        "user_id": user_id,
        "deleted_user": deleted_user
    }

# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/users/2
