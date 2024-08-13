from collections import deque

TC = int(input())
for T in range(1, 1 + TC):
    N, M = map(int, input().split())                                  # N이 화덕 크기 / M이 피자 개수
    pizzas = list(enumerate(map(int, input().split()), start=1))      # 3 5 8 5 1  => [(1, 3), (2, 5)]
    fire_place, pizzas = pizzas[:N], pizzas[N:]                       # [(1,3), (2,5) ....]
    answer = -1
    while fire_place:                                                 # 화덕이 빌 때까지
        pizza = fire_place.pop(0)                                     # 화덕에서 피자 뽑기
        if pizza[1] < 2:                                              # 치즈가 0,1 인 경우
            answer = pizza[0]                                           # 뽑은 피자 번호를 answer로 업데이트
            if pizzas:                                                      # 대기 피자가 남아있으면
                fire_place = fire_place + [pizzas.pop(0)]                   # 화덕 마지막칸에 넣음
        else:
            pizza_idx, cheese_info = pizza[0], pizza[1]//2           # 뽑은 피자의 치즈가 2이상인 경우, 치즈 반으로 줄임
            fire_place = fire_place + [(pizza_idx, cheese_info)]     # 다시 화덕의 마지막칸에 넣음

    print(f'#{T} {answer}')


