from libs._bridge import init, submit, close

NICKNAME = '방어용사2'
game_data = init(NICKNAME)

def detect_enemy(my_position, color, turn):
    enemy_positions = [(i, j) for i in range(len(map_data)) for j in range(len(map_data[0])) if map_data[i][j][0] == 'E']
    output = 'S'
    
    for enemy in enemy_positions:
        dist = abs(my_position[0] - enemy[0]) + abs(my_position[1] - enemy[1])
        
        if dist == 1:
            if enemy[0] < my_position[0]:
                return 'U F S'
            if enemy[0] > my_position[0]:
                return 'D F S'
            if enemy[1] > my_position[1]:
                return 'R F S'
            if enemy[1] < my_position[1]:
                return 'L F S'
        
        if dist == 2:
            return 'S'
        
    if any(abs(my_position[0] - enemy[0]) + abs(my_position[1] - enemy[1]) > 2 for enemy in enemy_positions):
        return handle_far_enemy(my_position, color)
    
    return output

def handle_far_enemy(my_position, color):
    if color == 'yellow':
        if my_position == [1, 15]:
            return 'D A'
        if my_position == [2, 15]:
            return 'U A'
    
    if color == 'red':
        if my_position == [0, 14]:
            return 'L A'
        if my_position == [0, 13]:
            return 'R A'
    
    if color == 'green':
            return 'D F'  # Return empty string for green

    return 'S'  # Default case

# 입력 데이터 분류
char_to_int = {'U': 0, 'R': 1, 'D': 2, 'L': 3}
map_data = [[]]  
allies = {}
enemies = {}
codes = []  

# 입력 데이터를 파싱하여 변수에 저장
def parse_data(game_data):
    game_data_rows = game_data.split('\n')
    row_index = 0

    # 첫 번째 행 데이터 읽기
    header = game_data_rows[row_index].split(' ')
    map_height, map_width, num_of_allies, num_of_enemies, num_of_codes = map(int, header)
    row_index += 1

    # 맵 초기화
    map_data.clear()
    map_data.extend([game_data_rows[row_index + i].split(' ') for i in range(map_height)])
    row_index += map_height

    # 아군 정보 초기화
    allies.clear()
    for i in range(row_index, row_index + num_of_allies):
        ally = game_data_rows[i].split(' ')
        allies[ally.pop(0)] = ally
    row_index += num_of_allies

    # 적군 정보 초기화
    enemies.clear()
    for i in range(row_index, row_index + num_of_enemies):
        enemy = game_data_rows[i].split(' ')
        enemies[enemy.pop(0)] = enemy
    row_index += num_of_enemies

    # 암호문 정보 초기화
    codes.clear()
    codes.extend(game_data_rows[row_index:row_index + num_of_codes])

idx_r, idx_y, idx_g = 0, 0, 0
moving_list_red = ['L A', 'U A']
moving_list_yellow = ['U A', 'A']
moving_list_green = ['L A', 'U A', 'U A', 'U A', 'U A']
cnt = 0
color = ''

# 메인 반복문
while game_data is not None:
    cnt += 1
    print(f'----입력데이터----\n{game_data}\n----------------')
    parse_data(game_data)

    my_position = next(([i, j] for i in range(len(map_data)) for j in range(len(map_data[0])) if map_data[i][j] == 'A'), [1, 15])
    
    if cnt == 1:
        color = 'red' if my_position == [1, 15] else 'yellow' if my_position == [3, 15] else 'green' if my_position == [5, 15] else ''
    
    output = ''
    if color == 'red':
        idx_r += 1
        output = moving_list_red[idx_r - 1] if 1 <= idx_r <= 2 else detect_enemy(my_position, 'red', cnt)
        
    elif color == 'yellow':
        idx_y += 1
        output = moving_list_yellow[idx_y - 1] if 1 <= idx_y <= 2 else detect_enemy(my_position, 'yellow', cnt)

    elif color == 'green':
        idx_g += 1
        output = moving_list_green[idx_g - 1] if 1 <= idx_g <= 5 else detect_enemy(my_position, 'green', cnt)
    game_data = submit(output)

# 연결 해제
close()
