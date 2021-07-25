with open("vocabulary.txt", "w") as f:
    while True:
        a = input("영어 단어를 입력하세요: ")
        if a == "q":
            break
        b = input("한국어 뜻을 입력하세요: ")
        if b == "q":
            break
        f.write("{}: {}\n".format(a, b))

