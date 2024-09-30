############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def max_adjacent_sum(matrix):
    N = len(matrix)
    new_matrix = [[0] * (N+2)] + [ [0] + row + [0] for row in matrix] + [[0] * (N+2)]   # 확장 한 행렬 만들기
    max_sum = matrix[0][0] + matrix[0][1] + matrix[1][0]                                # 최대 값을 계산하기 위함(초기 값 설정)
    for i in range(1, 1+ N):
        for j in range(1, 1+N):
            s = new_matrix[i][j-1] + new_matrix[i][j] + new_matrix[i][j+1] + new_matrix[i+1][j] + new_matrix[i-1][j] # 계산
            if s > max_sum: # 계산 결과가 기존의 최대 값 보다 큰지 확인
                max_sum = s # max_sum을 새롭게 확인 한 최대 값으로 업데이트
    return max_sum          # 최대 값 반환
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

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(max_adjacent_sum(matrix1))  # 29
print(max_adjacent_sum(matrix2))  # 25
#####################################################
