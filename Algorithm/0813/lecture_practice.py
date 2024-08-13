# 연결리스트
# Q_size = 4
# cQ = [0]*Q_size
# front = rear = 0
# print(cQ)
#
#
# rear = (rear+1)%Q_size # enQueue A
# cQ[rear] = 'A'
# print(cQ)
#
#
# rear = (rear+1)%Q_size # enQueue B
# cQ[rear] = 'B'
# print(cQ)
#
#
# front = (front+1)%Q_size # deQueue
# print(cQ[front])
# print(cQ)
#
#
# rear = (rear+1)%Q_size # enQueue C
# cQ[rear] = 'C'
# print(cQ)
#
#
# rear = (rear+1)%Q_size # enQueue D
# cQ[rear] = 'D'
# print(cQ)
#
#
# if (rear+1)%Q_size == front:
#     print('Queue is full')
#     print(cQ)


####################################################################################################
# pop 시간 오래걸리는거 보려주려고 한듯..?

# list_q = []
# for i in range(1000000):
#     list_q.append(i)
# for _ in range(1000000):
#     print(list_q.pop(0))
# print('end')

####################################################################################################
# 우선순위 큐

# 배열을 이용한 우선순위 큐
# 리스트를 이용한
