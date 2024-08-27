N = int(input())
seq = list(map(int, input().split()))
m = M = seq[0]

for s in seq:
    if m > s: m = s
    if M < s: M = s
print(m, M)