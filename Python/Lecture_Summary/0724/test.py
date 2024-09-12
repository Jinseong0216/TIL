N = int(input())

dic = dict()
for _ in range(N):
    x,y = map(int,input().split())
    dic[x] = dic.get(x, []) + [y]

for i in sorted(dic.keys()):
    for j in sorted(dic[i]):
        print(i, j)
