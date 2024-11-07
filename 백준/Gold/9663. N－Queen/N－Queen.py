def dfs(level, columns, diag1, diag2):
    global count
    if level == N: 
        count += 1; return
    
    for col in range(N):
        if col in columns: continue
        if (level - col) in diag1: continue
        if (level + col) in diag2: continue 
        
        columns.add(col); diag1.add(level - col); diag2.add(level + col)
        
        dfs(level + 1, columns, diag1, diag2)
        
        columns.remove(col); diag1.remove(level - col); diag2.remove(level + col)

N = int(input())
count = 0
columns, diag1, diag2 = set(), set(), set()

dfs(0, columns, diag1, diag2)
print(count)