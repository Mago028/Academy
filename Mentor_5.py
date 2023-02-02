# 5강
# P.99
# 1번
score = int(input('점수를 입력하세요>> '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f'점수는 {score}점이고, 학점은 {grade}학점입니다.')

# 2번
num = int(input('정수를 입력하세요>> '))
print(f'{num}는 3의', '배수입니다.' if num % 3 == 0 else '배수가 아닙니다.')

# 3번
n1 = int(input('정수1 입력>> '))
n2 = int(input('정수2 입력>> '))
n3 = int(input('정수3 입력>> '))
if n1 > n2 and n1 > n3:
    print(f'가장 큰 수는 {n1}입니다.')
elif n2 > n1 and n2 > n3:
    print(f'가장 큰 수는 {n2}입니다.')
elif n3 > n1 and n3 > n2:
    print(f'가장 큰 수는 {n3}입니다.')
else:
    print('같은 수를 입력했습니다!')

# 3번_다른풀이
num1, num2, num3 = map(int, input('정수 3개를 입력하시오>>').split())
if num1 > num2 and num1 > num3:
    print(f'가장 큰 수는 {num1}입니다.')
elif num2 > num1 and num2 > num3:
    print(f'가장 큰 수는 {num2}입니다.')
elif num3 > num1 and num3 > num2:
    print(f'가장 큰 수는 {num3}입니다.')
else:
    print('같은 수를 입력했습니다!')

# 4번
car = input('차량번호를 입력하세요>> ')
print(f'차량번호 "{car}"는 오늘', '운행가능입니다.' if int(car[-1]) % 2 == 0 else '운행불가입니다.')
