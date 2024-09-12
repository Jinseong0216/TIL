for t in range(1,int(input())+1):

    N, M = map(int, input().split())
    seq = list(map(int, input().split()))
    min_max = [sum(seq[:M])] * 2

    for i in range(1, N-M+1):
        min_max = [min(min_max[0], sum(seq[i:i+M])), max(min_max[1], sum(seq[i:i+M]))]

    print(f'#{t}', min_max[1]-min_max[0])