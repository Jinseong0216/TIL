## 07/23(화)

### 09:00 ~ 11:00

- 딕셔너리 관련 메서드

    1. .clear(): 딕셔너리 모든 키/값 쌍 제거

    2. get(key, [, default]): 키 해당 값 반환 or **없으면 None이나 default값 반환**

    3. ...

    4. .pop(): 메서드가 list의 .pop() 메서드와 다름을 알아야함.    
        다른 class에 존재함.

    5. .setdefault(): 키와 연결된 값 반환,      
        키가 없다면 '해당 키': default를 딕셔너리에 추가 후 반환
        ```
        person = {'name': 'Alice', 'age': 25}
        print(person.setdefault('country', 'KOREA'))
        print(person)

        >>>
        KOREA
        {'name': 'Alice', 'age': 25, 'country': 'KOREA'}
        ```
    
    6. .update([other]): other가 제공하는 키/값 쌍으로 딕셔너리를 갱신, 기존 키는 덮어씀    
        **실습 권장** 

- 셋 관련 메서드

    1. .add():
    
    2. .clear():

    3. .remove(): 없는 항목 제거하려하면 에러 발생

    4. .pop(): list에서는 순서, dictionary에서는 특정 키 기준
        그러나.. set에서는 **임의의 원소**를 제거후 반환...

        **임의**?   
        **code를 돌려보면 같은 원소만 빠지는 걸 확인 할 수 있는데.. 왜 그럴까?**
    
    5. .discard(): 지우려는 원소가 없어도 에러 발생하지 않음.


    - **해시 테이블**

        (1) 해시 함수를 사용하여 변환한 값을 색인(index)으로 삼아 key와 data를 저장하는 자료 구조

        데이터를 효율적으로 저장하고 검색하기 위해 사용

        (2) **해시 함수**

        - python이 재실행 될 때마다, 해시 함수의 구조가 바뀜

        - 그래서, terminal을 통해서 set1.pop()을 했을 때, 결과가 계속 달라지고    
                vscode or jupyter를 통해서 실행 할 때는, 결과가 계속 같았던 것.

        - 임의의 크기 데이터 -> 고정된 길이 고유값(정수임)으로 변환 시킴

        - 지문과 같은 역할, 데이터를 고유하게 식별

        - 주로, 테이블 자료구조에 사용 & 빠른 데이터 검색을 위해 사용.(파이썬이 아니라도)

        print(set)을 하더라도 해시 테이블에 저장된 순서대로 출력 하는 것.
        + 정수들은 해시테이블에도 동일하게 뿌려짐.

        그래서 print({1,2,3,4,5}) >>> {1,2,3,4,5} 이 됨

        - python hash function = F

            1. F(정수 m) = m: 왜..? 효율적 일 처리를 위함.

            그렇다고 하더라도 ...

        - 가변 데이터는 해시 불가능

        - 99-dict-practice-01 & 02.py 풀기 추천


### Sky 요약 11:00 ~
- Create Read Update Delete를 항상 목표로.



- generator
    1. range가 대표적
    ``` 
    print(range(0,5))   >>> range(0,5)
    ```
    2. overflow방지
    3. 순회를 시켜줌