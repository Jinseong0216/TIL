

N = int(input())
A = []
B = []

for _ in range(N):
    box = input().split()
    A.append(int(''.join([str(box.count(str(x))) for x in range(4,0,-1)])))


for _ in range(N):
    box = input().split()
    B.append(int(''.join([str(box.count(str(x))) for x in range(4,0,-1)])))

for i in range(N):
    if A[i] - B[i] > 0: print('A')
    elif A[i] - B[i] == 0: print('D')
    else: print('B')