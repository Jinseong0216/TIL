# 문제가 조금 이상한듯.. 
# (N - R*C)가 아니라 |N -R*C|여야 하는 것 같음..
for t in range(int(input())):
    N, A, B = map(int, input().split())
    R, C, m = N, 1, B*N
    while R >= C:
        for C in range(min(R,N//R) + 1):
            m = min(A*(R-C)+B*(N-R*C), m)
        R -= 1

    print(f'#{t+1} {m}')
