# 회식장소 정하기
# 1반 반장 원겸이와 CA 경민이는 한붓그리기를 통하여 회식장소를 정하고자 한다.
# 둘 모두 한붓그리기가 가능한 경우:
#                    같은 장소를 지나가는 경우 해당 장소에서 회식을 하려고 한다.
#                    가능한 모든 회식 장소를 출력하시오
#                    한붓 그리기는 가능하지만, 같은 장소를 지나가지 않는 경우 회식 실패를 출력한다.
#                    같은 장소로(삼성전기 기숙사 입구는 고려하지 않는다.)
# 둘 중 한명이라도 한붓그리기를 할수 없다면, 회식 실패를 출력한다.

# 원겸이와 경민이는 모두 삼성전기 기숙사 입구에서 출발한다.
# 장소 0 = 삼성전기 기숙사 입구
# 장소 1 = 명지 1동
# 장소 2 = 명지 2동
# 장소 3 = 하단
# 장소 4 = 사상
# 장소 5 = 송삼
# 장소 6 = 신호동
# 장소 7 = 광안리
# 장소 8 = 서면
# 장소 9 = 동래


[입력]

테스트 케이스의 수
전체 노드의 수, 전체 엣지의 수
원겸이가 지나가야 할 노드
경민이가 지나가야 할 노드
테스트 케이스의 수 # T
전체 노드의 수, 전체 엣지의 수 # N, E, root
노드1 노드2 0 or 1
... E번
노드1 노드2 0 or 1

ord_lst = {원겸: [[] _ in range(노드수)], 경민: [[] _ in range(노드수)]}

def dfs(node, name, cnt):
    global ord_lst
    if cnt == 원겸개수:
        for idx in range(L):
            if visited[idx]:
                if ord_lst
        for vertex, order in visited:
            pass





