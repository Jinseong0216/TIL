# 각 혈액형의 인원수를 계산하는 딕셔너리를 생성하기.
blood_types = ['A', 'B', 'O', 'AB', 'A', 'O', 'B', 'A', 'AB', 'O', 'A', 'B']


# 1. [] 표기법을 사용한 방법
def count_blood_types(blood_types):
    blood_dic = {}
    for blood in blood_types:
        if blood in blood_dic:
            blood_dic[blood] += 1
        else:
            blood_dic[blood] = 1
    return blood_dic


print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}


# 2. get() 메서드를 사용한 방법
def count_blood_types(blood_types):
    blood_dic = {}
    for blood in blood_types:
        blood_dic[blood] = blood_dic.get(blood, 0) + 1
    return blood_dic

print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}
