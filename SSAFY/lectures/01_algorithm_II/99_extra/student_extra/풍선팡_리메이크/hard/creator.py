'''
문제를 만들면서 고려하지 못한 것:
최대값을 선택하고 터뜨린 부분은 0 으로 바꿔서 다시 풍선팡을 수행하면 될 줄 알았음
문제) 첫번쨰 선택에서 최대값이 겹치는 경우가 있으면 그 경우에 대한 모든 탐색이 불가능
문제2) 최대값을 선택함으로 인해 추가 기회 때 더 높아질 경우를 놓칠 수 있음
이 문제를 해결하기 위해서 모든 경우에서, 추가 기회를 얻는 경우도 한번에 상정하여 최대값을 출력하는 방식으로 변경
'''

import sys
sys.stdin = open("input.txt")

dx = [1,0,-1,0]     # 짝수는 상하좌우
dy = [0,1,0,-1]
rx = [1,-1,1,-1]    # 홀수는 대각선
ry = [1,1,-1,-1]

t = int(input())

for idx in range(t):
    n,m = map(int,input().split())

    ballons = [list(map(int,input().split())) for _ in range(n)]
    # 2차원 리스트에 대한 전역
    result = 0
    for i in range(n):
        for j in range(m):
            s = ballons[i][j]       # 터뜨릴 풍선 지정
            k = 0                   # 추가 기회 제공 시 사용될 변수
            rem = [(i, j)]
            for dt in range(4):     # 델타 탐색 시작

                # 1) 짝수 조건 분기
                if ballons[i][j] % 2 == 0:
                    di = i + dx[dt]
                    dj = j + dy[dt]
                    if 0 <= di < n and 0 <= dj < m:
                        s += ballons[di][dj]
                        rem.append((di,dj))
                    # 계산 후 추가 조건 분기
                    # 터뜨린 풍선과 합의 홀짝이 같다면
                    if ballons[i][j] % 2 == s % 2:
                        # 초기 설정 반복 (대신 rem에 담긴 이전에 터뜨린 풍선 별도 관리)
                        for x in range(n):
                            for y in range(m):
                                k = ballons[x][y]
                                if (x,y) not in rem:
                                    for dt in range(4):
                                        # 2) 짝수 조건 분기
                                        if ballons[x][y] % 2 == 0:
                                            dxi = x + dx[dt]
                                            dxj = y + dy[dt]
                                            if 0 <= dxi < n and 0 <= dxj < m and (dxi,dxj) not in rem:
                                                k += ballons[dxi][dxj]


                                        # 2) 홀수 조건 분기
                                        else:
                                            rxi = x + rx[dt]
                                            rxj = y + ry[dt]
                                            if 0 <= rxi < n and 0 <= rxj < m and (rxi,rxj) not in rem:
                                                k += ballons[rxi][rxj]
                                    # 델타 이후 계산이 완료되고, 최대값 비교
                                    output = s + k
                                    if output > result:
                                        result = output

                # 1) 홀수 조건 분기
                else :
                    ri = i + rx[dt]
                    rj = j + ry[dt]
                    if 0 <= ri < n and 0 <= rj < m:
                        s += ballons[ri][rj]
                        rem.append((ri, rj))
                    # 계산 후 추가 조건 분기
                    # 터뜨린 풍선과 합의 홀짝이 같다면
                    if ballons[i][j] % 2 == s % 2:
                        # 초기 설정 반복 (대신 rem에 담긴 이전에 터뜨린 풍선 별도 관리)
                        for x in range(n):
                            for y in range(m):
                                k = ballons[x][y]
                                if (x,y) not in rem:
                                    for dt in range(4):
                                        # 2) 짝수 조건 분기
                                        if ballons[x][y] % 2 == 0:
                                            dxi = x + dx[dt]
                                            dxj = y + dy[dt]
                                            if 0 <= dxi < n and 0 <= dxj < m and (dxi,dxj) not in rem:
                                                k += ballons[dxi][dxj]


                                        # 2) 홀수 조건 분기
                                        else:
                                            rxi = x + rx[dt]
                                            rxj = y + ry[dt]
                                            if 0 <= rxi < n and 0 <= rxj < m and (rxi,rxj) not in rem:
                                                k += ballons[rxi][rxj]
                                    # 델타 이후 계산이 완료되고, 최대값 비교
                                    output = s + k
                                    if output > result:
                                        result = output

    print(f"#{idx+1} {result}")