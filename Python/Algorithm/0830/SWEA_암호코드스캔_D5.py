import sys
sys.stdin = open('input.txt', 'r')

# 유효성 검사 함수
def is_valid(codes):
    codes = [decoder[code] for code in codes]
    validity = 0
    for i in range(1, 8): validity += (2*(i%2)+1)*codes[i]
    if (validity+codes[0])%10 == 0: return sum(codes)
    else: return 0


# 단축해서 7자리 코드로만드는 함수
def shortening(code, weight):
    if weight == 1: return code
    r = ''
    for cnt in range(7):
        c = set(code[cnt*weight:(cnt+1)*weight])
        if len(c) == 1: r += code[cnt*weight]
    return r

# 디코더정보(역순으로 저장)
decoder = {'1011000': 0, '1001100': 1, '1100100': 2, '1011110': 3,
           '1100010': 4, '1000110': 5, '1111010': 6, '1101110': 7,
           '1110110': 8, '1101000': 9}


for T in range(1, int(input())+1):
    # 바코드 정보 저장
    barcode = []
    # 가로 세로 크기
    N, M = map(int, input().split())
    # 16진수 -> 2진수변환 후의 길이M
    M = 4*M
    # 바코드 만들기
    for _ in range(N):
        hex_code = input().strip()
        # 16진수를 2진수로 변환한 후, 역순으로 저장
        barcode.append((''.join(bin(int(hex_num, 16))[2:].zfill(4) for hex_num in hex_code))[::-1])

    # 코드의 가능한 최대 굵기
    weight_bound = M//56
    ans = 0
    for weight in range(1, weight_bound+1):
        idx, jdx = 0, 0
        while idx < N:
            # 검사할 행
            row = barcode[idx]
            # 범위 지정
            while jdx < M-((weight*56)-1):
                # 시작이 1이라면 검사를 진행
                if row[jdx:jdx+weight] == '1'*weight:
                    # 코드를 담을 리스트
                    codes = []
                    # 코드의 굵기를 고려하여 코드 변환
                    code = shortening(row[jdx:jdx+7*weight], weight)
                    # 숫자로 표현이 가능한 코드라면
                    if code in decoder:
                        # 코드 검사의 시작점 체크(2줄짜리 코드면 1줄만 검사하기위함)
                        if idx==0 or (shortening(barcode[idx-1][jdx: jdx+7*weight], weight) not in decoder):
                            # 숫자로 표현이 가능한 코드라면 추가
                            codes.append(code)
                            # 8개 검사
                            for cnt in range(1, 8):
                                code = shortening(row[jdx+7*weight*cnt:jdx+7*weight*(cnt+1)], weight)
                                # 숫자 변환 불가 코드라면 중지
                                if code not in decoder: break
                                codes.append(code)
                            # 숫자8개로 표현이 가능한 코드라면
                            if len(codes)==8:
                                # 검사 후의 열 지정
                                jdx = jdx+56*weight
                                # 유효성 검사 후 더하기
                                ans += is_valid(codes)
                                continue
                jdx = jdx+1
            idx, jdx = idx+1, 0

    print(f'#{T}', ans)