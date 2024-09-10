N, L = int(input()), []

for k in range(N):
    a,b,c,d = map(int,input().split())
    L += [set((a+i,b+j) for i in range(c) for j in range(d))]
    for t in range(k):
        L[t] = L[t] - L[k]

for k in range(N): print(len(L[k]))