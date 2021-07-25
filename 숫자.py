import random

def program():
    a = int(input("숫자를 입력하세요: "))
    start = 1

    while start == 1:
        b = random.randint(1,100)
        if a == b:
            start -= 1
        else:
            print("{}은 정답이 아닙니다.")

    print("정답은 {}입니다.".format(b))


program()