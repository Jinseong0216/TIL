'''
다음과 같은 규칙에 따라 수들을 만들려고 한다.

첫 번째 수로 양의 정수가 주어진다.
두 번째 수는 양의 정수 중에서 하나를 선택한다.
세 번째부터 이후에 나오는 모든 수는 앞의 앞의 수에서 앞의 수를 빼서 만든다. 예를 들어, 세 번째 수는 첫 번째 수에서 두 번째 수를 뺀 것이고, 네 번째 수는 두 번째 수에서 세 번째 수를 뺀 것이다.
음의 정수가 만들어지면, 이 음의 정수를 버리고 더 이상 수를 만들지 않는다.
첫 번째 수로 100이 주어질 때, 두 번째 수로 60을 선택하여 위의 규칙으로 수들을 만들면 7개의 수들 100, 60, 40, 20, 20 , 0, 20이 만들어진다. 그리고 두 번째 수로 62를 선택하여 위의 규칙으로 수들을 만들면 8개의 수들 100, 62, 38, 24, 14, 10, 4, 6이 만들어진다. 위의 예에서 알 수 있듯이, 첫 번째 수가 같더라도 두 번째 수에 따라서 만들어지는 수들의 개수가 다를 수 있다.

입력으로 첫 번째 수가 주어질 때, 이 수에서 시작하여 위의 규칙으로 만들어지는 최대 개수의 수들을 구하는 프로그램을 작성하시오. 최대 개수의 수들이 여러 개일 때, 그중 하나의 수들만 출력하면 된다.

입력
첫 번째 수가 주어진다. 이 수는 30,000 보다 같거나 작은 양의 정수이다.

출력
첫 번째 줄에는 입력된 첫 번째 수로 시작하여 위의 규칙에 따라 만들 수 있는 수들의 최대 개수를 출력한다.

둘째 줄에 그 최대 개수의 수들을 차례대로 출력한다. 이들 수 사이에는 빈칸을 하나씩 둔다.


100 >>>             8
                    100 62 38 24 14 10 4 6
'''


def fibonacci(n):
    if 0 < n < 3: return 1
    else: return fibonacci(n-1) + fibonacci(n-2)

def make_seq(start_num, second_num):
    seq = [start_num, second_num]
    i = 2

    if start_num < second_num:
        return (i, seq)
    
    else:
        while True:
            s = (fibonacci(i-1)*start_num - fibonacci(i)*second_num) * ((-1)**(i))
            if s < 0: break
            else: 
                seq.append(s)
                i += 1

        return (i, seq)

N = int(input())

max_len = 2
seq = []
for i in range((N // 2), N):
    result1, result2 = make_seq(N, i)
    if result1 > max_len:
        max_len = result1
        seq = result2
        print(max_len)
        print(*seq)

#print(max_len)
#print(*seq)

c = None + ['key']
