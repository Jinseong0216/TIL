sentence = input().strip()
cnt = 0
for character in sentence:
    if ord(character) == 32: cnt += 1

if sentence == '': print(0)
else: print(cnt+1)