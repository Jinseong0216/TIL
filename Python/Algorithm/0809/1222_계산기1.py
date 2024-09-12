for t in range(1, 11):
    N = int(input())
    eqn = list(input())
    ans, stack, dic = [], [], {'+': 0, '-': 0, '*': 1, '/': 1}
    for x in eqn:
        if x.isdecimal(): ans.append(x)
        else:
            if x == '+' or x == '-':
                while stack: ans.append(stack.pop())
            else:
                while stack:
                    y = stack.pop()
                    if dic[y]: 
                        ans.append(y)
                    else:
                        stack.append(y)
                        break 
            stack.append(x)
    while stack: ans.append(stack.pop())
    eqn = ans
    N = len(eqn)
    ans, stack = 1, []
    for i in range(N):        
        if eqn[i].isdecimal(): stack.append(eqn[i])        
        else:
            y = int(stack.pop())
            x = int(stack.pop())
            if eqn[i] == '+': stack.append(str(x+y))
            elif eqn[i] == '-': stack.append(str(x-y))
            elif eqn[i] == '*': stack.append(str(x*y))
            elif eqn[i] == '/': stack.append(str(x//y))
    print(f'#{t} {stack.pop()}')



