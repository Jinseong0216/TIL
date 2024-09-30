############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 리스트 메서드 count 를 사용하지 않습니다.
def count_treasures(treasure_list):
    treasure_dict = {}                                                  # 보물의 이름과 개수를 담을 딕셔너리 생성
    for treasure in treasure_list:                                      # treasure = 수집한 보물의 이름
        treasure_dict[treasure] = treasure_dict.get(treasure, 0) + 1    # 보물의 이름에 해당하는 키가 없는 경우 value가 1, 이미 존재하는 경우 value가 기존 값 + 1 이 됨.
    
    return treasure_dict    # 보물의 이름과 개수를 담은 딕셔너리 반환

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(count_treasures(["gold", "silver", "diamond", "gold", "silver"]))  # {'gold': 2, 'silver': 2, 'diamond': 1}
print(count_treasures(["pearl"]))  # {'pearl': 1}
#####################################################

print(count_treasures([]))