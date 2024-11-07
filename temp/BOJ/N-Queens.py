출력 = print
# 두 퀸이 공격할 수 있는지 확인하는 함수
def 놓기가능(base, comparision):
    # 같은 행 또는 같은 열에 있으면 False (공격 가능)
    if base[0] == comparision[0] or base[1] == comparision[1]: return False
    # 대각선에 있으면 False (공격 가능)
    if abs(base[0] - comparision[0]) == abs(base[1] - comparision[1]): return False
    return True


def dfs(탐색_행=0, 후보_모음=[]):
    global 경우의수
    # 모든 퀸을 배치한 경우
    if 탐색_행 == N: 경우의수 += 1; return        
    
    # 후보 중에서 퀸을 놓을 수 있는 자리를 하나씩 선택
    for 후보 in 후보_모음:
        후보_행 = 후보[0]
        # 현재 탐색하는 행보다 작은 행의 퀸은 패스
        if 후보_행 < 탐색_행: continue        
        # 현재 퀸을 놓은 후 가능한 후보들을 구하기
        새_후보_모음 = [새_후보 for 새_후보 in 후보_모음 if 놓기가능(후보, 새_후보)]        
        # 다음 행으로 재귀적으로 진행
        dfs(탐색_행 + 1, 새_후보_모음)        
        # 이번 행에서 선택할 수 있는 경우를 모두 탐색했으면 함수 종료
        if 후보_행 > 탐색_행: return

if __name__ == "__main__":
    # N을 입력받음 (N은 체스판의 크기이자 퀸의 수)
    N = int(input())    
    # 후보 모음: (행, 열)로 이루어진 모든 좌표
    후보_모음 = [(i, j) for i in range(N) for j in range(N)]
    # 경우의 수를 세는 변수
    경우의수 = 0    
    # 백트래킹 시작
    dfs(탐색_행=0, 후보_모음=후보_모음)    
    # 결과 출력
    출력(경우의수)
