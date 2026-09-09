from fastapi import FastAPI
from enum import Enum

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# http://localhost:8000/
@app.get("/")
def read_root():
    return {"Hello": "World"}


# http://localhost:8000/items/555
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


# http://localhost:8000/users/me
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "나는 me입니다"}


# http://localhost:8000/users/사용자
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"사용자아이디(user_id)": user_id}

# 같은 HTTP 메소드 + 같은 경로를 중복 정의하면
# 먼저 등록된 경로가 매칭됨**
# 따라서 같은 메소드와 같은 경로는 중복해서 만들지 않는 것
# 이 좋음

# http://localhost:8000/users
@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]

# http://localhost:8000/users
@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]

# http://localhost:8000/models/{aaa}
# http://localhost:8000/models/{resnet}
# http://localhost:8000/models/{lenet}
# http://localhost:8000/models/{기타}

from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
    aaa = "기타"

# http://localhost:8000/models/
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    # 키를 요청하면, 값을 reteurn
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    #값을 요청하면, 키를 reteurn
    if model_name.value == "resnet":
         # 값을 찾아서 키를 return
        return {"model_name": model_name, "message": "LeCNN all the images"}

    #그 외의 상황
    return {"model_name": model_name, "message": "Have some residuals"}

# http://localhost:8000/items/
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    # return fake_items_db[skip : skip + limit]  
    #                       0  :   0  +  10
    # 범위연산자
    return fake_items_db[0 : 1]

# http://127.0.0.1:8000/items/foo-item
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

async def get_model(model_name: ModelName):
    return {"model_name": model_name, "items": items}

    # 그 외에 상황
    return {"model_name": model_name, "message": "그 외에, Have some residuals"}


# http://localhost:8000/items/
# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]
#     # return fake_items_db[0 : 10]
#     # 범위연산자
#     # return fake_items_db[0 : 2]


# http://localhost:8000/items2/test
# http://localhost:8000/items2/test?q=None
@app.get("/items2/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


