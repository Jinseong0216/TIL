# 1. 문제를 제대로 읽자
#    - 여자의 경우, idx를 중심으로 찾아서 바꾸는걸 몰랐음
# 2. 인덱스를 신경쓰자... +1 안해서 인덱스를 안맞췄다
# 3. 케이스 다 되는지 확인해보고 가자... while max_len >= 0 이어야 하는데 , while max_len > 0 했었다

import sys
sys.stdin = open('input.txt')

N = int(input())
switch = [0] + list(map(int, input().split()))
M = int(input())

def change(sex, idx, switch):
    if sex == 1:
        for i in range(1, N+1):
            if i % idx == 0:
                switch[i] = [1, 0][switch[i]]
    else:
        max_len = min(idx-1, N-idx)
        while max_len >= 0:
            if switch[idx-max_len:idx+max_len+1] == switch[idx-max_len:idx+max_len+1][::-1]:
                for j in range(idx-max_len, idx+max_len+1):
                    switch[j] = [1, 0][switch[j]]
                return
            max_len -= 1

for _ in range(M):
    sex, idx = map(int, input().split())
    change(sex, idx, switch)

if N % 20 == 0:
    print_times = N//20
else:
    print_times = (N//20) + 1

for idx in range(print_times):
    answer = switch[1+20*idx:1+20*idx+20]
    ans = ' '.join(str(info) for info in answer)
    print(ans)
