import sys
sys.stdin = open('input.txt')

def binary_search(start, end, target):
    global result

    now = 'middle'      # 최초 탐색시 방향 상관 없음.
    while True:
        mid = (start + end) // 2    # 중앙 값 계산 후,
        if target == A[mid]:        # 타겟이 중앙값이라면
            result += 1             # 조사 성공.
            return
        elif target > A[mid]:       # 타겟이 중앙값보다 크다면
            # 이전에도 오른쪽에서 왔는데, 또 오른쪽으로 조사하러 가야한다면 실패.
            if now == 'right': return   
            now = 'right'           # 오른쪽으로 이동 체크
            start = mid+1           # 탐색 시작지점 초기화
        # 반대의 경우
        elif target < A[mid]:   
            if now == 'left': return
            now = 'left'
            end = mid - 1           # 탐색 종료지점 초기화


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # A 리스트 정렬
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    result = 0  # 탐색 조건을 만족하는 경우
    for target in B:
        binary_search(0, N-1, target)
    print(f'#{tc} {result}')