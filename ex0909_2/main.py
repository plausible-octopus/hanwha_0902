from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
# CRUD
# CREATE = POST = 생성
# READ = GET = 조회
# UPDATE = PUT = 수정
# DELETE = DELETE = 삭제


# 임시 데이터
items = {
    1: {"name": "노트북", "price": 1500000},
    2: {"name": "마우스", "price": 50000}
}


# 데이터 형식
class Item(BaseModel):
    name: str
    price: int


# CREATE = POST = 생성
@app.post("/items/")
async def create_item(item: Item):

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


# READ = GET = 전체 목록 조회
@app.get("/items/")
async def read_items():

    return {
        "message": "전체 목록 조회 완료",
        "items": items
    }


# READ = GET = 단일 조회
@app.get("/items/{item_id}")
async def read_item(item_id: int):

    # 아이템 존재 여부 확인
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="아이템이 존재하지 않습니다."
        )

    return {
        "message": "단일 조회 완료",
        "item_id": item_id,
        "item": items[item_id]
    }


# UPDATE = PUT = 수정
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
        "message": "수정 완료",
        "item_id": item_id,
        "item": items[item_id]
    }


# DELETE = DELETE = 삭제
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):

    # 아이템 존재 여부 확인
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="아이템이 존재하지 않습니다."
        )

    # 데이터 삭제
    deleted_item = items.pop(item_id)

    return {
        "message": "삭제 완료",
        "item_id": item_id,
        "deleted_item": deleted_item
    }


# Swagger Docs
# http://127.0.0.1:8000/docs


class ItemSchema(BaseModel):
    name: str
    price: int
    desc: str


# 임시 데이터
items_db = {
    1: {"name": "사과", "price": 3000, "desc": "맛있는 사과"},
    2: {"name": "바나나", "price": 2000, "desc": "달콤한 바나나"}
}


# 생성 Create
@app.post("/items/")
async def create_item(item: ItemSchema):
    item_id = max(items_db.keys(), default=0) + 1
    items_db[item_id] = item.model_dump()

    return {"msg": "아이템 생성 완료", "data": items_db[item_id]}


# 전체 조회 Read
@app.get("/items/")
async def get_items():
    return {"msg": "전체 조회 완료", "data": items_db}


# 단일 조회 Read
# http://127.0.0.1:8000/items/1
@app.get("/items/{item_id}")
async def get_item(item_id: int):

    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="제품을 찾을 수 없습니다.")

    return {"msg": "단일 조회 완료", "data": items_db[item_id]}


# 수정 Update
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: ItemSchema):

    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="제품을 찾을 수 없습니다.")

    items_db[item_id] = item.model_dump()

    return {"msg": "수정 완료", "data": items_db[item_id]}


# 삭제 Delete
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):

    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="제품을 찾을 수 없습니다.")

    deleted_item = items_db.pop(item_id)

    return {"msg": "삭제 완료", "data": deleted_item}
