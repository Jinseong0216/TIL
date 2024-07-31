import sys

sys.stdin = open('input9367.txt')

T = int(input())
for t in range(1, 1+T):
    N = int(input())
    seq = list(map(int, input().split()))

    max_length = 0
    now_length = 1
    for i in range(N-1):
        if seq[i] >= seq[i+1]:
            max_length = max(max_length, now_length)
            now_length = 1
        else:
            now_length += 1
    max_length = max(max_length, now_length)

    print(f'#{t}', max_length)