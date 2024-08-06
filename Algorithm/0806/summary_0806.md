## 08/06(화)

### 09:00
- stack
    1. 선형 구조
    2. **후입 선출**
    
    - top: 가장 마지막에 삽입된 원소
    - push: 삽입
    - pop: 삭제

```
stack = []
stack.append(1) # push(1)
stack.append(2) # push(2)
stack.append(3) # push(3)
print(stack.pop())
print(stack.pop())
print(stack.pop())

>>> 3
2
1
```