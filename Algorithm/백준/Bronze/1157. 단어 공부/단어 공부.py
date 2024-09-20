max_freq = 0
freq_dic = {}
freq_w = []
word = input().strip()
for w in word:
    w = w.upper()
    freq_dic[w] = freq_dic.get(w, 0)+1
    if max_freq < freq_dic[w]:
        max_freq = freq_dic[w]
        freq_w = [w]
    elif max_freq == freq_dic[w]:
        freq_w.append(w)

if len(freq_w) > 1: print('?')
else: print(freq_w[0])