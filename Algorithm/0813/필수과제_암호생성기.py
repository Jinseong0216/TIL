for _ in range(1, 11):
    tc = input()
    numbers = list(map(int, input().split()))
    idx = cycle = 0

    while True:
        num = numbers[idx] - (cycle+1)
        numbers[idx] = num
        idx, cycle = (idx+1) % 8, (cycle+1) % 5
        if num <= 0:
            numbers[idx-1] = 0
            numbers = list(map(str, numbers[idx:] + numbers[:idx]))
            print(f'#{tc}', *numbers)
            break
