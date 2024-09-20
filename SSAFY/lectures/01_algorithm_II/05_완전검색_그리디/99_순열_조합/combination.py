'''
import itertools

arr = [1, 2, 3]
r = 2
print(list(itertools.combinations(arr, r)))
'''

def combine(start, current, r):
    if r == 0:
        result.append(current[:])
        return
    
    for i in range(start, len(arr)):
        current.append(arr[i])
        combine(i + 1, current, r - 1)
        current.pop()

result = []
arr = [1, 1, 3]
combine(0, [], 3)

print(result)
