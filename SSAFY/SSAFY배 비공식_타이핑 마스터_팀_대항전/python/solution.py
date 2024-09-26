from itertools import permutations
import sys
# 인코딩
sys.stdin = open('input.txt', 'r', encoding='UTF8')

###############################################################################################
def cal_score(speed, precision, language='E'):
    # 한국어 가중치 0.7
    #  영어 가중치 1.0
    weight = 0.7 if language == 'K' else 1.0
    result = int((speed*precision * weight)/100)
    return result


###############################################################################################
def compare_score(team_ord):
    # 팀 평균 점수
    data_dic[team_ord]['team_score'] = str(sum(data_dic[team_ord]['score']) // 2)

    def min_difference(std_numbers):
        # 초기값 세팅
        min_diff = float('inf')
        for pos_score in permutations(std_numbers, teacher_digit):
            # 가능한 점수차이
            pos_diff = abs(teacher_score - int(''.join(pos_score)))
            # 최소차이 업데이트
            if min_diff > pos_diff: min_diff = pos_diff
        return min_diff # 최소 차이 반환

    # 팀 평균 점수에 해당하는 숫자를 리스트로 형 변환
    student_numbers = list(data_dic[team_ord]['team_score'])
    # 점수의 자리 수
    student_digit = len(student_numbers)
    if student_digit < teacher_digit:
        # 구현핑 점수의 자리 수와의 차이만큼 0 추가
        student_numbers = student_numbers + ['0' for _ in range(teacher_digit - student_digit)]
    # 최소 차이 업데이트
    data_dic[team_ord]['min_difference'] = min_difference(student_numbers)


###############################################################################################
# 제출 순서 체크 함수
# 만약 늦게 제출한 팀원의 순서가 같다면 그냥 팀 번호 낮은 팀이 우선순위 받는걸로... 필요시 수정.
def cal_submit_rank():
    # temp = [[늦게 제출한 팀원의 속도, 팀1 번호], [늦게 제출한 팀원의 속도, 팀2 번호], ...]
    temp = sorted([ [min(data_dic[team_ord]['speed']), team_ord] for team_ord in data_dic['team_ord']], reverse=True)
    for rank in range(len(temp)):
        # 순서/ 팀 번호
        rank, team_ord = rank+1, temp[rank][1]
        # 제출 순서 업데이트
        data_dic[team_ord]['submit_rank'] = rank


###############################################################################################
# 최종 순위 생성 함수
def cal_final_rank():
    # final_result = [[최소차이, 제출순서, 팀1 번호], [최소차이, 제출순서, 팀2 번호], ... ]
    final_result = [
        [data_dic[team_ord]['min_difference'], data_dic[team_ord]['submit_rank'], team_ord]
        for team_ord in data_dic['team_ord']
    ]
    # 최소차이가 작은 순으로 정렬. 최소 차이가 같다면, 제출순서가 빠른 순으로 정렬
    final_result.sort()
    for i in range(len(final_result)):
        # 해당 팀의 최소차이, 팀 번호
        diff, team_ord = final_result[i][0], final_result[i][2]
        # 최종 순위 업데이트
        data_dic[team_ord]['final_rank'] = i+1
        # 출력
        # ex. 1등 : 주조장 사팀원 (8 팀) | 점수 차 : 0 | 원점수 : 643
        print(f'{i+1}등 : {" ".join(data_dic[team_ord]["name"])} ({team_ord} 팀) | 점수 차: '
              f'{diff} | 원점수 : {data_dic[team_ord]["team_score"]}')


###############################################################################################
N = int(input()) # 팀의 수
S, P = map(int, input().split()) # 구현핑 속도/ 구현핑 정확도
teacher_score = cal_score(S, P) # 구현핑 점수
teacher_digit = len(str(teacher_score)) # 구현핑 점수 자리수


# 학생
data_dic = {'team_ord': []}
for team_ord in range(1, N+1):
    data_dic['team_ord'].append(team_ord) # 각 팀의 번호를 저장
    # 속도/ 정확도/ 언어/ 이름
    ns1, np1, lang1, name1 = map(lambda x: int(x) if x.isdecimal() else x, input().split())
    ns2, np2, lang2, name2 = map(lambda x: int(x) if x.isdecimal() else x, input().split())
    data_dic[team_ord] = {
        'name': [name1, name2], 'speed': [ns1, ns2], 'precision': [np1, np2], 'lang': [lang1, lang2],
        'score': {cal_score(ns1, np1, lang1), cal_score(ns2, np2, lang2)}, 'team_score': None,
        'min_difference': None, 'submit_rank': None, 'final_rank': None,}
    compare_score(team_ord)
    # dict_keys(['team_ord', 1, 2, 3, 4, 5, 6, 7, 8])
    # dic['team_ord'].keys() =
    # = dict_keys(['name', 'speed', 'precision', 'lang', 'score', 'team_score',
    # 'min_difference', 'submit_rank', 'final_rank']
cal_submit_rank()
cal_final_rank()

