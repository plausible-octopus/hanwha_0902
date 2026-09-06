# 09/04 Python Practice
# Python 기본 문법 복습


# 1. 문자열과 변수
name = "Johnny"
age = 29

print(f"My name is {name}, I am {age}")


# 2. Dictionary
car = {
    "brand": "Kia",
    "model": "Sportage",
    "year": 2026
}

print(car["brand"])
print(car.keys())


# 3. 함수와 전역변수(Global)
message = "Python is awesome"

def show_global():
    print(message)

show_global()


# 4. 지역변수(Local)
def show_local():
    message = "Python practice"
    print(message)

show_local()

# 함수 밖에서는 전역변수가 유지됨
print(message)


# 5. Class
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")


person = Person("Johnny")
person.greet()


# 6. 상속(Inheritance)
class Student(Person):
    pass


student = Student("John")
student.greet()