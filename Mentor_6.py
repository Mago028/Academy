# 6강
# p.111
# 1번
num = int(input('정수를 입력하세요>> '))
count = 0
if num < 0:
    print('잘못된 입력입니다.')
else:
    while True:
        count += 1
        print(f'{count}번째 Hello')
        if num == count:
            break

# 2번
num = 1
while num <= 100:
    num += 1
    if num % 7 == 0:
        print(num)

# 3번
money = int(input('자판기에 얼마를 넣을까요??>> '))
count = 0
while money > 300:
    count += 1
    money -= 300
    print(f'커피 {count}잔, 잔돈 {money}원')

# 4번
s = set()
while len(s) < 5:
    number = int(input('0~9 사이 정수를 입력하세요>> '))
    s.add(number)
print('모두 입력되었습니다.')
print(f'입력된 값은 {s}')

# 5번
number = 1
while number <= 100:
    print(number, end='\t')
    if number % 10 == 0:
        print()
    number += 1

# 6번
n = 1
while n <= 9:
    m = 2
    while m <= 9:
        print(f'{m}X{n}={m*n}', end='\t')
        if m == 9:
            print()
        m += 1
    n += 1

