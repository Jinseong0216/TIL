import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    numbers, N = input().split()  # 숫자 문자열과 스왑 횟수를 입력받음
    arr = []  # 숫자 배열
    arr_copy = []  # 복사본 배열
    cnt = 0  # 스왑 횟수 카운터
    idx = -1  # 최대값을 교환할 위치

    # 입력받은 숫자 문자열을 정수형 리스트로 변환
    for i in range(len(numbers)):
        arr.append(int(numbers[i]))  # 원본 배열 생성
        arr_copy.append(int(numbers[i]))  # 복사본 배열 생성

    while cnt < int(N):
        max_v = max(arr_copy)  # 현재 배열에서의 최대값을 찾음
        if max_v != 0:  # 최대값이 0이 아닐 경우
            for i in range(len(arr_copy)-1, -1, -1):  # 배열의 끝에서부터 탐색
                if arr_copy[i] == max_v:  # 최대값을 찾았을 경우
                    arr_copy[i] = 0  # 해당 값을 0으로 변경하여 다시 선택되지 않도록 함
                    idx += 1  # 교환할 위치 업데이트
                    break  # 최대값 찾기 종료
            for i in range(len(arr)-1, idx, -1):  # 원본 배열에서 최대값을 교환할 위치 찾기
                if arr[i] == max_v:  # 최대값을 찾았을 경우
                    arr[i], arr[idx] = arr[idx], arr[i]  # 최대값을 교환할 위치로 스왑
                    cnt += 1  # 스왑 횟수 증가
                    if arr[idx] == arr[idx-1]:  # 스왑 후 동일한 값이 나올 경우
                        if arr[i] < arr[i+1]:  # 더 큰 값이 뒤에 있을 경우
                            arr[i], arr[i+1] = arr[i+1], arr[i]  # 한 번 더 스왑하여 위치 조정
                            break  # 추가 스왑 종료
                    else:
                        break  # 스왑 종료

        elif max_v == 0:  # 모든 최대값이 사용된 경우
            arr[len(arr)-1], arr[len(arr)-2] = arr[len(arr)-2], arr[len(arr)-1]  # 마지막 두 요소 스왑
            cnt += 1  # 스왑 횟수 증가

    print(f'#{tc}', ''.join(map(str, arr)))  # 결과 출력
