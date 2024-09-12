# 통계학
import sys
input = sys.stdin.readline  # 병신같은 이 조건 없으면 바로 에러남

N = int(input())
M = (N+1)//2
data = [0]*(8001)
for _ in range(N): data[4000+int(input().strip())] += 1

Max_value = float('-inf')
min_value = float('inf')
Intermediate_value = total_sum = cum_cnt = 0
max_appearance, max_appearance_list = 0, []
for idx in range(8001):
    cnt = data[idx]
    if cnt != 0:
        num = idx-4000
        if Max_value < num: Max_value = num # 최댓값
        if min_value > num: min_value = num # 최솟값
        if M - cnt <= cum_cnt < M: Intermediate_value = num  # 중간값
        if max_appearance == cnt: max_appearance_list.append(num)
        elif max_appearance < cnt:
            max_appearance, max_appearance_list = cnt, [num]
        total_sum += cnt*num
        cum_cnt += cnt

print(round(total_sum/N))
print(Intermediate_value)
if len(max_appearance_list) == 1: print(max_appearance_list[0])
else: print(max_appearance_list[1])
print(Max_value-min_value)





