# 약수
N = int(input())
divisors = list(map(int, input().split()))
ans = min(divisors)*max(divisors)
print(ans)