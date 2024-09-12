import sys
from collections import deque

sys.stdin = open('input1249.txt', 'r')

T = int(input())
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

def bfs():
    dij = [[1, 0], [0, 1]]

    que = deque([0, 0])
    distance = [[-1]*N for _ in range(N)]
    distance[0][0] = 0

    while que:
        i, j = que.popleft()
        for di, dj in dij:
            ni, nj = i+di, j+dj

            if 0 > ni or ni >= N or 0 > nj or nj >= N: continue
            if distance == -1: continue
            que.append([ni. nj])
            distance[ni][nj]
































##############################################################
# 불필요
import sys
sys.stdin = open('input.txt')
##############################################################
# N = 스위치 길이
N = int(input())
# 학생에게 부여된 번호를 기준으로 작업을 하는 것을 확인함. 혼동의 방지를 위해 switch의 정보가 idx = 1부터 시작
switch = [0] + list(map(int, input().split()))
# 학생의 수
M = int(input())


def change(sex, idx, switch):
    if sex == 1:                                           # 남자
        for i in range(1, N+1):
            if i % idx == 0:
                switch[i] = [1, 0][switch[i]]
    else:                                                     # 여자
        max_len = min(idx-1, N-idx)
        while max_len >= 0:
            if switch[idx-max_len:idx+max_len+1] == switch[idx-max_len:idx+max_len+1][::-1]:
                for j in range(idx-max_len, idx+max_len+1):
                    switch[j] = [1, 0][switch[j]]
                return
            max_len -= 1

# 함수 적용
for _ in range(M):
    sex, idx = map(int, input().split())
    change(sex, idx, switch)

# 몇줄 출력할지 정하기
print_times = (N-1)//20 + 1
# 출력하기
for idx in range(print_times):
    answer = switch[1+20*idx:1+20*idx+20]
    print(' '.join(str(info) for info in answer))