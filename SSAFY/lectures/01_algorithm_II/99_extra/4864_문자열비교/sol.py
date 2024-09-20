import sys
sys.stdin = open('input.txt')

# 3개의 함수
# 브루트 포스
def brute_force(pattern, target):
    pattern_index = 0
    target_index = 0
    origin_target_index = 0
    while target_index < len(target):
        # 특수한 상황
        if pattern[pattern_index] != target[target_index]:
            pattern_index = -1
            target_index = origin_target_index
            origin_target_index += 1
        # 모든 상황에 대해 항상 동일하게 동작
        target_index += 1
        pattern_index += 1

        if len(pattern) == pattern_index:
            return True
    return False
# KMP
def KMP(pattern, target):
    def make_lps():
        lps = [0] * len(pattern)
        # 0번쨰 요소는 앞에 중복되는 값이 있을리 없다.
        for idx in range(1, len(pattern)):
            if pattern[idx] == pattern[lps[idx-1]]:
                lps[idx] = lps[idx - 1] + 1
        lps.insert(0, -1)
        return lps
    lps = make_lps()

    pattern_index = 0
    target_index = 0
    while target_index < len(target):
        if pattern[pattern_index] != target[target_index]:
            pattern_index = lps[pattern_index]
        target_index += 1
        pattern_index += 1

        if pattern_index == len(pattern):
            return True
    return False
# 보이어무어
def boyer_moore(pattern, target):
    char_table = {pattern[idx]: len(pattern) -1 -idx for idx in range(len(pattern))}

    pattern_index = len(pattern)
    target_index = 0
    while target_index <= len(target) - pattern_index:
        for p_idx in range(pattern_index-1, -1, -1):
            if target[target_index + p_idx] != pattern[p_idx]:
                target_index += char_table.get(target[target_index + p_idx], len(pattern))
                break
        else:
            return True
    return False


T = int(input())

for tc in range(1, T+1):
    pattern = input()
    target = input()
    result = boyer_moore(pattern, target)
    print(pattern in target)