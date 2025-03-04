import sys
sys.setrecursionlimit(200000)

def solution(k, room_number):
    answer = []
    used = {}

    def find(room):
        if room not in used:
            used[room] = room + 1  # 다음 빈 방을 기록
            return room
        parent = find(used[room])
        used[room] = parent  # 경로 압축
        return parent

    for preference in room_number:
        empty_room = find(preference)
        answer.append(empty_room)

    return answer