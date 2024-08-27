N, X = map(int, input().split())
seq = list(map(int, input().split()))

for s in seq:
    if s < X: print(s, end=' ')
print()