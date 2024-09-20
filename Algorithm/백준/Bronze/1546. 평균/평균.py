N = int(input())
scores = list(map(int, input().split()))
M = float('-inf')
total_sum = 0
for score in scores:
    total_sum += score
    if M < score: M = score

ans = (total_sum/(N*M))*100
print(ans)