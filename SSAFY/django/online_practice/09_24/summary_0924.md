## 09/24 정리
- 장고의 경우 에러가 나면 화면을 읽어보는게 좋음

***
### GET vs POST Method
- GET과 POST는 각각의 특성에 맞게 사용하기
- GET: 데이터 조회를 위함
- POST: 데이터 생성 or 수정을 위함

***
#### GET Method 특징
- 사용예시
  1. 검색 쿼리 전송
  2. 웹 페이지 요청
  3. API에서 데이터 조회

- 특징
  1. 데이터 전송
     - URL의 쿼리 문자열을 통해 데이터를 전송
     - http://127.0.0.1:8000/articles/create?title=제목&content=내용
     - ? 이후는 검색에 관한 파트
  2. 데이터 제한
     - URL 길이에 제한이 있어 대량 데이터 전송에는 적합하지 않음
  3. 브라우저 히스토리(기록 남음)
  4. 캐싱
     - (브라우저는 GET의 요청 응답을 로컬에 저장 가능)
     - (동일 URL 요청시, 서버접속 X 기존결과 활용)
     - 페이지 로딩 시간을 크게 단축


***
#### POST Method
- 사용예시
  1. 로그인 정보 제출
  2. 파일 업로드
  3. 새 데이터 생성(ex. 새 게시글 작성)
  4. API에서 데이터 변경 요청
  
- 특징
  1. 서버에 데이터를 전송할 때, URL을 전송하지 않음
    - HTTP BODY를 통해 데이터를 전송
  2. GET보다 더 많은 양의 데이터 전송가능
  3. POST 요청은 브라우저 히스토리에 안남음
  4. 캐싱
    - (POST 요청은 기본적으로 캐싱 불가능)
    - (POST는 일반적으로 서버의 상태 변경을 요청하기 때문)


***
#### POST의 사용
- POST 사용시, GET만 POST로 바꾼 정도의 차이임


#### 403 Forbiddent
- 서버에 요청이 전달되었지만, 권한 때문에 거절되었다는 것을 의미함

- **CSRF**(사이트간 요청위조)
  - 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 
    보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법

  - 읽어보기
    - https://www.cloudflare.com/ko-kr/learning/security/threats/cross-site-request-forgery/
    - https://www.imperva.com/learn/application-security/csrf-cross-site-request-forgery/

- **CSRF Token**
  - 토큰을 사용하여 CSRF공격을 막을 수 있음.
  - 자기가 만든 페이지라는 것을 확인하기 위함.
  - **POST방식에서만 필요함 GET은 아님. 왜?**
  - form 사이에 `{% csrf_token %}`를 넣어주면 됨
    - 새로 고침시마다 매번 값이 달라짐(개발자도구에서 확인이 가능)
  - 장고가 직접 제공한 페이지에서 데이터를 작성하고 있는 것인지에 대한 확인 수단으로 사용

  - **왜 POSt일 때만 Token을 확인할까** 
    - DB에 대한 변경사항을 만드는 요청이기 때문에 토큰을 사용해 최소한의 신원 확인을 하는 것
    1. POSt는 단순 조회를 위한 GET과 달리 특정 리소스에 변경(CUD)을 요구하는 의미와 기술적 부분이 있음
    2. DB에 조작을 가하는 요청은 반드시 인증 수단이 필요
    

***
#### HTTP response status code
- 서버가 클라이언트의 요청에 대한 처리 결과를 나타내는 3자리 숫자
- HTTP response status codes를 구글에 치면 **5가지** 타입이 있음을 알 수 있음.
  - 1xx
  - 2xx(성공에 관련함)
  - 3xx
  - 4xx(클라이언트의 잘못에 관함)
  - 5xx(서버의 잘못에 관함)

- **403**: 서버에 요청은 전달되었으나, **권한** 때문에 거절되었다는 것을 의미
- **404**: 주소에 해당하는 데이터가 없음을 의미


#### Redirect
- 서버는 데이터 저장 후 페이지를 응답하는 것이 아닌,    
    사용자를 적절한 기존 페이지로 보내야 함.

    - 사용자를 보낸다. $\rightarrow$ 사용자가 GET요청을 한번 더 보내도록 해야 함.
      - **실제로 사용자를 보내는 것이 아님!**
    - 실제로 서버가 클라이언트를 직접 다른 페이지로 보내는 것이 아니라  
        클라이언트가 GET요청을 한번 더 보내도록 응답하는 것

- **redirect()**
  - 클라이언트 인자에 작성된 주소로 다시 요청을 보내도록 하는 함수
  - `from django.shortcuts import redirect`을 통해 사용 가능함 
  - `render`대신 사용하면 됨

  - 동작원리
    1. Client - POST(게시글 작성 요청 + 입력 데이터)
    2. django - create view 함수 호출
    3. django - redirect 응답. detail 주소로 요청을 보내라
    4. Client - GET(detail 페이지 요청)
    5. django - detail view 함수 호출
    6. django - detail 페이지 응답


***
#### Delete
- variable outting이 필요함
  - 왜?: **삭제/수정 전에 조회를 먼저 해야하기 때문**

