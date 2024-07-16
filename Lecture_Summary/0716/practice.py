T = int(input())

for t in range(1,T+1):
    c = 1
    cards = input().strip()
    N = len(cards)// 3
    cards_range = set(range(1,14))
    dict = {'S': cards_range, 'D': cards_range, 'H': cards_range, 'C': cards_range}

    for i in range(N): 
        card_and_num = cards[i*3 : i*3 + 3]
        card = card_and_num[0]
        num = int(card_and_num[1:3])

        c1 = len(dict[card])
        dict[card] = dict[card] - set([num])
        c2 = len(dict[card])

        if c1 == c2: 
            print(f'#{t} ERROR')
            c = 0
    if c: print(f'#{t}', len(dict['S']), len(dict['D']), len(dict['H']), len(dict['C']))
