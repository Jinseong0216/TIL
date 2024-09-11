N = int(input())

ans = 0
cnt = N//5
while cnt >= 0:
    if (N - 5*cnt)%3 == 0: ans = cnt + ((N-5*cnt)//3); break
    cnt -= 1
    
if cnt == -1: print(-1)
else: print(ans)