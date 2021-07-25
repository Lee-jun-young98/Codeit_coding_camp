import random

# 코드를 작성하세요.
def program():
    a = random.randint(1, 20)
    chance = 4
    count = 1
    while chance != 0:
        number = int(input("기회가 {}번남았습니다.1 - 20 사이의 숫자를 맞혀보세요:".format(chance)))
        if a > number:
            chance -= 1
            count += 1
            print("Up")
        elif number == a:
            print("축하합니다. {}번만에 숫자를 맞히셨습니다.".format(count))
            break;
        else:
            chance -= 1
            count += 1
            print("Down")

program()