def dfs(length = 0):
    # 백 트래킹 조건
    if length == M: print(" ".join(seq)); return
    # 모든 숫자에 대해서 반복문 
    for num in range(1, N+1):
        # 이미 들고있는 숫자면 continue
        if visited[num]: continue
        # 방문 체크; 숫자 추가
        visited[num] = True; seq.append(str(num))
        # 재귀 호출
        dfs(length+1)
        # 방문 체크 해체; 숫자 삭제
        visited[num] = False; seq.pop()

if __name__ == "__main__": 
    N, M = map(int, input().split())
    # 방문 체크용
    visited = [False]*(N+1)
    # 출력 전 수열을 담을 배열
    seq = []
    # 함수 호출
    dfs()