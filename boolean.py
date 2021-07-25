print(True and True)
print(True or False)
print(False or True)
print(False or False)


print(2>1)
print(2<1)
print(3>=2)
print(3<=3)
print(2==2)
print(2!=2)

print(2 > 1 and "Hello" == "Hello")

print(not not True)

print(7 == 7 or (4<3 and 12 > 10))

print(type(4/2))
print(type("True"))
print(type(2.0**3))
print(type(2*3==6))

## return에서 값을 주었으면 뒤에 작성한 것이 나오지 않는다. -> return에서 함수 종료 기능이 있다.
def square(x):
    print("함수시작")
    return(x * x)
    print("함수끝")

print(square(2) + square(3))


