T = int(input())
for t in range(1,T+1):
    eqn = input().split()[::-1][1:]
    ans, N, stack = 1, len(eqn), []
    while eqn:
        p = eqn.pop()
        if p.isdecimal(): stack.append(p)        
        elif len(stack) < 2: ans = 0
        else:
            x = int(stack.pop())
            y = int(stack.pop())
            if p == '+': stack.append(str(x+y))
            elif p == '-': stack.append(str(x-y))
            elif p == '*': stack.append(str(x*y))
            elif p == '/': stack.append(str(x//y))
            else: ans = 0
    if len(stack) != 1: print(f'#{t} error')
    else: print(f'#{t} {stack.pop()}')
