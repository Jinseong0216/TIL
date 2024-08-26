# 퍼펙트 셔플
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(input().split())

    chop_1 = cards[:N%2 + N//2]
    chop_2 = cards[N%2 + N//2:]
    shuffle = []
    for idx in range((N+1)//2):
        shuffle = shuffle + chop_1[idx:idx+1] + chop_2[idx:idx+1]

    print(" ".join(shuffle))
