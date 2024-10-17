x_lst, y_lst, coordinates = [], [], []
for _ in range(3):
    x, y = map(int, input().split())
    x_lst.append(x), y_lst.append(y), coordinates.append([x, y])

X, Y = set(x_lst), set(y_lst)
ans = [str(x)+' '+str(y) for x in X for y in Y if [x, y] not in coordinates]
print(ans[0])