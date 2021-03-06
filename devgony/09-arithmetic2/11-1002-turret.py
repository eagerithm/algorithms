t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    r1r2 = r1 + r2
    maxr = max(r1, r2)
    minr = min(r1, r2)
    if r1 == r2 and d == 0:
        print(-1)
        continue
    if maxr > d + minr: print(0)
    elif maxr == d + minr: print(1)
    else:
        if r1r2 > d: print(2)
        elif r1r2 == d: print(1)
        else: print(0)
"""터렛
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	136002	27832	22013	21.282%
문제
조규현과 백승환은 터렛에 근무하는 직원이다. 하지만 워낙 존재감이 없어서 인구수는 차지하지 않는다. 다음은 조규현과 백승환의 사진이다.



이석원은 조규현과 백승환에게 상대편 마린(류재명)의 위치를 계산하라는 명령을 내렸다. 조규현과 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다.

조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고, 조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때, 류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 이루어져 있다.

한 줄에 x1, y1, r1, x2, y2, r2가 주어진다. x1, y1, x2, y2는 -10,000보다 크거나 같고, 10,000보다 작거나 같은 정수이고, r1, r2는 10,000보다 작거나 같은 자연수이다.

출력
각 테스트 케이스마다 류재명이 있을 수 있는 위치의 수를 출력한다. 만약 류재명이 있을 수 있는 위치의 개수가 무한대일 경우에는 -1을 출력한다.

예제 입력 1 
3
0 0 13 40 0 37
0 0 3 0 7 4
1 1 1 1 1 5
예제 출력 1 
2
1
0"""
"""풀이
python의 경우 sqrt해도 문제가 없으나 다른 언어의 경우 부동소수점을 고려해 d**2, (r1 - r2)**2를 활용
while에서 로직 종료를 위해서는 continue
복잡한 케이스 해결을 위해 함수형태로 작성하고 assert 하자

# 1. 두 원이 일치
if r1 == r2 and d == 0: 
        print(-1)
        continue
# 2. 원 하나가 다른 원의 안쪽에 위치
    if maxr > d + minr: print(0) 
# 3. 내접
    elif maxr == d + minr: print(1)
    else:
# 4. 원이 겹침
        if r1r2 > d: print(2)
# 5. 외접
        elif r1r2 == d: print(1)
# 6. 원이 서로 떨어져있음
        else: print(0)
"""