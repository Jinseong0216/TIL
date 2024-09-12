def fnct(seq, k):
    return seq[k-2]-seq[k-1]
N = int(input())
max_len = 4
max_seq = [N, N, 0, N]
for i in range(N//2, N):
    seq = [N, i]
    while seq[-1] >= 0:
        seq.append(seq[-2]-seq[-1])
    seq.pop()
    if max_len < len(seq):
        max_len = len(seq)
        max_seq = seq

print(max_len)
for s in max_seq:
    print(s, end=' ')
print()


