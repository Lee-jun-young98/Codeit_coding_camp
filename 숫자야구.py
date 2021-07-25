import random

def generate_numbers(n):
    numbers = []

    while len(numbers) < n:
        new_number = random.randint(0,9)

        if new_number not in numbers:
            numbers.append(new_number)

    return numbers

def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력해 입력하세요.")

    new_guess = []
    count = 1
    while len(new_guess) != 3:
        a = int(input("{}번째 숫자를 입력하세요: ".format(count)))
        if a >= 10 or a < 0:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            continue

        if a in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
            continue

        if a not in new_guess:
            new_guess.append(a)
            count = count + 1

    return new_guess


def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    for i in range(0, len(guess)):
            if guess[i] == solution[i]:
                strike_count = strike_count + 1
            elif guess[i] in solution:
                ball_count = ball_count + 1

    return strike_count, ball_count

def game_start():
    print("0과 9사이에 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.")
    ANSWER = generate_numbers(3)
    tries = 0
    guess = []
    while guess != ANSWER:
        guess = take_guess()
        s, b = get_score(guess, ANSWER)
        print("{0}S" "{1}B".format(s, b))
        tries += 1

    print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))

game_start()