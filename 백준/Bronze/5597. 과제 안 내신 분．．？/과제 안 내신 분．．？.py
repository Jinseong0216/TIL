S = set(range(1, 31))
std_num = [int(input().strip()) for _ in range(28)]
ans = [s for s in S if s not in std_num]
print(ans[0])
print(ans[1])