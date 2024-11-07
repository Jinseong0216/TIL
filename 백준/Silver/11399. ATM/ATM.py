N = int(input())
arr = sorted(map(int, input().split()))
ans = sum((N-order)*(arr[order]) for order in range(N))
print(ans)