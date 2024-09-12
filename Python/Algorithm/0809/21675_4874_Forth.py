# x,y를 뽑는 순서 반대로 했어야함..
# 그걸 못해서 y / x가 되서 에러 났던 것
T = int(input())
for t in range(1,T+1):
    eqn = input().split()
    ans, N, stack = 1, len(eqn), []
    for i in range(N-1):        
        if eqn[i].isdecimal(): stack.append(eqn[i])        
        elif eqn[i] == '.': ans = 0
        elif len(stack) < 2: ans = 0
        else:
            y = int(stack.pop())
            x = int(stack.pop())
            if eqn[i] == '+': stack.append(str(x+y))
            elif eqn[i] == '-': stack.append(str(x-y))
            elif eqn[i] == '*': stack.append(str(x*y))
            elif eqn[i] == '/': stack.append(str(x//y))
            else: ans = 0
    if len(stack) != 1: print(f'#{t} error')
    elif not ans: print(f'#{t} error')
    else: print(f'#{t} {stack.pop()}')