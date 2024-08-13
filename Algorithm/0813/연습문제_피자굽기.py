from collections import deque

TC = int(input())
for T in range(1, 1 + TC):
    N, M = map(int, input().split())
    pizzas = list(enumerate(map(int, input().split())))
    ans = deque(pizzas[:N])
    pizzas = deque(pizzas[N:])
    result = []
    while ans:
        pizza = ans.popleft()
        if pizza[1] < 2:
            result.append(pizza[0])
            if pizzas: ans.append(pizzas.popleft())
        else:
            ans.append((pizza[0], pizza[1]//2))
    num = result[-1]
    print(f'#{T} {num + 1}')
