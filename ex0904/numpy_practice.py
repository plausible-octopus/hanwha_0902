# 09/04 NumPy Practice

import numpy as np


# 1. NumPy 배열 만들기

arr1 = np.array([1, 2, 3])

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

arr3 = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])

print("1차원:", arr1)
print("2차원:")
print(arr2)
print("3차원:")
print(arr3)


# 2. 배열 차원 확인

print("arr1 차원:", arr1.ndim)
print("arr2 차원:", arr2.ndim)
print("arr3 차원:", arr3.ndim)


# 3. 인덱싱
# 인덱스는 0부터 시작

print(arr1[0])       # 1
print(arr2[1, 2])    # 6
print(arr3[0, 1, 2]) # 6


# 4. 음수 인덱스
# -1은 뒤에서 첫 번째 값

print(arr2[1, -1])   # 6


# 5. 슬라이싱
# [start:end:step]
# end 위치는 포함하지 않음

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])   # [2 3 4 5]
print(arr[:4])    # [1 2 3 4]
print(arr[4:])    # [5 6 7]
print(arr[::2])   # [1 3 5 7]


# 6. 2차원 배열 슬라이싱

matrix = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])

print(matrix[1, 1:4])     # [7 8 9]
print(matrix[0:2, 1:4])


# 7. 데이터 타입 확인

print(arr.dtype)