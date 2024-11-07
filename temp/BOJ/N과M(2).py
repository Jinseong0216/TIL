'''
#TODO: 단계별로 풀어보기(백트래킹) - N과 M (2)

#? Strategy: dfs사용시 그냥 조회하는 순서가 바로 요구한 것임
#? 왜 백트래킹에 있는지는 모르겠으나.. length==M인 부분이 백트래킹인듯
'''

def dfs(length = 0):
    # 백 트래킹 조건
    if length == M: print(" ".join(seq)); return
    # 현 위치
    current = 0 if seq == [] else int(seq[-1])
    # 다음 위치부터 마지막까지 반복문
    for num in range(current+1, N+1):
        if visited[num]: continue
        # 방문 체크; 숫자 추가
        visited[num] = True; seq.append(str(num))
        # 재귀 호출
        dfs(length+1)
        # 방문 체크 해제; 숫자 삭제
        visited[num] = False; seq.pop()

if __name__ == "__main__":
    N, M = map(int, input().split())
    # 방문 체크용
    visited = [False]*(N+1)
    # 출력 전 수열을 담을 배열
    seq = []
    # 함수 호출
    dfs()