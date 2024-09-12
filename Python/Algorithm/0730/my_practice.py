for t in range(1, 11):
    cnt = int(input())
    seq = list(map(int, input().split()))

    while cnt != 0:
        max_height, min = max(seq)
        max_index = seq.index(max_height)