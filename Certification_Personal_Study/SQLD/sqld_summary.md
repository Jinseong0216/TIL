## 1과목(DB modeling, ERD, 정규화-NF)

- relationship
    1. 관계를 맺는다는 의미는 부모의 식별자를 자식에 상속하고, 상속된 속성을 매핑키(조인키)로 활용한다는 것
   
- 관계의 분류
  1. 존재에 의한 관계
        - 사원 엔터티와 부서 엔터티
  2. 행위에 의한 관계 
        - 주문은 고객에 의해 발생

- 조인의 의미
    - 데이터의 중복을 피하기 위해서 테이블은 정규화에 의해 분리됨.
        분리되면서 두 테이블은 서로 관계를 맺게 되고, 다시 두 테이블의 데이터를 동시에 출력하거나 관계가 있는 테이블을 참조하기 위해서는 데이터를 연결해야 하는데 이 과정을 조인이라고 함

    계좌
    | 계좌번호 | 예수금 | 관리점코드|
    |---|---|---|
    |100111|100|1000|
    |100222|200|1001|

    관리점
    |관리점코드|관리점|
    |---|---|
    |1000|서울점|
    |1001|경기점|
    
    ```
    SELECT A.계좌번호, B.관리점
    FROM 계좌 A, 관리점 B
    WHERE A.관리점코드 = B.관리점코드
    AND A.계좌번호 = '100111'
    ```

    - 계층형 데이터 모델
      - 하나의 엔터티 내의 인스턴스들끼리 계층 구조를 가지는 경우임
      - 계층 구조를 갖는 인스턴스끼리 연결하는 조인을 셀프조인이라고 함(같은 테이블 여러번 조인)
  
### 트랜잭션
- 하나의 연속적인 업무단위임!
  
    트랜잭션에 의한 관계는 **필수적인 관계형태**를 가짐
  
    하나의 트래잭션에는 여러 SELECT, INSERT, DELETE, UPDATE 등이 포함 될 수 있음!
  
- **필수적, 선택적 관계와 ERD**

    두 엔터티의 관계가 서로 필수적일 때 하나의 트랜잭션을 형성

    두 엔터티가 서로 독립적으로 수행이 가능하다면 선택적 관계로 표현

    IE-표기법
        - 원을 사용하여 필수적 관계와 선택적 관계를 구분
        - **필수적 관계에는 원을 그리지 않는다**
        - **선택적 관계에는 관계선 끝에 원을 그린다.**
    
    바커-표기법
        - 실선과 점선으로 구분
        - **필수 = 실선**
        - **선택 = 점선**
  
- DBMS(Data Base Management System): DB관리 시스템
    Null은 DBMS에서 아직 정해지지 않은 값을 의미함

    1. Null을 포함한 연산결과는 항상 Null
    2. 집계함수(sum, avg, min, max, count 등의 함수)는 항상 Null을 무시한 값을 리턴
        (COUNT = 행의 수를 리턴)
        ```
        SELECT AVG(COMM), SUM(COMM)/COUNT(*)
            FROM EMP.
        ```
        AVG(COMM) = NULL개수 안세고 값이 있는 애들끼리의 평균을 구한 것
        SUM(COMM)/COUNT(*) = 전체의 합에서 Null값이 애들의 수도 포함하여 평균을 구한 것
        즉, 두 값의 결과가 전혀 다름!!


## 메모
- VARCHAR(50): 50byte까지 넣을 수 있는 가변길이 문자열
- CHAR(50): 50byte까지 넣을 수 있는 고정길이 문자열
  - EX: VARCHAR(50)에서 "12345"는 = "12345                                         "
        (남은 공간을 공백으로 채워서 고정 길이로 만들어 줌)
        CHAR(50)에서 "12345"는 "12345"
        (가변 길이라서 상관 없음)

## 2과목 Part 2. (서브쿼리, 집합연산자, 그룹함수, 윈도우함수)

### 서브쿼리
- 서브쿼리 
  1. 동작 방식에 따른 서브쿼리
  - UN-CORRELATED(비연관) 서브쿼리
  - CORRELATED(연관) 서브쿼리
    
  2. 위치에 따른 서브쿼리
  - 스칼라
  - 인라인 뷰
  - WHERE 절

- 주의사항
  - **서브쿼리는 ORDER BY절에 사용할 수 없음.!!**
  - 연산자의 선택이 중요함
  

#### WHERE절 서브쿼리
1. 단일 행 서브쿼리
2. 다중 행 서브쿼리
   1. 비교 연산자 사용 불가
      1. IN
        1. >ANY: ANY안의 값에서 최소보다 큰행 반환
         - >ANY(2000, 3000) 2000보다 큰 행 반환
      2. <ANY
         - <ANY(2000, 3000) 2000보다 작은 행 반환
      3. >ALL
         - >ALL(2000, 3000) 3000보다 큰 행 반환
      4. <ALL
         - <ALL(2000, 3000) 2000보다 작은 행 반환 
3. 다중 열 서브쿼리
4. 상호연관 서브쿼리
   - 메인쿼리와 서브쿼리의 비교를 수행하는 단계
   - 비교할 집단이나 조건은 서브쿼리에 명시(메인쿼리절에는 서브쿼리 컬럼이 정의 안되서 에러 발생함)


#### 인라인뷰 서브쿼리
- **FROM절에 사용**
- 쿼리안의 뷰 형태로 테이블철머 조회할 데이터를 정의하기 위해 사용
- 테이블명이 존재하지 않기 때문에 다른 테이블과 조인 시 반드시 테이블 별칭 명시해야함
    (단독으로 사용하는 경우 불필요함)
- WHERE 절과 다르게 서브쿼리의 결과를 메인 쿼리 어느 절에서도 사용 가능 
    (당연함. FROM이 DBMS가 가장 먼저 읽는 절이기 때문.)
- 인라인뷰의 결과와 메인쿼리 테이블과 조인할 목적으로 주로 사용.
- 모든 연산자 사용 가능함

```
SELECT  E.EMPNO, E.ENAME, E.SAL, I.MAX_SAL
FROM    EMP E, (SELECT DEPTNO, MAX(SAL) AS MAX_SAL
                FROM  EMP
                GROUP BY DEPTNO) I
WHERE   E.DEPTNO = I.DEPTNO
    AND E.SAL = I.MAX_SAL;
```


#### 스칼라 서브쿼리
- **SELECT절에 사용**
- 하나의 컬럼처럼 표현하기 위해 사용
- 각 행마다 스칼라 서브쿼리 결과가 하나여야 함!!!!(단일행 서브쿼리 형태)
- 조인의 대체연산
- 스칼라 서브쿼리를 사용한 조인 처리 시, OUTER JOIN이 기본 값이 됨(값이 없어도 생략안되고 NULL 됨)
  (메인 쿼리절이 출력하는 대상에 대해 항상 값을 리턴해야 하므로, 생략되지 않고 NULL로 출력 되는 것!!)


### 집합 연산자
- SELECT문 결과를 하나의 집합으로 간주, 그 집합에 대한 합집합, 교집합, 차집합 연산
- SELECT문과 SELECT문 사이에 집합 연산자 정의함
- **두 집합의 컬럼이 동일하게 구성되어야 함!!(데이터 타입과 순서 일치 필요!!)**
- 전체 집합의 데이터타입과 컬럼명은 첫번째 집합에 의해 결정됨

#### 합집합
- 두 집합의 총 합을 출력
- UNION과 UNION ALL

- UNION
  - 중복된 데이터는 한 번만 출 력
  - **중복된 데이터를 제거하기 위해 내부적으로 정렬 수행**
  - **중복된 데이터가 없는경우는 UNION 사용 대신 UNION ALL**사용
    (불필요한 정렬이 발생 할 수 있으므로 비효율적임)

- UNION ALL
  - **중복된 데이터도 전체 출력**
  

    10번 부서 소속이 아닌 직원 정보와 20번 소속 직원 정보가 각각 분리되어 있다고 가정할 때, 두 집합의 합집합
    ```
    SELECT  EMPNO, ENAME, DEPTNO
    FROM    EMP
    WHERE   DEPTNO <> 10
    UNION
    SELECT  EMPNO, ENAME, DEPTNO
    FROM    EMP
    WHERE   DEPTNO = 20;
    ```

### 교집합
- 두 집합 사이에 INTERSECTION
- 두 집합의 교집합(공통으로 있는 행) 출력
    
    ```
    SELECT EMPNO, ENAME, SAL, DEPTNO
    FROM EMP
    WHERE DEPTNO != 10
    INTERSECT
    SELECT EMPNO, ENAME, SAL, DEPTNO
    FROM EMP
    WHERE DEPTNO != 20;
    ```

### 차집합
- 두 집합 사이의 MINUS 전달
- 두 집합의 차집합 출력
- A-B B-A는 다름!
 
    ```
    SELECT EMPNO, ENAME, SAL, DEPTNO
    FROM EMP
    WHERE DEPTNO != 10
    MINUS
    SELECT EMPNO, ENAME, SAL, DEPTNO
    FROM EMP
    WHERE DEPTNO != 20;
    ```

### 주의사항
- 두 집합의 컬럼 수 일치
- 두 집합의 컬럼 순서 일치
- 두 집합의 각 컬럼의 데이터 타입 일치
- 각 컬럼의 사이즈는 달라도 괜찮음
- 개별 SELECT문에 ORDER BY 전달 불가능(GROUP BY 전달 가능)

    에러 표시
    ```
    SELECT  EMPNO, ENAME, DEPTNO
    FROM    EMP
    WHERE   DEPTNO <> 10
    UNION
    ORDER BY SAL
    SELECT  EMPNO, ENAME, DEPTNO
    FROM    EMP
    WHERE   DEPTNO = 20
    ORDER BY SAL;
    ```

    집합연산자 전체 결과에 대해서 ORDER BY절 전달 가능
    ```
    SELECT  EMPNO, ENAME, DEPTNO
    FROM    EMP
    WHERE   DEPTNO <> 10
    UNION
    SELECT  EMPNO, ENAME, DEPTNO
    FROM    EMP
    WHERE   DEPTNO = 20;
    ORDER BY    SAL;
    ```

### 그룹함수
- 숫자함수 중 여러값을 전달하여 하나의 요약값을 출력하는 다중행 함수
- GROUPY BY 절에 의해 그룹별 연산 결과를 리턴 함
- **반드시 한 컬럼만 전달**
- **NULL**은 무시하고 연산

#### COUNT
- 행의 수를 세는 함수
- 대상 컬럼은 *또는 단 하나의 컬럼만 전달이 가능함
- **문자, 숫자, 날짜** 컬럼 모두 전달이 가능함
- 행의 수를 세는 경우 NOT NULL 컬럼을 찾아 세는 것이 좋음(PRIMARY KEY 칼럼)
  
#### SUM
- 총 합 출력
- **숫자** 컬럼만 전달가능

#### AVG
- 평균 출력
- **숫자** 컬럼만 전달가능
- **NULL을 제외한 대상의 평균을 리턴 하므로, 전체 대상 평균 연산 시 주의**

#### MIN, MAX
- 최대, 최소 출력
- **날짜, 숫자, 문자 모두 가능함**(오름차순 순서대로 최소, 최대 출력)
  
#### VARIANCE, STDDEV
- 분산, 표준편차(standard deviation)
- 표준편차 = 분산의 SQRT값

#### GROUP BY FUNCTION
- GROUPY BY절에 사용하는 함수
- **여러 GROUP BY 결과를 동시에 출력(합집합)하는 기능**
- 그룹핑 합 그룹을 정의

    ```
    SELECT  DEPTNO, SUM(SAL)
    FROM    EMP
    GROUP BY DEPTNO;
    ```

##### GROUPING SETS(A, B)   
- A별, B별 그룹 연산의 결과 출력
- 나열 순서 중요X
- 기본 출력에 전체 총계는 출력X
- NULL 혹은 () 사용하여 전체 총 합 출력 가능함!!
 
    ```
    SELECT  DEPTNO, JOB, SUM(SAL)
    FROM    EMP
    GROUPY BY   GROUPING SETS(DEPTNO, JOB);
    ```

    | DEPTNO | JOB | SUM(SAL)|
    |---|---|---|
    ||CLERK|4150|
    ||SALESMAN|5600|
    ||PRESIDENT|5000|
    |30||9400|
    |20||10000|
    |10||8750|

  그러나, UNION ALL로 대체 가능함!!

##### ROLLUP(A, B)
- **A별, (A, B)별, 전체 그룹 연산 결과 출력**
- **나열 대상의 순서가 중요함**
- 기본적으로 **전체 총 계가 출력됨**

    ROLLUP(DEPTNO, JOB) -> DEPTNO 별, (DEPT, JOB) 별, 전체 연산 결과 출력
    (3가지 경우 전부 출력되는 것임)
    ```
    SELECT  DEPTNO, JOB, SUM(SAL)
    FROM    EMP
    GROUP BY    ROLLUP(DEPTNO, JOB);
    ```

    | DEPTNO | JOB | SUM(SAL)|
    |---|---|---|
    |10|CLERK|1300|     - DEPT, JOB 그룹연산
    |10|MANAGER|2400|
    |10|PRESIDENT|5000|
    |10||합산|           - DEPT 그룹연산
    |20|CLERK|1000|
    |20|ANALYST|2000|
    |20|MANNGER|1000|
    |20||4000|          
    |30|CLERK|950|
    |30|MANAGER|2850|
    |30||3800|
    |||합산|             - 전체 총 합 결과


##### CUBE(A, B)
- **A별, B별, (A,B)별, 전체 그룹 연산 결과 출력**
- 그룹으로 묶을 대상의 나열 **순서 중요하지 않음**
- 기본적으로 **전체 총 계가 출력 됨**

- 기본적으로 **전체 총계가 제일 위에 출력됨**
  
- **GROUPING SETS로 대체가 가능함**
    `GROUP BY   GROUPING SETS(DEPTNO, JOB, (DEPTNO, JOB), ());


### 윈도우 함수
- 서로 다른 행의 비교나 연산을 위해 만든 함수
- GROUP BY를 쓰지 않고 그룹 연산 가능함!!!
- LAG, LEAD, SUM, AVG, MIN, MAX, COUNT, RANK
(LAG, LEAD 이전 행의 값을 찾기, 다음 행의 값을 찾기)


- 윈도우 함수의 문법
    ```
    SELECT 윈도우함수([대상]) OVER ([PARTITION BY 컬럼]
                                   [ORDER BY 컬럼 ASC|DESC]
                                   [ROWS|RANGE BETWEEN A AND B]);
    ```
    아래의 순서 중요함!(전달순서 PART BY -> ORD BY -> ROWS)
    - PARTITION BY 절: 출력할 총 데이터 수 변화 없이 그룹연산 수행할 GROUP BY 컬럼
    - ORDER BY 절: 
        - **RANK의 경우 필수**(정렬 컬럼 및 정렬 순서에 따라 순위 변화)
        - SUM, AVG, MIN, MAX, COUNT 등은 누적값 출력 시 사용
    - ROWS|RANGE BETWEEN A AND B
        - 연산 범위 설정
        - **ORDER BY 절 필수**
        - ROWS는 ROWNUM으로 구별(일반적으로 생각하는 그거 맞음)
        - RANGE는 PARTITION BY(BROUP BY)에서 묶은 애들을 하나의 ROW로 고려하는 것임

**전체를 출력하는 컬럼과 그룹함수 결과는 함께 출력할 수 없음**
```
SELECT  EMPNO, ENAME, SAL, DEPTNO, SUM(SAL)
FROM EMP;
>>> 단일 그룹의 그룹 함수가 아닙니다
```

**그룹 함수의 형태**
- SUM, COUNT, AVG, MIN, MAX 등
- **OVER 절을 사용하여 윈도우 함수로 사용 가능**
- 반드시 연산할 대상을 그룹함수의 입력값으로 전달

스칼라 서브쿼리로 해결
```
SELECT EMPNO, ENAME, SAL, DEPTNO,
        (SELECT SUM(SAL) FROM EMP) AS TOTAL
```

윈도우 함수로 해결
```
SELECT EMPNO, ENAME, SAL, DEPTNO,
        SUM(SAL) OVER () AS TOTAL
FROM EMP;
```

##### SUM, AVG, MIN, MAX, COUNT
- 사용방법 동일
```
SELECT EMPNO, ENAME, SAL, DEPTNO,
        SUM(SAL) OVER () AS TOTAL
FROM EMP;
```

```
SELECT EMPNO, ENAME, SAL, DEPTNO,
        MIN(SAL) OVER (PARTITION BY DEPTNO) AS 부서별 급여 총합
FROM EMP;
```


**윈도우 함수의 연산 범위: 집계 연산 시 행의 범위 설정 가능**
1. ROWS | RANGE
   - ROWS: 값이 같더라도 각 행씩 연산
   - RANGE: 같은 값의 경우 하나의 RANGE로 묶어서 동시 연산(DEFAULT임 이게)
     - 그래서, 값이 같은 경우 같은 범위로 취급하여 동시 연산함!!
        ```
        SELECT R.*
                SUM(SAL) OVER (ORDER BY SAL)
        FROM RANGE_TEST R;
        ```

        |EMPNO|ENAME|DEPTNO|SAL|SUM(SAL)OVER(ORDERBYSAL)|
        |---|---|---|---| :---:|
        |7369|스미스|20|800|800|
        |7900|제임스|30|950|1750|
        |7876|아담|20|1100|2850|
        |7521|와드|30|1250|5350|
        |7654|마틴|30|1250|5350|
        |7934|밀러|10|1300|6650|

2. BETWEEN A AND B
   - 시작점 정의
     - CURRENT ROW: 현재행부터
     - UNBOUNDED PRECEDING: 처음부터
     - N PRECEDING: N 이전부터

    - 마지막 시점 정의
      - CURRENT ROW: 현재행까지
      - UNBOUNDED FOLLOWING: 마지막까지
      - N FOLLING: N 이후까지

#### 순위 관련 함수
- RANK
  - RANK WITHIN GROUP
  - **특정값에 대한 순위 확인(RANK WITHIN)**
  - 윈도우가 아닌 일반함수

    ```
    SELECT RANK(값) WITHIN GROUP(ORDER BY 컬럼);
    ```

    급여가 3000 이면 전체 급여 순위가 얼마?
    ```
    SELEECT RANK(3000) WITHIN GROUP(ORDER BY SAL DESC) AS RANK_VALUE
    FROM EMP;

- RANK() OVER()
  - 전체 중/특정 그룹 중 값의 순위 확인
  - ORDER BY절 필수
  - 순위를 구할 대상을 ORDER BY절에 명시(여러 개 OK)
  - 그룹 내 순위를 구할 시 PARTITION BY 절 사용 가능

    ```
    SELECT ENAME, DEPTNO, SAL,
            RANK() OVER(ORDER BY SAL DESC) AS RANK_VALUE1
            FROM EMP;
    ```

- DENSE_RANK
  - 누적순위
  - 값이 같을 때 동일한 순위 부여 후 다음 순위가 바로 이어지는 순위 부여 방식
  - 1등이 5명이더라도 그 다음 순위가 2등

- ROW_NUMBER
- 연속된 행 번호
- 동일한 순위를 인정하지 않고 단순히 순서대로 나열한대로의 순서 값 리턴 

- LAG, LEAD
  - 행 순서대로 각각 이전 값(LAG), 이후 값(LEAD) 가져오기
  - ORDER BY 절 필수

