# 멘토씨리즈파이썬
# p.180_1
number = input('전화번호를 입력하세요>> ')
print(number.split('-')[1])

# p.180_2
while True:
    number = input('사업자등록번호를 입력하세요(예:123-45-67890)>> ')
    place = number.split('-')
    if len(place[0]) == 3 and len(place[1]) == 2 and len(place[2]) == 5:
        if place[0].isdecimal() and place[1].isdecimal() and place[2].isdecimal() == True:
            print('올바른 형식입니다.')
            break
        else:
            print('숫자 외에 입력하실 수 없습니다!')
            continue
        break
    else:
        print('올바른 형식이 아닙니다!')

# p.181_3
manage = '"김철수",85'
name = manage.split(",")[0].strip('"')
score = manage.split(",")[1]
print(f"이름은 {name}이고, 점수는 {score}점입니다.")