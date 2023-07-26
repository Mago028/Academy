# 멘토씨리즈파이썬
# p.160_1

for num, rainbow in enumerate(['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']):
    print(f'무지개의 {num+1}번째 색은 {rainbow}입니다.')

# p.160_2
print('점수를 입력하세요. 더 이상 입력할 점수가 없으면 음수를 아무거나 입력하세요.')
score = []
while True:
    s = int(input('점수 입력>> '))
    score.append(s)
    if s <= 0:
        score.pop()
    if s >= 0:
        continue
    else:
        print(f'평균={sum(score) / len(score)}, 최대={max(score)}, 최소={min(score)}')
        break