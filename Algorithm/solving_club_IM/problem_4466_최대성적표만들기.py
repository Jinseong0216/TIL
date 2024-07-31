# Built-in function sort 사용
# T = int(input())
# for t in range(1, T+1):
#     N, K = map(int, input().split())
#     scores = list(map(int, input().split()))
#     scores.sort()
#
#     print(f'#{t}', sum(scores[-i] for i in range(1, K+1)))


# 버블 정렬 활용
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))

    s = 0
    for i in range(N-1, N-K-1, -1):
        for j in range(i):
            if scores[j] > scores[j+1]:
                scores[j], scores[j+1] = scores[j+1], scores[j]
        s += scores[i]
    print(f'#{t}', s)
