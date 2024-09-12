## 08/02(금)

### 09:00 ~
- ASCII Code

    7-bit 인코딩으로 128문자를 표현,    
    33개 출력 불가능 제어 문자들과 공백을 비롯한 95개의 출력가능 문자로 이루어짐    
    (33 + 95 = 128)    
    (출력 불가능 제어 문자: 0~31, 127)
    (출력 가능 문자: 32~126)

- 주소가 부여되는 최소단위는 bite

- 인코딩.. 타입???
    - CRLF(for Windows), LF(for Unix & Mac OS), CR(for Classic Mac OS)

- getsizeof: 몇 bite를 사용하고 있는가?
    ```
    import sys
    a = ''
    b = 'a'
    c = 'ab'
    d = 'abc'

    print(sys.getsizeof(a)) # 49 
    print(sys.getsizeof(b)) # 50
    print(sys.getsizeof(c)) # 51
    print(sys.getsizeof(d)) # 52
    ```

    **기본으로 저장하는데 49bite를 사용하는듯? 찾아봐야함**

- Tips
    1. 가우스 기호(올림 ceil, 내림 floor) 기억 


- is, ==

    ```
    s1 = 'abc'
    s2 = 'abd'
    s3 = s1[:2] + 'c'

    print(s2 == s3) # True
    print(s2 is s3) # False
    print(s1 is s2) # True
    ```

- **신기하게도 `s1 is s2 == True`이다**
    
- 왜?
- 같은 대상을 참조했기 때문. (reference가 중요함)


- string: immutable
- list: mutable


***
- **위상 정렬** 개념이란???
***



- **join** 시간 복잡도가 굉장히 낮음 아주 좋은 메서드
    - 같은 기능 구현시, join 활용하는 것이 좋다.


- **early return** 활용 좋은듯 (강사님 추천)
    - 아닌 조건을 정해서 탈출해버림. (depth가 얕아짐!)

- **델타 탐색 dx, dy**를 사용 할 경우 순서가 매우 중요함!

- **델타 탐색 팁**
    ```
    dxy = [[0,1], [1,0], [0,-1], [-1, 0]]
    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
    ```
    강사님 선호 방식