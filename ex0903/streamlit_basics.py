import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


# 1. 기본 출력
st.write("Hello, Streamlit!")


# 2. Pandas DataFrame
df = pd.DataFrame({
    "first column": [1, 2, 3, 4],
    "second column": [10, 20, 30, 40],
})

st.write("DataFrame")
st.dataframe(df)


# 3. NumPy 난수 데이터
dataframe = np.random.randn(10, 20)

st.write("NumPy Random Data")
st.dataframe(dataframe)


# 4. 화면을 3개의 컬럼으로 나누기
col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")


# 5. Altair 차트
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

chart = (
    alt.Chart(chart_data.reset_index())
    .mark_line()
    .encode(
        x="index",
        y="a"
    )
)

st.altair_chart(chart, use_container_width=True)


# 6. 수식 출력
st.latex(r"a^2 + b^2 = c^2")