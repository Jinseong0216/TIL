def main(N):
    nums = [0, 1, 3, 5]
    M = N // 10

    if M < 4: 
        return nums[M]
    else: 
        return main(N-30)*2 + main(N-20)*3

T = int(input())    
for t in range(1, T+1):
    N = int(input())
    ans = main(N)
    print(f'#{t} {ans}')

# def main(N):
#     nums = [0, 1, 3, 5]
#     if N < 40: return [0, 1, 3, 5][N//10]
#     else: return main(N-30)*2 + main(N-20)*3
     
# for t in range(int(input())): print(f'#{t+1} {main(int(input()))}')