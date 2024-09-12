for t in range(1, int(input()) + 1):
    dummy_num = input()
    cards = input()
    cards_freq = [ (cards.count(str(n)), n) for n in range(10) ]
    cards_freq.sort()
    
    print(f'#{t}', cards_freq[-1][1], cards_freq[-1][0])