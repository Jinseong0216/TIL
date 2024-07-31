############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def find_max_position(matrix):
    N = len(matrix)                     # 행렬의 크기
    x, y = 0, 0
    entry = matrix[x][y]                # 최대 값의 초기 값을 matrix[0][0]으로 설정
    for i in range(N):
        for j in range(N):
            if entry < matrix[i][j]:    # 현재 값이 기존의 최대 값보다 큰지 확인
                entry = matrix[i][j]    # 최대 값을 현재 값으로 할당
                x, y = i, j             # 위치 인덱스 업데이트
    return [x, y]
# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

# 예시 행렬 데이터
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 2, 3],
    [4, 5, 6],
    [7, 8, 1]
]

matrix3 = [
    [9, 2, 5],
    [4, 9, 6],
    [7, 8, 1]
]
#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(find_max_position(matrix1))  # [2, 2]
print(find_max_position(matrix2))  # [0, 0]
print(find_max_position(matrix3))  # [0, 0]
#####################################################
