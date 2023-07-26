# 멘토씨리즈파이썬
# 8강
# p.141_1
print('현재 10000원있습니다.')
money = 10000
while money > 0:
    price = int(input('사용할 금액 입력>> '))
    if price <= 0:
        print('0원 이하의 금액은 사용할 수 없습니다.')
        continue
    money -= price
    print(f'현재 {money}원이 있습니다.')
# p.141_2
while True:
    score = int(input('이번 영화의 평점을 입력하세요>> '))
    if score <= 0 or score > 5:
        print('평점은 1~5 사이만 입력할 수 있습니다.')
        continue
    else:
        print(f"평점: {'⭐'*score}")
        break
# p.142_3
count = 1
while count <= 5:
    password = input('비밀번호를 입력하세요>>> ')
    if password == 'qwerty':
        print('비밀번호를 맞혔습니다.')
        break
    if count == 5:
        print('비밀번호 입력 횟수를 초과했습니다.')
    count += 1
# p.143_4
dan = 1
while dan <= 9:
    dan += 2
    if dan >= 10:
        break
    n = 1
    while True:
        if dan % 2 == 1:
            n += 1
            print('{}x{}={}'.format(dan, n, dan*n))
            if n == dan:
                print()
                break
