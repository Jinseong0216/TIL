from itertools import permutations

pos_list = list(permutations(['1','1','2'], 3))
teacher_score = 0
min_diff = min(abs(teacher_score - int(''.join(pos_score))) for pos_score in pos_list)
print(min_diff)