for t in range(1, int(input())+1):
    K, N, M = map(int, input().split())            
    chargers = list(map(int, input().split()))     
    cnt = 0

    if max(chargers[i+1] - chargers[i] for i in range(len(chargers)-1)) > K: 
        print(f'#{t}', cnt)
    
    else:
        i = 0                                               
        while i < N + 1:
            if i+K >= N: break
            else:
                i = max(charger for charger in chargers if i+K >= charger)
                cnt += 1
        print(f'#{t}', cnt)