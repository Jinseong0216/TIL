def comparision(base,exp,case = 10000, comment = None):
    
    import time
    
    def main(base,exp):
        if exp == 0: return 1
        else: return base * main(base, exp - 1)

    if comment: print(comment)
    
    sec_sum = 0
    
    for i in range(case):
        start = time.time()
        base**exp
        end = time.time()
        sec_sum += float(end - start)

    print(str(int(case)) + '-' + 'times' + ' of base ' + str(base) + ' and exp ' + str(exp))  
    print("Brutal force:",sec_sum)
    
    sec_sum = 0
    for i in range(case):
        start = time.time()
        main(base,exp)
        end = time.time()
        sec_sum += float(end - start)
    
    print("Recursion:",sec_sum)



#======================================================
base = 70379 #prime
exp = 809 # prime
comment = 'base and exp are all primes'
cases_list = [int(1E4),int(1E3)]

print('1번째 test:','='*35)

for case in cases_list:
    comparision(base,exp, case, comment)



#======================================================
base = 70378 # not prime
exp = 809 # prime
comment = 'base in not a prime, exp is a prime'
cases_list = [int(1E4),int(1E3)]

print('2번째 test:','='*35)

for case in cases_list:
    comparision(base,exp, case, comment)



#======================================================
base = 70379 # prime
exp = 788 # not prime
comment = 'base is a prime, exp is not a prime'
cases_list = [int(1E4),int(1E3)]

print('3번째 test:','='*35)

for case in cases_list:
    comparision(base,exp, case, comment)




#======================================================
base = 70378 # not prime
exp = 788 # not aprime
comment = 'base and exp are not primes'
cases_list = [int(1E4),int(1E3)]

print('4번째 test:','='*35)

for case in cases_list:
    comparision(base,exp, case, comment)


"""
| type | prime, prime | not prime, prime | prime, not prime | not prime, not prime |
| --- | --- | --- | --- |--- |
| brutal | 0.167 | 0.154 | 0.145 | 0.16 |
| recursion | 2.00 | 1.98 | 1.88 | 1.89 |
"""