# # 인사성 밝은 곰곰이

ans = 0 # 정답을 기록할 변수
info = {} # 채팅을 이미 입력한 사람
for _ in range(int(input())):
    record = input()
    if record == 'ENTER': info ={} # 새로운 사람이 입장 시, 채팅기록 초기화
    else:
        ans += info.get(record, 1)
        info[record] = 0
print(ans)ㄴ