# Initial values
N, M, x, y, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

# Bottom, Side-Left, Side-Bottom, Side-Right, Side-Top, Top
dice = [0, 0, 0, 0, 0, 0]
delta = [None, (0, 1), (0, -1), (-1, 0), (1, 0)]

def rolling_dice(position, command):
    global dice, grid

    x, y = position
    dx, dy = delta[command]
    nx, ny = x+dx, y+dy

    if nx < 0 or ny < 0 or nx >= N or ny >= M: return x, y

    if command == 1: dice[0], dice[1], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[1]    
    elif command == 2: dice[0], dice[1], dice[3], dice[5] = dice[1], dice[5], dice[0], dice[3]
    elif command == 3: dice[0], dice[2], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[2]
    elif command == 4: dice[0], dice[2], dice[4], dice[5] = dice[2], dice[5], dice[0], dice[4]

    if grid[nx][ny] == 0: grid[nx][ny] = dice[0]
    else: dice[0], grid[nx][ny] = grid[nx][ny], 0        
    return nx, ny

for command in commands:
    nx, ny = rolling_dice((x, y), command)
    if nx == x and ny == y: continue
    x, y = nx, ny
    print(dice[5])