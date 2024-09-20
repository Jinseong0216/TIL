'''
import itertools

arr = [1, 1, 2]
print(list(set(itertools.permutations(arr))))
'''
import itertools

arr = [1, 1, 2]
print(list(set(itertools.permutations(arr))))

def permute(acc, arr):
    if len(arr) == 0:
        result.append(acc)
        return
    
    for i in range(len(arr)):
        # 중복인 경우, 스킵
        if i > 0 and arr[i] == arr[i - 1] and not visited[i - 1]: continue
        
        next_element = arr[i]
        arr[i], arr[-1] = arr[-1], arr[i]
        visited[i] = True
        permute(acc + [next_element], arr[:-1])
        visited[i] = False
        arr[i], arr[-1] = arr[-1], arr[i]

arr = [1, 1, 2]
result = []
arr.sort()  
visited = [False] * len(arr)
permute([], arr)

# Example usage
print(result)
