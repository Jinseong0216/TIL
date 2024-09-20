import sys
sys.stdin = open('input.txt')

def chance(x, y, data):
    new_arr = [list(arr) for arr in data]
    check = False
    tmp = new_arr[x][y]
    if new_arr[x][y] % 2:
        check = True
        tmp += bonus(x, y, [[-1, -1], [-1, 1], [1, -1], [1, 1]], new_arr)
    else:
        tmp += bonus(x, y, [[-1, 0], [1, 0], [0, -1], [0, 1]], new_arr)
    new_arr[x][y] = 0
    return check, tmp, new_arr

def bonus(x, y, direction, arr):
    count = 0
    for dx, dy in direction:

        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M:
            count += arr[nx][ny]
            arr[nx][ny] = 0
    return count

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for x in range(N):
        for y in range(M):
            check, tmp, new_arr = chance(x, y, data)
            if check == (tmp % 2):
                for i in range(N):
                    for j in range(N):
                        check, tmp2, new_arr2 = chance(i, j, new_arr)
                        tmp2 += tmp
                        if result < tmp2:
                            result = tmp2
            else:
                if result < tmp:
                    result = tmp


    print(f'#{tc} {result}')
