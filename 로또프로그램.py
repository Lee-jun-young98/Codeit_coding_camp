import random

def generate_numbers(n):
    # 지난 과제의 코드를 붙여 넣으세요.
    numbers = []
    while len(numbers) < n:
        num = random.randint(1, 45)
        if num not in numbers:
            numbers.append(num)
    return numbers



def draw_winning_numbers():
    list_lot = sorted(generate_numbers(6))
    while len(list_lot) != 7:
        num = random.randint(1,45)
        if num not in list_lot:
            list_lot.append(num)
    return list_lot


def count_matching_numbers(numbers, winning_numbers):
    count = 0
    for num in numbers:
        if num in winning_numbers:
            count = count + 1
    return count

print(count_matching_numbers([2,7,11,14,25,40],[14]))

def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

    if count == 6:
        return 1000000000
    elif count == 5 and bonus_count == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0



print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))