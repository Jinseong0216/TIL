# 장훈이의 높은 선반
def dfs(idx, total):
    global ans

    if total >= B: ans = min(total, ans); return; # 목표키를 넘긴경우 업데이트 후 종료
    if ans == B or idx == N-1: return # 이미 최적화된 목표키를 찾았거나 모든 경우 조회가 끝났다면 종료
    dfs(idx+1, total) # idx+1위치의 점원 키를 더하지 않는 경우
    dfs(idx+1, total+heights[idx+1]) # idx+1위치의 점원 키를 더하는 경우


for t in range(1, int(input())+1): # 테스트케이스
    N, B = map(int, input().split()) # 점원의 수N, 목표높이B
    heights = list(map(int, input().split())) # 점원의 키
    ans = float('inf') # 초기값 설정
    dfs(-1, 0) # 함수 호출
    print(f'#{t} {ans-B}')