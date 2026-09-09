# FastAPI

## 1. FastAPI 시작

### 가상환경 생성

```cmd
python -m venv .fastvenv
```

### 가상환경 활성화

```cmd
.fastvenv\Scripts\activate
```

활성화되면 터미널 앞에 `(.fastvenv)`가 표시된다.

---

## 2. FastAPI 설치

```cmd
pip install fastapi uvicorn
```

- **FastAPI** : API를 만들기 위한 Python 웹 프레임워크
- **Uvicorn** : FastAPI 애플리케이션을 실행하는 서버

---

## 3. FastAPI 기본 코드

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
```

- `FastAPI()` → FastAPI 애플리케이션 객체 생성
- `@app.get("/")` → `/` 주소로 들어오는 GET 요청 처리
- `item_id: int` → `item_id`를 정수 타입으로 받음
- `q: str | None = None` → `q`는 문자열 또는 `None`

---

## 4. reload

개발 중 코드 변경사항을 바로 반영하기 위해 `--reload`를 사용한다.

```cmd
uvicorn main:app --reload
```

코드 수정 → 저장(`Ctrl + S`) → 변경 감지 → 서버 자동 재시작 → 수정 내용 반영

- `main` → `main.py`
- `app` → `main.py` 안의 FastAPI 객체
- `--reload` → 코드 변경 시 서버 자동 재시작
- 개발 환경에서 사용하며 실제 운영 환경에서는 일반적으로 사용하지 않는다.

---

## 5. port

포트는 문서나 순서를 정리하는 기능이 아니라 **서버 실행/통신과 관련된 번호**이다.

한 컴퓨터에서 여러 서버를 구분해서 실행할 때 사용한다.

같은 포트를 두 서버가 동시에 사용하면 충돌할 수 있기 때문에 `--port`로 다른 포트를 지정할 수 있다.

```cmd
uvicorn main:app --reload --port 8001
```

- `--port 8001` → 서버를 8001번 포트에서 실행

예)

- FastAPI → `8000`, `8001`
- Streamlit → `8501`

### 옵션 차이

- `--reload` → 코드 변경 시 서버 자동 재시작
- `--port` → 서버가 사용할 포트 번호 지정

---

## 6. Uvicorn 서버 실행 확인

```text
Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

- Uvicorn 서버가 `127.0.0.1`의 **8000번 포트에서 실행 중**
- `http://127.0.0.1:8000` → 현재 실행 중인 서버 주소
- `8000` → 현재 사용 중인 포트 번호
- `Ctrl + C` → 실행 중인 서버 종료

---

## 7. localhost와 port

- **localhost = 내 컴퓨터**
- **port = 내 컴퓨터 안에서 어떤 서버인지 구분하는 번호**

예)

```text
localhost:8000
```

→ 내 컴퓨터의 8000번 포트에서 실행 중인 서버

---

## 8. Framework와 Library 차이

### Library

- 내가 필요할 때 가져다 사용
- 내가 원하는 방식으로 필요한 기능을 호출

### Framework

- 정해진 방식에 맞춰 사용
- Framework가 정해놓은 구조와 규칙을 따라야 함
- **Framework가 시키는 방식으로 해야 함**

### 쉽게 기억

- **Library → 내가 도구를 가져다 씀**
- **Framework → 정해진 틀에 맞춰서 사용**

예)

- FastAPI → Framework
- Pandas, NumPy → Library

## 9. FastAPI 기본 실행

- `from fastapi import FastAPI` → FastAPI 불러오기
- `app = FastAPI()` → FastAPI 앱 생성
- `@app.get("/")` → `/` 경로로 들어오는 GET 요청 처리
- 서버 실행 후 `localhost:8000`에서 실제 응답 확인

### localhost와 port

- `localhost` = 내 컴퓨터
- `port` = 내 컴퓨터 안에서 어떤 서버인지 구분하는 번호
- 예: `localhost:8000`
  → 내 컴퓨터의 8000번 포트에서 실행 중인 서버


## 10. Swagger UI

- `127.0.0.1:8000/docs`로 접속
- FastAPI가 API 문서를 자동으로 만들어 줌
- `Try it out` → 값 입력 → `Execute` 순서로 API 테스트
- `200`번대 = 요청이 정상 처리된 성공 상태

### Response body

- `Response body` = 서버가 클라이언트에게 돌려주는 실제 데이터(응답 본문)
- `200` = 성공 상태 코드
- 예: `{"item_id": 5555, "q": null}` → Response body


## 11. 경로 매개변수와 타입 검증

- `/items/{item_id}`에서 `{item_id}`는 경로를 통해 전달받는 값
- `item_id: int`처럼 타입을 지정할 수 있음
- FastAPI가 지정된 타입을 보고 입력값을 자동으로 검증함
- `int`인데 `tttt`를 입력하면 검증 실패
  → `Value must be an integer`
- `5555`처럼 정수를 입력하면 정상 처리

### None과 null

- `q: str | None = None`
- `q`에 값을 넣지 않으면 기본값은 `None`
- Python에서는 `None`
- JSON 응답에서는 `null`

### 쉽게 기억

- `None` → Python
- `null` → JSON


## 12. API 경로(Path)와 HTTP 메소드(Operation)

- API를 설계할 때 `경로(Path)`는 관심사와 리소스를 분리하는 주요 방법
- `Operation` = HTTP 메소드

### HTTP 메소드

- `GET` = 조회(Read) → 데이터 가져오기
- `POST` = 생성(Create) → 새로운 데이터 만들기
- `PUT` = 수정(Update) → 기존 데이터 수정/교체
- `DELETE` = 삭제(Delete) → 기존 데이터 삭제

### 쉽게 기억

- `GET` → 가져오기
- `POST` → 만들기
- `PUT` → 바꾸기
- `DELETE` → 지우기


## 13. FastAPI 비동기

- `async def` = 비동기 함수를 만드는 문법
- FastAPI에서는 `async def`로 API 함수를 만들 수 있음
- `{item_id}`에 들어온 값이 함수의 `item_id`로 전달됨
- `return`으로 받은 값을 JSON 응답으로 반환
- 비동기는 네트워크, DB, 외부 API처럼 **기다리는 작업이 있을 때**
  기다리는 동안 다른 요청을 처리할 수 있어 효율적

### 쉽게 기억

- 동기 → 한 작업이 끝날 때까지 기다림
- 비동기 → 기다리는 동안 다른 일을 처리할 수 있음


## 14. FastAPI 경로 매칭

- 같은 HTTP 메소드 + 같은 경로를 중복 정의하면
  **먼저 등록된 경로가 매칭됨**
- 따라서 같은 메소드와 같은 경로는 중복해서 만들지 않는 것이 좋음

예:

```python
@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]
```

`/users`로 요청하면 먼저 정의된 함수가 매칭되므로:

```text
["Rick", "Morty"]
```

가 반환됨.


## 15. 고정 경로와 동적 경로 순서

- 고정 경로와 동적 경로가 겹칠 수 있으면 **고정 경로를 먼저 정의**
- 경로는 위에서부터 순서대로 매칭되는 것이 중요함

예:

```text
/users/me
/users/{user_id}
```

- `/users/me`를 먼저 정의해야 함
- 그렇지 않으면 `me`가 일반적인 `user_id` 값으로 처리될 수 있음


## 16. 경로 추가 후 확인 순서

1. 새로운 API 경로 추가
2. 파일 저장
3. `--reload` 실행 중이면 변경사항 자동 반영
4. Swagger(`/docs`) 또는 브라우저 새로고침
5. 추가한 경로가 등록됐는지 확인
6. 실제 API 주소로 접속해서 JSON 응답 확인

### `Not Found`가 나왔을 때

`{"detail":"Not Found"}`

→ 서버가 꺼졌다는 뜻이 아니라  
**요청한 주소와 일치하는 API 경로가 없다는 뜻**

확인 순서:

1. 코드에 해당 경로가 있는지 확인
2. 파일을 저장했는지 확인
3. `/docs`를 새로고침해서 경로가 등록됐는지 확인
4. 브라우저에 입력한 API 주소가 정확한지 확인

## 17. Enum 경로 매개변수

- `Enum` = **들어올 수 있는 값을 미리 정해두는 방법**
- `str, Enum`을 상속하면 FastAPI가 문자열 값이라는 것을 알 수 있음
- 허용할 값들을 미리 고정해서 정의
- 잘못된 값 입력을 막고 Swagger에서도 선택 가능한 값이 표시됨

## 18. Enum과 Swagger UI

- 경로 매개변수에 `Enum` 사용 → Swagger(`/docs`)에 드롭다운 선택창 표시
- 미리 정의한 값만 선택 가능
- 예: `alexnet`, `resnet`, `lenet`
- `/docs` → `Try it out` → 값 선택 → `Execute`

## 19. Enum에 기타 값 추가

```python
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
    aaa = "기타"
```

- `aaa` → Enum 멤버 이름
- `"기타"` → 실제 값
- Swagger 드롭다운에는 `기타`로 표시
- `ModelName.aaa` → 코드에서 해당 멤버에 접근
- `model_name is ModelName.aaa` → `기타` 선택 여부 확인

## 20. 쿼리 매개변수와 범위연산자

```python
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
```

- 쿼리 매개변수 → URL 뒤에 `?`로 값 전달
- 여러 쿼리 매개변수 → `&`로 연결
- 예: `/items/?skip=0&limit=10`
- `skip` → 건너뛸 개수
- `limit` → 가져올 최대 개수
- 값을 생략하면 기본값 적용 → `skip=0`, `limit=10`

### 범위연산자 풀이

```python
# fake_items_db[시작 : 끝]
# 시작 위치 포함, 끝 위치 제외

# skip=0, limit=10
return fake_items_db[0 : 10]

# 0번 인덱스부터 1번 인덱스 전까지
return fake_items_db[0 : 1]
```

- `[0 : 1]` → 0번 데이터 1개만 출력
- 예: `[{"item_name": "Foo"}]`
- `[1 : 3]` → 1번, 2번 데이터 출력

## 21. item_id 타입에 따른 오류 확인

```python
@app.get("/items2/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
```

- `item_id`를 `str` → `int`로 변경해서 실행해보기
- `item_id: str` → 문자열 입력 가능
  - `/items2/test` 가능
- `item_id: int` → 정수로 변환 가능한 값만 입력 가능
  - `/items2/1` 가능
  - `/items2/test` 입력 시 타입 검증 오류
- FastAPI가 경로 매개변수의 타입을 확인하고 검증
- `items2` 경로 이름도 바꿔가며 테스트

## 22. FastAPI 실행 명령어

### 실행명령어-one

```cmd
fastapi dev main.py
```

- FastAPI CLI를 이용한 개발 서버 실행

### 실행명령어-two

```cmd
uvicorn main:app --reload
```

- Uvicorn으로 직접 서버 실행
- `main` → `main.py` 파일
- `app` → `main.py` 안에 만든 FastAPI 객체
- `--reload` → 코드 수정 후 저장하면 서버 자동 재시작

## 23. Pydantic의 BaseModel 임포트

```python
from pydantic import BaseModel
```

- 파일 맨 위 import 부분에 추가
- POST 요청에서 받을 데이터의 구조와 타입을 정의할 때 사용
- 요청 본문(Body)으로 전달하면 사용자 정보가 URL에 직접 표시되지 않음
- `BaseModel` 자체가 정보를 숨기는 기능은 아님