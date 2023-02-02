# 4강
# p.85
# 1번
num = int(input('10~99 사이의 정수를 입력하세요>> '))
print('십의 자리: ', num//10)
print('일의 자리: ', num % 10)

# 2번
time = int(input('초를 입력하세요>> '))
print(f'변환 결과는 {time//3600}시간 {time%3600//60}분 {time%3600%60}초입니다.')

# 3번
number = input('4자리 사원번호를 입력하세요>> ')
print('근무시간은 오전입니다.' if int(number[-1]) >= 5 else '근무시간은 오후입니다.')

# 4번
print('한 박스에 20개의 라면을 담을 수 있습니다.')
print('라면의 개수를 입력하시면 필요한 박스 수를 알려드립니다.')
count = int(input('라면의 개수를 입력하세요>> '))
box = count//20
print(f'{count}개 라면을 담으려면 {box+1 if count%20 >= 1 else box}박스가 필요합니다.')

# 5번
kor = float(input('국어 점수를 입력하세요>> '))
eng = float(input('영어 점수를 입력하세요>> '))
math = float(input('수학 점수를 입력하세요>> '))
sum = kor+eng+math
print(f'평균은 {sum/3}점이고, 결과는', '합격입니다.' if sum/3 >= 80 else '불합격입니다.')
