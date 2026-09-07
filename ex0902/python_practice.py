# 2026-09-02 Python 기초 실습


# 1. 변수
name = "Python"
age = 29

print(name)
print(age)


# 2. 기본 자료형
text = "Python"
number = 10
decimal = 3.14
is_student = True

print(type(text))
print(type(number))
print(type(decimal))
print(type(is_student))


# 3. 리스트
fruits = ["apple", "banana", "orange"]

print(fruits)
print(fruits[0])

fruits.append("grape")
print(fruits)


# 4. 반복문
for i in range(5):
    print(i)


# 5. range()
# 0부터 4까지
for i in range(5):
    print(i)

# 1부터 5까지
for i in range(1, 6):
    print(i)


# 6. 함수
def hello(name):
    print("Hello", name)


hello("Python")


# 7. print()와 sep
print("2026", "09", "02", sep="-")
print("Python", "Java", "C", sep=" / ")


# 8. global
count = 0


def increase():
    global count
    count += 1


increase()
print(count)


# 9. 라이브러리와 함수
import math

print(math.sqrt(16))