word = input().strip()
alphabet = [chr(idx) for idx in range(97, 123)]
alphabet_dic = {al:0 for al in alphabet}

for idx in range(len(word)):
    if alphabet_dic[word[idx]] == 0:
        alphabet_dic[word[idx]] = idx+1

for al in alphabet:
    if alphabet_dic[al] == 0: print(-1, end=' ')
    else: print(alphabet_dic[al]-1, end=' ')
print()