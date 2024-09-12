for t in range(1, 11):
    N, eqn = int(input()), list(input())
    ans, stack = [], []
    for x in eqn:
        if x.isdecimal(): ans.append(x)
        else:
            if x == '+':
                while stack: ans.append(stack.pop()) 
                stack.append(x)
            else:
                if '*' in stack: ans.append(x)
                else: stack.append(x)
    while stack: ans.append(stack.pop())

    stack = []
    for chr in ans:
        if chr.isdecimal(): stack.append(chr)
        elif chr == '+':
            x = int(stack.pop()) + int(stack.pop())
            stack.append(str(x))
        elif chr == '*':
            x = int(stack.pop()) * int(stack.pop())
            stack.append(str(x))
    print(f'#{t} {stack.pop}')