import sys
sys.stdin = open('input.txt')


N = int(input())
pos = {}
for i in range(N):
    a, b, w, h = list(map(int, input().split()))
    for x in range(a, a+w):
        for y in range(b, b+h):
            if pos.get((x, y)) != None:
                pos[pos[(x, y)]] -= 1
            pos[(x, y)] = i
            pos[i] = pos.get(i, 0) + 1

for i in range(N):
    print(pos[i])
