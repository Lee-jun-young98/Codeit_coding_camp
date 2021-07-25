# 상수(constant) 대문자로 작성함
PI = 3.14

def calculate_area(r):
    return PI * r * r

radius = 4
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

radius = 6
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

radius = 7
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

