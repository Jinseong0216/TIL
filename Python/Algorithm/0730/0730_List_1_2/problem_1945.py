for t in range(1, int(input())+1):
    N = int(input())

    primes = [2, 3, 5, 7, 11]    
    cnt_global = []
    for prime in primes:
        cnt = 0
        while True:
            if N % prime == 0:
                N //= prime
                cnt += 1
            else:
                cnt_global += [cnt]
                break
    print(f'#{t}', *cnt_global)