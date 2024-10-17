converter = {'F': 0, 'D0': 1, 'D+': 1.5, 'C0': 2, 'C+': 2.5,
                 'B0': 3, 'B+': 3.5, 'A0': 4, 'A+': 4.5, 'P': 0}
cum_grade, cum_score = 0, 0
for _ in range(20):
    lecture_name, grade, score = input().split()
    if score == 'P': continue
    grade = int(float(grade))
    cum_grade = cum_grade+grade
    cum_score = cum_score+grade*converter[score]

print(cum_score/cum_grade)