# ex0907 (09/07) — Git · Debug · Pydantic · Python 기본 문법

## 1. Git 충돌 실습

- GitHub에서 직접 README 수정 → 로컬 파일과 충돌 발생
- 충돌 과정을 직접 경험하면서 `pull`, `push` 이해

```bash
git add .
git commit -m "수정 내용"
git pull
git push
```

### Git이 꼬였을 때

- 숨김 파일 `.git` 삭제 → 로컬 Git 연결 초기화
- GitHub Desktop `Remove` → 로컬 Repository 목록에서 제거
- GitHub 서버 Repository는 그대로 남아 있음
- 다시 필요하면 `Clone repository`
- 원격 Repository 완전 삭제 → `Settings → Danger Zone → Delete this repository`

---

## 2. 디버그 하는 법

- VS Code → `실행 및 디버그`
- 확인할 코드 줄 왼쪽 클릭 → 빨간 점 `Breakpoint`
- 디버그 실행 → Breakpoint에서 실행 정지
- 변수값과 코드 실행 흐름 확인
- 오류가 발생한 위치와 원인 확인에 사용

---

# Pydantic

## 3. 기본: 데이터 검증과 타입 변환

- Python의 Pydantic ≒ Java의 Validation
- 들어오는 데이터의 타입/형식 검증
- `BaseModel`을 상속해 모델 정의
- 필요한 경우 Pydantic이 지정한 타입으로 변환

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
```

---

## 4. 기본값 · Optional · 중첩 모델

### 기본값

```python
class User(BaseModel):
    name: str
    age: int = 20
```

### Optional

```python
from typing import Optional

class User(BaseModel):
    name: str
    nickname: Optional[str] = None
```

- 값이 없어도 되는 필드 → `Optional`
- 모델 안에 다른 모델을 넣어 중첩 구조 표현 가능

```text
User
 ├─ name
 └─ address
     ├─ city
     └─ zipcode
```

### 핵심

`입력 데이터 → Pydantic 검증 → 정상 데이터 → 로직 실행`

- 검증을 어디까지 적용할지도 설계의 일부

---

# Python 기본 문법

## 5. 빈 문자열 제거 — `strip()` / `continue`

```python
questions = ["asyncio란?", "", "FastAPI란?"]
valid_questions: list[str] = []

for question in questions:

    # 문자열 양쪽 공백 제거
    cleaned = question.strip()

    if not cleaned:
        continue

    valid_questions.append(cleaned)

print(valid_questions)

# ['asyncio란?', 'FastAPI란?']
```

- `strip()` → 문자열 양쪽 공백 제거
- `if not cleaned:` → 빈 문자열 확인
- `continue` → 현재 반복을 건너뛰고 다음 반복
- `append()` → 리스트에 값 추가

---

## 6. 이번 주 개발 방향

- 이번 주 Git 적극적으로 사용
- Git 충돌 및 복구 과정 연습
- 수~목 Streamlit 화면 배포 예정
- Python Full Stack 프로젝트 결과물 완성
- 개발 = 코드 작성뿐 아니라 **로직과 연결 순서 설계**
- `A → B → C` 형태로 기능이 어떻게 연결되는지 생각
- Pydantic 검증 범위 등도 직접 설계