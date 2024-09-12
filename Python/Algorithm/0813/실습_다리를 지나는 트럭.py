def solution(bridge_length, weight, truck_weights):
    answer = 1
    now_weight = truck_weights.pop(0)
    bridge = [0]*(bridge_length-1) + [now_weight] # 첫차가 다리에 입장한 상태
    next_truck = []
    while truck_weights + next_truck:
        now_weight -= bridge.pop(0)  # 무게 업데이트

        if next_truck == []:
            truck_weight = truck_weights.pop(0)
            next_truck.append(truck_weight)

        if now_weight + truck_weight <= weight: # 무게 비교
            bridge.append(truck_weight)  # 트럭 입장
            now_weight += truck_weight   # 무게 업데이트
            next_truck.pop(0)            # 다음 차량 초기화

        else:
            bridge.append(0) # 트럭 대기, 새롭게 다리 뒤에 0 추가
        answer += 1 # 이번 회차 끝났으니 시간초 추가

    answer += bridge_length
    return answer

