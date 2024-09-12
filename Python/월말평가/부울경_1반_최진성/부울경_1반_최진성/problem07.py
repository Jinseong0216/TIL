############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def calculate_days_to_fill_tank(tank_capacity, fill_amount, evaporation_amount):
    day = 1                                                     # 경과한 날 
    current_amount = fill_amount                                # 첫 날에는, 이미 물을 채우고 시작
    while (current_amount - tank_capacity) < 0:                 # 현재 물의 양 < 채워야 하는 총 용량인 경우 계속 반복
        current_amount += fill_amount - evaporation_amount      # 물 채우기와 물 증발하기 동시에 진행
        day += 1                                                # 하루 경과

    return day                                                  # 걸리는 일수 반환
# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(calculate_days_to_fill_tank(100, 20, 5))  # 7
print(calculate_days_to_fill_tank(1000, 100, 10))  # 11
print(calculate_days_to_fill_tank(100, 10, 1))  # 11
#####################################################

