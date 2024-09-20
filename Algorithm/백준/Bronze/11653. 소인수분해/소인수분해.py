def prime_factorization(n):
    m = n
    if m == 1: return
    for i in range(2, m+1):
        while True:
            if m%i == 0:
                print(i)
                m = m//i
            else: break
        if m == 1: break


N = int(input())
prime_factorization(N)