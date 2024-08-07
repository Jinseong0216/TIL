T = int(input())
for t in range(1, T+1):
    Data = input().strip()
    N = len(Data)
    stack = []

    
    ans = cnt = i = 0
    while i < N:
        if (i < N-1) and Data[i:i+2] == '()':
            M = stack.count('(')
            stack = ['(']*M
            cnt += M
            i += 2
            continue
        else:
            if Data[i] == ')':
                stack.pop()
                cnt += 1
            else:
                stack.append('(')
        i += 1
    print(f'#{t} {cnt}')
# 2
# ()(((()())(())()))(())
# (((()(()()))(())()))(()())