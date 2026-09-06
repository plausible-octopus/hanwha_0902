# ex0904 (09/04) — Python 문법 · NumPy · Git/GitHub

셋째 날. Python 문법을 복습하고 **NumPy 배열과 인덱싱**,  
**Git/GitHub를 이용한 버전 관리**를 학습.

## 다루는 내용

- 전역변수(Global) / 지역변수(Local)
- 클래스와 상속 기초
- NumPy 1차원 / 2차원 / 3차원 배열
- 인덱싱과 슬라이싱
- Git / GitHub 기본 개념
- GitHub Desktop
- `.gitignore`와 가상환경 관리

## 파일

| 파일 | 설명 |
|---|---|
| `python_practice.py` | 변수, 함수, 클래스, 상속 복습 |
| `numpy_practice.py` | NumPy 배열, 차원, 인덱싱, 슬라이싱 |

---

## 1. Global / Local Variable

변수는 선언 위치에 따라 사용할 수 있는 범위가 달라짐.

```python
# Global
message = "Python is awesome"

def show_global():
    print(message)

show_global()


# Local
def show_local():
    message = "Python practice"
    print(message)

show_local()
```

- 함수 밖에서 선언 → **전역변수(Global)**
- 함수 안에서 선언 → **지역변수(Local)**

---

## 2. Class / Inheritance

클래스로 데이터와 기능을 하나로 묶을 수 있음.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

class Student(Person):
    pass
```

`Student(Person)`처럼 기존 클래스의 기능을 물려받는 것을 **상속(Inheritance)**이라고 함.

---

## 3. NumPy 배열

```python
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

arr3 = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])

print(arr1.ndim)  # 1
print(arr2.ndim)  # 2
print(arr3.ndim)  # 3
```

- `np.array()` : NumPy 배열 생성
- `ndim` : 배열의 차원 확인
- 1차원 → 하나의 배열
- 2차원 → 행 / 열
- 3차원 → 2차원 배열이 여러 개 쌓인 구조

---

## 4. 인덱싱

인덱스는 `0`부터 시작.

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr[1, 2])   # 6
print(arr[1, -1])  # 6
```

2차원 배열은 `arr[행, 열]`로 접근.

`-1`은 뒤에서 첫 번째 값.

---

## 5. 슬라이싱

기본 형태:

```text
[start : end : step]
```

```python
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])  # [2 3 4 5]
print(arr[:4])   # [1 2 3 4]
print(arr[4:])   # [5 6 7]
print(arr[::2])  # [1 3 5 7]
```

- `start` : 시작
- `end` : 끝 (**해당 위치는 포함 X**)
- `step` : 간격

### 2차원 슬라이싱

```python
arr = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])

print(arr[1, 1:4])     # [7 8 9]
print(arr[0:2, 1:4])
```

---

## 6. Git / GitHub

**Git** → 파일의 변경 이력을 관리하는 버전 관리 시스템  
**GitHub** → Git 저장소를 온라인에서 저장하고 공유하는 서비스

기본 흐름:

```text
파일 수정
   ↓
git add
   ↓
git commit
   ↓
git push
   ↓
GitHub
```

자주 사용하는 명령어:

```bash
git status
git add .
git commit -m "0904 practice"
git push
```

---

## 7. GitHub Desktop

명령어 대신 GUI로 Git을 관리할 수 있는 프로그램.

```text
File > New repository
        ↓
Create repository
        ↓
파일 수정
        ↓
Commit to main
        ↓
Push origin
```

---

## 8. `.gitignore`

가상환경이나 불필요한 파일이 GitHub에 올라가지 않도록 제외.

```gitignore
.venv/
.thirdenv/
__pycache__/
*.pyc
.env
```

가상환경 폴더는 GitHub에 올리지 않고 로컬에서 따로 생성.

---

## 핵심 정리

- **Global / Local** → 변수를 선언한 위치에 따라 범위가 달라짐
- **NumPy** → 다차원 배열과 수치 데이터를 다루는 라이브러리
- **Index** → `0`부터 시작
- **2차원 배열** → `[행, 열]`
- **Slice** → `[start:end:step]`, `end`는 포함 X
- **Git** → 변경 이력 관리
- **GitHub** → Git 저장소를 온라인에서 관리
- **Commit → Push** → 변경 내용을 저장하고 GitHub에 반영