import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 무게, 적재량 오름차순 정렬
    W = sorted(list(map(int, input().split())))
    T = sorted(list(map(int, input().split())))

    result = 0
    # 트럭, 화물 둘 다 하나 이상 있다면,
    while W and T:
        # 가장 큰 트럭이 가장 큰 화물을 감당 할 수 있다면
        if T[-1] >= W[-1]:
            # 트럭과 화물을 빼서 무게에 추가하고
            T.pop()
            result += W.pop()
        else:
            W.pop()     # 제일 큰 트럭에 못 싣는다면 화물 버림.
    print(f'#{tc} {result}')