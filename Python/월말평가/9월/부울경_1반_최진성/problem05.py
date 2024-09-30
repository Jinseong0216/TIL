############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 set을 사용하지 않습니다.
def remove_duplicates(lst):
    removed_list = []                       # lst의 원소를 담을 리스트
    for element in lst:                     # element = lst의 원소
        if element not in removed_list:     # element가 removed_list에 없는지 체크
            removed_list.append(element)    # removed_list에 추가

    return removed_list                     # 중복이 제거된 리스트 반환
# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 

print(remove_duplicates([4, 5, 6, 4, 3, 2, 1, 2, 3]))  # [4, 5, 6, 3, 2, 1]
print(remove_duplicates(['a', 'b', 'c', 'a', 'd', 'b']))  # ['a', 'b', 'c', 'd']
print(remove_duplicates([4, 5, 'a', 4, 'b', 2, 'a', 3, 2, 3]))  # [4, 5, 'a', 'b', 2, 3]


