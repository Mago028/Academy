# 3강
# p.66
# 1번
num1 = float(input('첫 번째 실수를 입력하시오>> '))
num2 = float(input('두 번째 실수를 입력하시오>> '))
print(f'{num1}와 {num2}의 합은 {num1+num2}입니다.')

# 2번
month = int(input('1~12 사이의 월을 입력하시오>> '))
day = [31, 28, 31, 30, 31,30, 31, 31, 30, 31, 30, 31]
print(f'{month}월은 {day[month-1]}일까지 있습니다.')
