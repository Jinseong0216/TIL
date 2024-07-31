############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 min, max, sorted 함수 리스트 메서드 sort 를 사용하지 않습니다.
def population_difference(population_list):
    max_town, min_town = population_list[0], population_list[0]     # 인구 수가 최대, 최소인 마을을 찾기 위함(기준 점, 첫 번째 마을)
    for population in population_list:                              
        if population > max_town: max_town = population             # 기존의 최대 인구 수와 비교하여 더 크다면 업데이트
        if population < min_town: min_town = population             # 기존의 최소 인구 수와 비교하여 더 작다면 업데이트

    return max_town - min_town                                      # 최대 인구 수 - 최소 인구 수
    

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(population_difference([100, 200, 300, 400, 500]))  # 400
print(population_difference([50, 150, 250]))  # 200
print(population_difference([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]))  # 90
#####################################################
