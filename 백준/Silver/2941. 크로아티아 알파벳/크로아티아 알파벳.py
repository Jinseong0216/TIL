word = input().strip()
L = len(word)
idx, cnt = 0, 0
while idx < L:
    if word[idx] == 'c':
        if idx+1<L and (word[idx+1] == '=' or word[idx+1] == '-'): idx = idx+2
        else: idx = idx+1
        cnt = cnt+1
    elif word[idx] == 'd':
        if idx+2<L and word[idx+1:idx+3] == 'z=': idx = idx+3
        elif idx+1<L and word[idx+1] == '-': idx = idx+2
        else: idx = idx+1
        cnt = cnt+1
    elif word[idx] == 'l':
        if idx+1<L and word[idx+1] == 'j': idx = idx+2
        else: idx = idx+1
        cnt = cnt+1
    elif word[idx] == 'n':
        if idx+1<L and word[idx+1] == 'j': idx = idx+2
        else: idx = idx + 1
        cnt = cnt+1
    elif word[idx] == 's':
        if idx+1<L and word[idx+1] == '=': idx = idx+2
        else: idx = idx + 1
        cnt = cnt+1
    elif word[idx] == 'z':
        if idx-1>=0 and idx+1<L and word[idx-1:idx+2] == 'dz=': continue
        elif idx+1<L and word[idx+1] == '=': idx = idx+2
        else: idx = idx + 1
        cnt = cnt+1
    else:
        idx = idx+1
        cnt = cnt+1

print(cnt)