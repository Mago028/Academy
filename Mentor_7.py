# 멘토씨리즈파이썬
# 7강
# p.129
# 1번
for n in range(5, 0, -1):
    print(n)

# 2번
num = int(input('임의의 양수를 입력하세요>> '))
sum = 0
for num in range(0, num+1):
    sum += num
print(f'1부터 {num}사이 모든 정수와 합계는 {sum}입니다.')

# 3번
li = []
basket = int(input('몇 개의 과일을 보관할까요?>> '))
for basket in range(0, basket):
    fruit = input(f'{basket+1}번째 과일을 입력하세요>> ')
    li.append(fruit)
print(f'입력받은 과일들은 {li}입니다.')

# 4번
exam = [99, 78, 100, 91, 81, 85, 54, 100, 71, 50]
score = []
for i in exam:
    score.append(100 if i > 95 else i+5)
print(score)

# 5번
for i in range(1, 101):
    str_i = str(i)
    count = 0
    for x in str_i:
        if (x == '3') or (x == '6') or (x == '9'):
            count += 1
    if count == 0:
        print(i, end='\t\t')
    else:
        print(count * '짝', end='\t\t')
    if i % 10 == 0:
        print()