
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
# 파이덴틱(Pydantic): 들어오는 데이터가 내가 정한 형식에 맞는지 검사해주는 도구
# BaseModel: Pydantic에서 데이터 형식을 정의할 때 상속해서 쓰는 기본 클래스

app = FastAPI()


# 임시 아이템 데이터
items = {
    1: {"name": "사과", "price": 1000},
    2: {"name": "바나나", "price": 2000},
    3: {"name": "포도", "price": 3000}
}


class Item(BaseModel):
    name: str
    price: int


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/items/")
async def create_item(item: Item):
    return {
        "message": "아이템 생성 완료",
        "item": item
    }


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):

    # 아이템 존재 여부 확인
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="아이템이 존재하지 않습니다."
        )

    # 데이터 수정
    items[item_id] = {
        "name": item.name,
        "price": item.price
    }

    return {
        "message": "아이템 수정 완료",
        "item_id": item_id,
        "updated_item": items[item_id]
    }


# http://127.0.0.1:8000/docs

# C = Create = POST   = 생성
# R = Read   = GET    = 조회
# U = Update = PUT    = 수정
# D = Delete = DELETE = 삭제

# 임시 데이터
items = {
    1: {"name": "사과", "price": 1000},
    2: {"name": "바나나", "price": 2000}
}


# 데이터 형식
class Item(BaseModel):
    name: str
    price: int


# CREATE - 생성
@app.post("/items/")
async def create_item(item: Item):

    # 새 아이디 생성
    new_id = max(items.keys()) + 1

    items[new_id] = {
        "name": item.name,
        "price": item.price
    }

    return {
        "message": "아이템 생성 완료",
        "item_id": new_id,
        "item": items[new_id]
    }


# READ - 전체 조회
@app.get("/items/")
async def read_items():
    return items


# READ - 한 개 조회
@app.get("/items/{item_id}")
async def read_item(item_id: int):

    # 아이템 존재 여부 확인
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="아이템이 존재하지 않습니다."
        )

    return {
        "item_id": item_id,
        "item": items[item_id]
    }


# UPDATE - 수정
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):

    # 아이템 존재 여부 확인
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="아이템이 존재하지 않습니다."
        )

    # 데이터 수정
    items[item_id] = {
        "name": item.name,
        "price": item.price
    }

    return {
        "message": "아이템 수정 완료",
        "item_id": item_id,
        "updated_item": items[item_id]
    }


# DELETE - 삭제
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):

    # 아이템 존재 여부 확인
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="아이템이 존재하지 않습니다."
        )

    # 삭제된 데이터 저장
    deleted_item = items.pop(item_id)

    return {
        "message": "아이템 삭제 완료",
        "item_id": item_id,
        "deleted_item": deleted_item
    }


# Swagger Docs
# http://127.0.0.1:8000/docs