
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

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