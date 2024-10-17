jdx_range, white_board = [], []
for _ in range(5):
    line = list(input().strip())
    white_board.append(line)
    jdx_range.append(len(line))

for jdx in range(15):
    for idx in range(5):
        if jdx >= jdx_range[idx]: continue
        print(white_board[idx][jdx], end='')
print()