my_family = {
    '엄마': '김자옥',
    '아빠': '이석진',
    '아들': '이동민',
    '딸': '이지영'
}

## 안에있는 값들
for value in my_family.values():
    print(value)

for key in my_family.keys():
    print(key)

for key, value in my_family.items():
    print(key, value)