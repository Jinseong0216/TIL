'''
#TODO: 단계별로 풀어보기(백트래킹) - N과 M (3)

#? Strategy: dfs사용시 그냥 조회하는 순서가 바로 요구한 것임
#? 왜 백트래킹에 있는지는 모르겠으나.. length==M인 부분이 백트래킹인듯
#? 그.. 심지어 visited를 쓰지 않아도 되는 dfs를 사용하면 되는 문제
'''

def dfs(length = 0):
    # 백 트래킹 조건
    if length == M: print(" ".join(seq)); return
    # 모든 숫자에 대해서 반복문
    for num in range(1, N+1):
        # 숫자 추가
        seq.append(str(num))
        # 재귀 호출
        dfs(length+1)
        # 숫자 삭제
        seq.pop()

if __name__ == "__main__":
    N, M = map(int, input().split())
    # 출력 전 수열을 담을 배열
    seq = []
    # 함수 호출
    dfs()
 