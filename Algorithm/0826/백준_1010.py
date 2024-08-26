# 다리놓기
def factorial(n):
    if n==0 or n==1: return 1
    return n*factorial(n-1)

def combinations(n, r):
    ans = factorial(n)/(factorial(n-r)*factorial(r))
    return int(ans)

for _ in range(int(input())):
    N, M = map(int, input().split())
    print(combinations(M, N))

