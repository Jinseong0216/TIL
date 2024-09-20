import sys
sys.stdin = open('input.txt')

def search(n, acc):
    global result
    if acc > result:    # 누적값이 결괏값보다 크다면 return
        return
    if n >= 12:     # 1년에 대해 모두 조회했다면
        if acc < result:    # 최솟값 초기화
            result = acc
    else:
        if schedule[n]:     # 스케쥴이 있다면,
            search(n + 1, acc + schedule[n] * data[0])    # 일로 계산
            search(n + 1, acc + data[1])                # 월로 계산
            search(n + 3, acc + data[2])                # 3달치 한 번에 계산
        else:               # 없다면,
            search(n + 1, acc)  # 그냥 달만 증가


T = int(input())

for tc in range(1, T+1):
    # 하루, 한달, 세달, 1년
    data = list(map(int, input().split()))
    schedule = list(map(int, input().split()))
    result = data[3]  # 충분히 큰 값.
    search(0, 0)
    print(f'#{tc} {result}')
