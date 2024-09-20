import sys
sys.stdin = open("input.txt", "r")

T = int(input())


# 자리수에 따라 가중치를 계산해줘욤
def cal_weight(index):
    weight = 10 ** ((len(numbers) - 1) - index)
    return weight


for tc in range(1, T + 1):
    tmp_numbers, exchange = input().split()

    numbers = list(map(int, tmp_numbers))

    for cnt in range(int(exchange), 0, -1):
        target_numbers = sorted(numbers, reverse=True)

        different_cnt = 0
        for cmp in range(len(numbers)):
            if numbers[cmp] != target_numbers[cmp]:
                different_cnt += 1

        # CASE 1: 이미 완벽하게 정렬이 되어있다면..
        if numbers == target_numbers:
            # 똑같은 숫자 있음 그거 바꿔
            for s in range(len(numbers) - 1):
                if numbers[s] == numbers[s + 1]:
                    numbers[s], numbers[s + 1] = numbers[s + 1], numbers[s]
                    break
            else:
                # 아니면 걍 젤 작은 거 바꿔
                numbers[-1], numbers[-2] = numbers[-2], numbers[-1]

        # CASE 2: 숫자를 맞바꾸기 했을 때와 남은 바꾸기 횟수가 같으면
        # 어차피 내림차순 정렬한 것으로 잘 나올 거니께..ㅎㅎ
        elif different_cnt == (cnt * 2):
            numbers = target_numbers
            break

        # CASE 3: 다 안 되면,, 가중치 큰 거랑 숫자 큰 거(가중치 작은 거) 바꿈
        else:
            # 내림차순으로 정렬한 것과 비교하며 다른 숫자부터 확인한다.
            start_target = 0
            for t in range(len(numbers)):
                if numbers[t] != target_numbers[t]:
                    start_target = t
                    break

            # 바꿀 거 1 : 가중치 곱한 값이 큼
            max_value, index1, min_num = -1, -1, -1
            # 바꿀 거 2: 가중치 곱한 값이 작음 & 숫자가 큼
            min_value, index2, max_num = -1, -1, -1

            for i in range(start_target, len(numbers)):
                # 가중치 * 숫자 = value
                now_weight = cal_weight(i)
                now_value = -1
                if numbers[i] == 0:
                    now_value = now_weight - 1
                    # 0일때 굳이 0으로 만들어야 하나? 그냥 -1 해도 상관없을 거 같은데
                else:
                    now_value = now_weight * numbers[i]

                # 바꿀 거 1
                # 가중치를 곱한 값이 최대다! ! 어 너 목표대상이야
                if now_value > max_value:
                    max_value = now_value
                    index1 = i
                    min_num = numbers[i]

                # 바꿀 거 2
                # 숫자가 최대다 !!! ㄴㅓ 목표대상이야 짱의 자리로 가자
                if numbers[i] > max_num:
                    min_value = now_value
                    index2 = i
                    max_num = numbers[i]
                # 오엥 숫자가 중복된다....
                # 그럼 가중치 곱한 값까지 확인해서 자를 바꾸면 좋겠지용
                elif numbers[i] == max_num and now_value <= min_value:
                    min_value = now_value
                    index2 = i
                    max_num = numbers[i]

            numbers[index2], numbers[index1] = numbers[index1], numbers[index2]

    print(f'#{tc} {"".join(map(str, numbers))}')