# ex0903 (09/03) — Python · Streamlit · NumPy · Matplotlib

둘째날. Python 기본 문법을 복습하고, **NumPy/Pandas로 데이터를 다루고 Streamlit과 Matplotlib으로 출력하는 방법** 학습

## 다루는 내용

- Python 기본 문법 (`global`, 문자열, Class/Object)
- NumPy / Pandas 기초
- Streamlit 설치 및 실행
- Streamlit 데이터·이미지·차트 출력
- Matplotlib 기본 그래프

## 파일

| 파일 | 내용 |
|---|---|
| `streamlit_basics.py` | Streamlit 데이터 출력, 레이아웃, 이미지, 차트 |
| `matplotlib_plot.py` | NumPy와 Matplotlib 기본 그래프 |

---

## 1. Python 기본 문법

### 전역변수 `global`

함수 내부에서 전역변수 값을 변경할 때 `global` 사용

```python
x = "fantastic"

def myfunc():
    global x
    x = "awesome"
```

### 문자열

```python
text = "Python"

text.upper()  # PYTHON
text.lower()  # python
```

- `upper()` : 대문자 변환
- `lower()` : 소문자 변환

### Class / Object

Class → 객체(Object)를 만들기 위한 틀

```python
class Fruit:
    def __init__(self, name):
        self.name = name

apple = Fruit("apple")
```

`__init__()` → 객체 생성 시 자동 실행

---

## 2. NumPy / Pandas

- NumPy → 배열과 수치 데이터 처리
- Pandas → 표 형태 데이터 처리

```python
import numpy as np

numbers = np.arange(0, 30, 5)
print(numbers)
```

결과:

```text
[ 0  5 10 15 20 25 ]
```

`np.arange(시작, 끝, 간격)`

→ 끝 값은 포함하지 않음

Pandas의 `DataFrame` → 엑셀과 비슷한 표 형태의 데이터

---

## 3. Streamlit

Python 코드만으로 웹 앱이나 데이터 화면을 빠르게 만들 수 있는 라이브러리

### 설치

```cmd
pip install streamlit numpy pandas altair
```

설치 확인:

```cmd
streamlit hello
```

### 실행

```cmd
streamlit run streamlit_basics.py
```

종료:

```text
Ctrl + C
```

### 주요 기능

| API | 기능 |
|---|---|
| `st.write()` | 데이터 출력 |
| `st.dataframe()` | 표 출력 |
| `st.columns()` | 화면을 여러 열로 분할 |
| `st.image()` | 이미지 출력 |
| `st.altair_chart()` | 차트 출력 |
| `st.latex()` | 수식 출력 |

---

## 4. Matplotlib

Python에서 데이터를 그래프로 시각화할 때 사용하는 라이브러리

```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, "*:y")
plt.show()
```

`"*:y"` 의미

- `*` → 별 모양 마커
- `:` → 점선
- `y` → yellow(노란색)

> 모든 옵션을 외우기보다 필요한 기능을 찾아서 사용하기

---

## 실행 방법

### 가상환경 생성 / 활성화

```cmd
python -m venv .secondvenv
.secondvenv\Scripts\activate.bat
```

### 라이브러리 설치

```cmd
pip install streamlit numpy pandas altair matplotlib
```

### 실행

```cmd
streamlit run streamlit_basics.py
python matplotlib_plot.py
```

## 참고

- Streamlit 공식 문서: https://docs.streamlit.io/
- Matplotlib 공식 문서: https://matplotlib.org/
- NumPy 공식 문서: https://numpy.org/doc/