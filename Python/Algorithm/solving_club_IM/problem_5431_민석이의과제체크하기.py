T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    students = list(map(int, input().split()))
    ans = []
    for i in range(1, N+1):
        if i not in students:
            ans.append(i)
    ans.sort()
    print(f'#{t}', *ans)