import sys

sys.stdin = open('input.txt')
T = int(input())

for t in range(1,T+1):
    X, Y = map(int, input().split())
    print(t, '번째')
    for _ in range(X):
        print(list(map(int, input().split())))
