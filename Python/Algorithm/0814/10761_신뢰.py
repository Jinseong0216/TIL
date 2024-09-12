def move_to(start, end):
    return (end - start) and (end-start)//abs(end-start)

T = int(input())

for t in range(1, 1+T):
    info = input().split()
    N, buttons, idx = int(info[0]), {'B': [], 'O': []}, {'B': 1, 'O': 1}
    for i in range(N):
        buttons[info[2*i+1]] = buttons[info[2*i+1]] + [int(info[2*i+2])]
    i = time = cnt = 0
    while cnt < N:
        now, other = 'B', 'O'
        if info[2*i+1] == 'O': now, other = 'O', 'B'

        while idx[now] != buttons[now][0]:
            idx[now] += move_to(idx[now], buttons[now][0])
            if buttons[other]: idx[other] += move_to(idx[other], buttons[other][0])
            time = time+1

        buttons[now].pop(0)
        if buttons[other]: idx[other] += move_to(idx[other], buttons[other][0])
        time, cnt, i = time+1, cnt+1, i+1

    print(f'#{t} {time}')

