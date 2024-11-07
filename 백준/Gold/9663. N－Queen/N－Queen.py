def is_possible(base, comparision):
    if base[0] == comparision[0] or base[1] == comparision[1]: return False
    if abs(base[0]-comparision[0]) == abs(base[1]-comparision[1]): return False
    return True

def dfs(level, available):
    global count
    if level == N: count +=1; return        
    for candidate in available:
        if candidate[0] < level: continue
        new_available = list(queen for queen in available if is_possible(candidate, queen) == True)
        dfs(level+1, new_available)
        if candidate[0] > level: return    
    return

N = int(input())
available_space = [(i, j) for i in range(N) for j in range(N)]
count = 0
dfs(0, available_space)
print(count)
