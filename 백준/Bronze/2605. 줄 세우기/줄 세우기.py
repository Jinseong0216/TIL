N = int(input())
# 학생이 뽑는 번호표 저장
arr = list(map(int, input().split()))
# 학생들이 줄 선 순서가 들어갈 칸
order = []


for i in range(N):
    student = i+1 # 학생번호
    seat = i-arr[i]  # 학생이 들어갈 위치
    # seat보다 앞에있는 학생들은 그대로
    # seat번째 위치에는 새로 들어온 학생번호
    # seat보다 뒤에있던 학생들을 새로 들어온 학생의 뒤로 이동
    order = order[:seat] + [student] + order[seat:]
print(*order)
