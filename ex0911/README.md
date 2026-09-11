# 2026-09-11 OpenAI API Key 설정

## 1. API Key

OpenAI API Key는 Python, FastAPI, Colab 등의 프로그램에서 OpenAI API를 사용할 때 필요한 인증키다.

- 프로그램이 OpenAI 서비스를 사용할 수 있도록 인증
- 사용량 및 과금 계정 구분
- 비밀번호처럼 외부에 노출하지 않기

---

## 2. 가상환경 생성

```cmd
python -m venv .venv
```

가상환경 활성화:

```cmd
.venv\Scripts\activate
```

활성화되면 터미널 앞에 `(.venv)`가 표시된다.

---

## 3. 필요한 패키지 설치

```cmd
pip install openai python-dotenv
```

- `openai` : OpenAI API 사용
- `python-dotenv` : `.env` 파일의 환경변수 불러오기

---

## 4. `.env` 파일 생성

프로젝트 폴더 안에 `.env` 파일을 만든다.

```text
OPENAI_API_KEY=실제_API_KEY
```

### `.env`를 사용하는 이유

API Key를 Python 코드에 직접 작성하지 않고 별도 파일에 저장한다.

- API Key 노출 방지
- 코드와 비밀정보 분리
- GitHub 업로드 시 실수 방지

---

## 5. `.gitignore` 설정

`.gitignore` 파일을 만들고 아래 내용을 작성한다.

```gitignore
.venv/
.env
```

- `.venv/` : 가상환경 폴더 Git 제외
- `.env` : API Key가 들어있는 파일 Git 제외

`.env`는 비밀정보를 코드에서 분리하고, `.gitignore`는 `.env`가 GitHub에 올라가지 않도록 차단한다.

---

## 6. Python에서 API Key 불러오기

`keytest.py`

```python
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)
```

- `load_dotenv()` : `.env` 파일 불러오기
- `os.getenv("OPENAI_API_KEY")` : 저장된 API Key 가져오기
- `OpenAI(api_key=api_key)` : OpenAI 클라이언트 생성

---

## 7. API 연결 테스트

```python
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("HANWHA_OPENAI_KEY")

client = OpenAI(api_key=api_key)

try:
    response = client.responses.create(
        model="gpt-5.6-luna",
        input="연결 테스트입니다. OK라고만 답해줘."
    )

    print("OpenAI API 연결 성공")
    print(response.output_text)

except Exception as e:
    print("연결 실패")
    print(e)
```

실행:

```cmd
python keytest.py
```

정상 실행:

```text
OpenAI API 연결 성공
OK
```
- 교재 저자 GitHub 계정: `teddylee777`
- LangChain은 버전에 따라 코드 사용법이 달라질 수 있음
- 교재 코드와 현재 설치된 LangChain 버전이 다르면 오류가 발생할 수 있음
- 코드가 맞는데 오류가 나면 먼저 버전 차이 확인

### 현재 LangChain 버전 확인

```cmd
pip show langchain
---
pip list | findstr langchain

## 핵심 정리

- API Key = OpenAI API 사용을 위한 인증키
- API Key는 `.env` 파일에 저장
- `.env`는 `.gitignore`에 추가해서 GitHub 업로드 차단
- `python-dotenv`로 `.env`의 값을 Python에서 불러옴
- 실제 코드에는 API Key를 직접 작성하지 않음

## LangChain 버전에 따른 모델 설정

### ChatOpenAI 모델 지정

LangChain 버전에 따라 `ChatOpenAI`의 모델 지정 방식이 다를 수 있으므로 버전 확인 필요.

### 이전 버전 예시 (0.3.x)

```python
llm = ChatOpenAI(
    temperature=0.1,
    model_name="gpt-4o-mini"
)
```

### 1.x 버전

```python
llm = ChatOpenAI(
    temperature=0.1,
    model="gpt-4o-mini"
)
```

### 핵심

- 교재나 기존 예제는 LangChain `0.3.x` 버전 기준일 수 있음
- 현재 LangChain `1.x` 버전과 기존 예제 코드의 사용법이 다를 수 있음
- 코드 실행 전 현재 설치된 LangChain 버전 확인
- 버전 차이로 오류가 발생하면 현재 버전에 맞게 코드 수정
- `model_name="gpt-4o-mini"` → `model="gpt-4o-mini"` 형태로 변경해서 사용

### LangChain 버전 확인

터미널에서 확인:

```bash
pip show langchain
```

Python에서 확인:

```python
import langchain
print(langchain.__version__)
```

> 교재와 현재 설치된 LangChain의 버전 차이로 코드가 그대로 실행되지 않을 수 있으므로 버전을 확인하고 현재 버전에 맞는 사용법으로 변경한다.

## requirements.txt

- 프로젝트에 필요한 Python 패키지와 버전을 기록하는 파일
- `.venv` 대신 `requirements.txt`를 GitHub에 업로드

```bash
# 현재 설치된 패키지 저장
pip freeze > requirements.txt

# 패키지 일괄 설치
pip install -r requirements.txt
```