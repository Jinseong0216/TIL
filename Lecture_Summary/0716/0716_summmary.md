# 07/16(화)

- 파이썬 단축평가 기억하기
    ```
    string = 'abcde'
    print(('a' or 'f') in string)   # 'a' -> True -> 'a' -> True
    print(('f' or 'a') in string)   # 'f' -> True -> 'f' -> False
    print(('a' and 'f') in string)  # 'a' -> True: Pass -> 'f' -> True -> 'f' -> False
    print(('f' and 'a') in string)  # 'f' -> True: Pass -> 'a' -> True -> 'a' -> True
    ```  
- OOO구조로 인해 검색 속도가 늦어짐

- list
    - 여러가지 date type을 항목으로 가질 수 있음
    - n차원 배열을 다룰 수 있음

- range

- dictionary 

    | 고유 | 고객명 | 음식명 | 갯수 | 가격 |
    | --- | --- | --- | --- | --- |
    | 1 | sky | 과일 | 2 | 3000 |
    | 2 | 진성 | 반찬 | 1 | 5000 |
    
    위와 같은 표를 dictionary 자료형을 이용하여 아주 편하게 다룰 수 있음!

    ```
    today_scale = {1: ['sky', '과일', 2, 3000], 2: ['진성', '반찬', 1, 5000]}
    ```

- 연산자
    - 실수 연산자: (int,float, ... etc) $\cdot$ (int,float, ... etc)
    - 논리 연산자: (Boolean) $\cdot$ (Boolean)
        - 연산자의 우선순위 : 비교연산자 > 논리연산자

    - 멤버십 연산자: `in, not in`

- ***왜 True는 1 False는 0으로 설정 했을까?***
    - 전류가 들어오면 1 안들어오 오면 0이기 때문

- ***자리를 옮기게 된 경우***
    1. python 설치확인
    2. git 설치확인
    3. vscode 설치확인
    4. 원하는 directory에서 gitbash here
    5. git init
    6. git config --global -l
        - username과 email address 확인
    7. 윈도우 자격증명을 바꿔야함(다른방법있으나 권고)
        
        (1) 찾기 - 자격 증명 관리자

        (2) windows 자격 증명

        (3) github와 lab.ssafy.com을 둘다 편집하면 됨(global name, username, email 바꾸면 됨)
            
    8. git 설정 후 clone 등으로 다시 받아오면 됨(GitHub, labssafy)

- ***얕은 복사, 깊은 복사***
    - 얕은 복사: 두 대상이 같은 주소 값을 가짐
    - 깊은 복사: 두 대상이 다른 주소 값을 가짐

        이전에 내가 깊은 복사를 할 때, `B_list = [element for element in A_list]`로 했지만

        ***아주 편하게 할 수 있는 방법이 있음*** 
        1. `B_list = A_list[:]`
        2. `import copy` 사용

        