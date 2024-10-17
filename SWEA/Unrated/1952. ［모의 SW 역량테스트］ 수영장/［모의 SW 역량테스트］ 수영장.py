for T in range(1, int(input())+1): # 테스트 케이스의 수
    price_lst = list(map(int, input().split())) # 이용권 가격 [price_1, price_2, price_3, price_4]
    schedule = list(map(int, input().split())) # [Jan, Feb, ..., Dec]
    weight = [1, 1, 3, 12]


    def main(price, month):
        global min_value

        if month >= 12: # 파이썬이라 11월이 마지막달임... 탈출조건 지정 및 결과 업데이트
            if min_value > price: min_value = price
            return

        for i in range(4): # 모든 경우에 대한 완전탐색
            new_price = price + (schedule[month] if i == 0 else 1) * price_lst[i] # 일간 이용권 사용시와 아닌경우 가격 업데이트
            next_month = month + weight[i] # 다음번 월 계산
            main(new_price, next_month) # 재귀 호출


    min_value = float('inf')  # 초기값 세팅
    main(0, 0)
    print(f'#{T}', min_value)
