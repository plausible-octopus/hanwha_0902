# FastAPI - 0909

## 1. FastAPI 설치

```bash
pip install "fastapi[standard]"
```

- FastAPI 개발에 필요한 패키지를 설치한다.

---

## 2. 서버 실행

```bash
uvicorn main:app --reload
```

- `main` → `main.py`
- `app` → `app = FastAPI()`
- `--reload` → 코드 수정 시 서버 자동 재실행

기본 주소

```text
http://127.0.0.1:8000
```

---

## 3. Swagger Docs

```text
http://127.0.0.1:8000/docs
```

- FastAPI가 자동으로 제공하는 API 문서
- GET / POST 요청을 직접 테스트할 수 있다.

---
## 4. GET / POST / PUT / DELETE

### GET

- 서버의 데이터를 조회하거나 가져올 때 사용
- 예: 사용자 조회, 상품 목록 조회
- 쉽게 기억: `데이터 줘`

### POST

- 서버에 데이터를 보내서 생성하거나 처리할 때 사용
- 예: 회원가입, 게시글 작성, 주문 생성
- 보통 JSON 데이터를 Body에 담아서 전송
- 쉽게 기억: `이 데이터 받아서 처리해`

### PUT

- 서버에 있는 기존 데이터를 수정하거나 교체할 때 사용
- 예: 사용자 정보 수정, 게시글 수정
- 보통 수정할 데이터를 JSON 형태로 Body에 담아서 전송
- 쉽게 기억: `기존 데이터를 이걸로 바꿔줘`

### DELETE

- 서버에 있는 기존 데이터를 삭제할 때 사용
- 예: 사용자 삭제, 게시글 삭제
- 보통 삭제할 데이터의 ID를 경로에 넣어서 요청
- 쉽게 기억: `이 데이터 삭제해줘`
---

## 5. BaseModel

- POST 요청으로 들어오는 데이터의 형식과 타입을 검증할 때 사용
- Pydantic의 `BaseModel`을 상속해서 작성
- 잘못된 타입의 데이터가 들어오면 FastAPI가 자동으로 검증한다.

---

## 6. pyproject.toml / uv.lock

### pyproject.toml
- 프로젝트 설정과 필요한 패키지 정보를 관리

### uv.lock
- 실제 설치되는 패키지의 정확한 버전을 기록
- 다른 PC에서도 같은 개발 환경을 재현할 수 있게 해준다.
- 보통 직접 수정하지 않고 `uv`가 자동으로 관리한다.

### 쉽게 기억

```text
pyproject.toml → 무엇이 필요한지
uv.lock → 정확히 어떤 버전인지
```