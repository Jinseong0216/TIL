# 20551. 증가하는 사탕 수열
T = int(input()) # 문제 수
for t in range(1, T+1):
    arr = list(map(int, input().split())) # 입력받은 사탕의 수
    ans = 0 # 먹어야 할 사탕의 수
    for idx in range(len(arr)-1, 0, -1): # 마지막 사탕부터 역순으로 조회
        if arr[idx] == 1: # 조건을 만족시킬 수 없는 경우임!
            ans = -1; break;
        temp = arr[idx-1] # 사탕의 수 임시 저장
        arr[idx-1] = min(arr[idx]-1, arr[idx-1]) # 앞의 사탕이 더 많다면 -1 차이가 나도록
        ans += (temp-arr[idx-1]) # 먹은 사탕의 수 업데이트

    print(f'#{t} {ans}')