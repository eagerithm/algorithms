# 가장 긴 바이토닉 부분 수열 (https://www.acmicpc.net/problem/11054)
# 수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.
# 예를 들어, {10, 20, 30, 25, 20}과 {10, 20, 30, 40}, {50, 40, 25, 10} 은 바이토닉 수열이지만,  {1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 은 바이토닉 수열이 아니다.
# 수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.

N = int(input())
seq = list(map(int, input().split()))

max_count = 0

for mid_idx in range(N):
    biggest = seq[mid_idx]

    dp_asc = [0]
    for left in range(mid_idx):
        cur = seq[left]
        if cur >= biggest: continue
        if dp_asc[-1] < cur:
            dp_asc.append(cur)
        else:
            for idx in range(2, len(dp_asc)+1):
                if dp_asc[-idx] < cur:
                    dp_asc[-idx+1] = cur
                    break
        
    dp_desc = [biggest]
    for right in range(mid_idx+1, N):
        cur = seq[right]
        if cur >= biggest: continue
        if dp_desc[-1] > cur:
            dp_desc.append(cur)
        else:
            for idx in range(2, len(dp_desc)+1):
                if dp_desc[-idx] > cur:
                    dp_desc[-idx+1] = cur
                    break
    max_count = max(max_count, len(dp_asc)-1 + len(dp_desc))

print(max_count)

#  =================================================================