for t in range(1, 1+int(input())):
    N = input()
    seq = input()
    cnt = 0
    while seq.count('1'*cnt): cnt += 1
    print(f'#{t}', cnt-1)