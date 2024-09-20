import sys
sys.stdin = open('input.txt')


def cal(arr, now, dir):
    '''
        dir에 적힌 값이 -1 이라면, 왼쪽
        dir에 적힌 값이 +1 이라면, 오른쪽
        while arr[now]의 값이 존재할때까지 (보석이 있을때 까지)
    '''
    position = now + dir
    while 0 <= position < N:
        if arr[position]:   # 보석이 있다면
            return position
        position += dir
    # 보석이 내 조사 방향으로 없을때는 return None
    return None


def search(start):
    '''
        start -> 내가 조사를 시작할 지점이고,
        해당 지점에서부터 좌우의 보석중 가까운것을 0으로 변경할 예정
        원본 data를 수정하게 되면,
        start -> 0~ N까지 모든 상황에 대해서 조사를 해야하는데.
        그래서... 복제본을 만들어서 쓰자.
    '''
    gems = arr[:]
    now = start
    # while 옆에 종료조건 뭐라고 잡을지 조건 잡기 애매하면
    while True:
        # 할일 작성
        # 현재 위치에서 좌 우 중에 가장 가까운 보석을 찾기.
        # 좌, 우 로 이동한다는건? 어떤 특정방향으로 내가 원하는 값을 찾을떄까지 반복
        left_gem_idx = cal(gems, now, -1)
        right_gem_idx = cal(gems, now, 1)

        # 둘다 None이다 -> 왼쪽, 오른쪽 둘다 보석이 없다.
        # 모든 위치에 대한 보석을 다 0으로 처리해서 이제 더이상 작업할 이유가 없다.
        if left_gem_idx is None and right_gem_idx is None:
            return True     # 이번 start번째에서 출발하면 도중에 실패하지 않고 완료.

        # 양쪽 거리 계산
        # 왼쪽 잼이 있는 경우에만 거리가 계산
        if left_gem_idx is not None:
            left_dist = now - left_gem_idx
        else:   # 왼쪽에 잼이 없으면 어뜩함?
            # 왼쪽에 보석이 없는데 왼쪽으로 가는 상황을 안만들기 위해서
            left_dist = N*M     # 충분히 큰 값

        if right_gem_idx is not None:
            right_dist = right_gem_idx - now
        else:
            right_dist = N*M

        # 만약 양쪽의 거리가 같다.
        if left_dist == right_dist:
            return False        # 욕심 폭발

        if left_dist < right_dist:
            now = left_gem_idx
        else:
            now = right_gem_idx

        gems[now] = 0


T = int(input())
for tc in range(1, T + 1):
    # 칸의 수와 기준 칸
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.insert(0, 0)
    N += 1
    result = N + 1  # 충분히 큰 수
    # 모든 칸에 대해서 전수 조사
    for i in range(1, N):
        # 조사를 할건데 조사 결과가 True인 경우에 대해서만
        if search(i):
            # 최솟값 갱신
            if result >= abs(M - i):
                result = abs(M - i)

    print(f'#{tc} {result}')


