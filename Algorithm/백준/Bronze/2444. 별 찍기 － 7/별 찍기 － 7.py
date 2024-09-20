N = int(input())
for i in range(2*N-1):
    if i >= N: i = 2*N-2-i
    line = ' '*abs(i-N+1) + '*'*abs(i) + '*' + '*'*abs(i)
    print(line)
