# 2026-09-02 Python 기초

## 1. Python 개발 환경 구축

- Python 설치 및 버전 확인
- VS Code 설치
- Python Extension 설치
- 가상환경(venv) 생성 및 활성화
- VS Code에서 Python 실행 환경 설정

## 2. 가상환경 (venv)

프로젝트별 패키지와 라이브러리를 독립적으로 관리할 때 사용

```bash
# 가상환경 생성
python -m venv .venv

# 가상환경 활성화 (Mac)
source .venv/bin/activate
```

가상환경 폴더는 GitHub 업로드 대상에서 제외

`.gitignore`에 가상환경 폴더 등록

```gitignore
.venv/
venv/
```

### 가상환경을 사용하는 이유

- 프로젝트별 패키지 독립 관리 가능
- 프로젝트마다 다른 버전의 라이브러리 사용 가능
- 패키지 충돌 방지
- 필요한 패키지만 별도로 설치 가능

---

## 3. Python 기본 문법

### 변수

값을 저장할 때 사용

```python
name = "Python"
age = 29

print(name)
print(age)
```

### 리스트

여러 개의 값을 하나의 변수에 저장 가능

```python
fruits = ["apple", "banana", "orange"]

print(fruits)
print(fruits[0])
```

### 반복문

같은 작업을 여러 번 반복할 때 사용

```python
for i in range(5):
    print(i)
```

### range()

숫자의 범위를 만들어 반복문에서 사용 가능

```python
for i in range(1, 6):
    print(i)
```

- `range(5)` → 0부터 4까지
- `range(1, 6)` → 1부터 5까지
- 마지막 숫자는 포함되지 않음

### 함수

반복해서 사용하는 코드를 하나의 기능으로 묶어서 사용 가능

```python
def hello(name):
    print("Hello", name)

hello("Python")
```

### print()와 sep

`sep`을 이용해 출력되는 값 사이의 구분자 지정 가능

```python
print("2026", "09", "02", sep="-")
```

출력 결과

```text
2026-09-02
```

### global

함수 내부에서 전역 변수의 값을 변경할 때 사용

```python
count = 0

def increase():
    global count
    count += 1

increase()
print(count)
```

---

## 4. 라이브러리와 함수

### 함수 (Function)

특정 작업을 수행하도록 만든 코드

```python
def add(a, b):
    return a + b
```

### 라이브러리 (Library)

여러 함수, 클래스, 모듈 등을 모아놓은 코드 모음

필요한 기능을 `import`하여 사용 가능

```python
import math

print(math.sqrt(16))
```

### 차이

- 함수 → 하나의 특정 기능 수행
- 라이브러리 → 여러 기능을 모아놓은 코드 모음
- 기본 문법은 별도의 라이브러리 설치 없이 사용 가능
- 외부 라이브러리는 필요한 경우 설치 후 `import`하여 사용

---

## 5. Git / GitHub 기초

작성한 코드의 변경사항 관리 및 GitHub 업로드 가능

```bash
git add .
git commit -m "학습 내용 정리"
git push
```

- `git add .` → 변경된 파일 추가
- `git commit` → 변경사항 기록
- `git push` → GitHub 원격 저장소에 업로드

---

## 파일 구성

```text
ex0902/
├── README.md
└── python_practice.py
```

- `README.md` → 09/02 학습 내용 정리
- `python_practice.py` → Python 기본 문법 실습