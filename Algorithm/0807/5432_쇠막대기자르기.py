T = int(input())
for t in range(1, T+1):
    Data = input().strip()
    N = len(Data)
    
    ans = cnt = i = 0
    while i < N:
        if (i < N-1) and Data[i:i+2] == '()':
            ans, i = ans+cnt, i+2
            continue
        else:
            if Data[i] == ')':
                ans = ans + 1
                cnt = cnt - 1
            else:
                cnt = cnt + 1
            i += 1
    print(f'#{t} {ans}')