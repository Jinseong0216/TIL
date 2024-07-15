# 3809
# 문제에 제시된 입력방식 잘못됨

T = int(input())

for t in range(1,T+1):

    N = int(input())
    sequence = []
    M = 0
    while M < N:
        line = input().split()
        M += len(line) 
        sequence += line

    ans_set = set()
    s = 0
    for i in range(1, N+1):
        for j in range(N + 1 - i):
            s = sequence[j:j+i]
            s = ''.join(s)
            ans_set.add(int(s))
            
            if len(ans_set) == 10**i: continue

        if len(ans_set) < 10**i:
            nums = set(range(10**i))
            ans = min(nums - ans_set)
            print(f'#{t}',str(ans))
            break
