N = int(input())
seq = input().split()
target = input().strip()

cnt = 0
for idx in range(N):
    if seq[idx] == target: cnt += 1

print(cnt)
