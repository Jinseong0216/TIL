import sys
sys.stdin = open('input.txt')

def search():
    # 초기화: 13개월로 하는 이유는 3달 이용권을 적용할 때 범위를 벗어나지 않게 하기 위함
    dp = [float('inf')] * 13
    dp[0] = 0

    for i in range(1, 13):
        # 1일 이용권으로 이용하는 경우
        dp[i] = min(dp[i], dp[i - 1] + data[0] * schedule[i - 1])
        # 1달 이용권으로 이용하는 경우
        dp[i] = min(dp[i], dp[i - 1] + data[1])
        # 3달 이용권으로 이용하는 경우 (범위를 벗어나지 않도록)
        if i >= 3:
            dp[i] = min(dp[i], dp[i - 3] + data[2])
        else:
            dp[i] = min(dp[i], data[2])  # 시작 달에서 3달 이용권을 사용할 경우

    # 1년 이용권과 비교하여 최종 최소 비용 결정
    return min(dp[12], data[3])

T = int(input())
for tc in range(1, T+1):
    data = list(map(int, input().split()))
    schedule = list(map(int, input().split()))
    result = search()
    print(f'#{tc} {result}')
