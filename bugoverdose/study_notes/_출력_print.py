# 복수의 인자를 받으면 공백으로 나눔 
print("A", "B", 12)
# A B 12
# ==============================================
animals = 'eels'

print(f'My hovercraft is full of {animals}.')
# My hovercraft is full of eels.

print(f'My hovercraft is full of {animals!r}.')
# My hovercraft is full of 'eels'.
# ==============================================
import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    print(f'Case #{i+1}: {A+B}')
# Case #1: 2
# Case #2: 5
# Case #3: 7
# Case #4: 17
# Case #5: 7
# ==============================================
# 문자열.format()

print('We are the {} who say "{}!"'.format('knights', 'Ni'))
# We are the knights who say "Ni!"

# ==============================================
# 소수점은 f'~{number:.2f}' 형식으로 2번째 소수점까지 표시(3번째에서 반올림)

import sys

for line in sys.stdin:
    scores = list(map(int, line.split()))
    scores.pop(0)
    scores.sort(reverse = True)
    average = sum(scores)/len(scores)
    above_average = 0
    for score in scores:
        if score > average:
            above_average += 1
        else:
            break
            
    above_average_ratio = above_average/len(scores)*100
    print(f'{above_average_ratio:.3f}%')
# ==========================
N = int(input())
nums = list(map(int, input().split()))
# 6
# -4 3 -9 0 4 1

pos = 0
neg = 0
zero = 0

for num in nums:
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        zero += 1

print(f'{pos/N:.6f}') # 0.500000
print(f'{neg/N:.6f}') # 0.333333
print(f'{zero/N:.6f}') # 0.166667
# ==============================================
# sys.stdout.write : 하나의 문자열을 인자로 받아 출력. 줄바꿈 기능 없음. 성능은 좋음.

import sys

for i in range(5):
    sys.stdout.write(str(i) + "\n")
# 1
# 2
# 3
# 4
# 5
# ==============================================