N, M = map(int, input().split())
dic_info = {i: [0]*(N+1) for i in range(1, N+1)}
for _ in range(M):
    prior, subject = map(int, input().split())
    dic_info[subject][prior] = 1

ans = {i: 0 for i in range(1, N+1)}
semester = 1

while dic_info:
    finish_lst = []
    new_dic = {}
    semester = str(semester)
    for subject, priority in dic_info.items():
        if priority == [0]*(N+1):
            finish_lst.append(subject)
            ans[subject] = semester
        else:
            new_dic[subject] = priority

    for subject in new_dic:
        for finish in finish_lst:
            new_dic[subject][finish] = 0
    dic_info = new_dic
    semester = int(semester)
    semester += 1

print(' '.join(ans.values()))