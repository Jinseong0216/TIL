## 11/11 라이브 강의 정리
### Routing
- 네트워크에서 경로를 선택하는 프로세스
- Client -> Server --HTML--> Client 

- CSR에서의 라우팅
  - CSR에서 라우팅은 클라이언트 측에서 수행
  - Client --최초요청--> Server --HTML--> Client --AJAX--> Server --JSON--> Client

- SPA에서 라우팅이 없다면
  - 유저가 URL을 통한 페이지의 변화를 감지할 수 없음
  - 페이지가 뭘 렌더링 중인지 알 수 없음
  - 브라우저의 뒤로  가기 기능 사용 불가능
  - 페이지는 1개이지만, 주소에 따라 여러 컴포넌트를 새로 렌더링하여 마치 여러 페이지를 사용하는 것처럼 보이도록 해야 함

  ### Vue Router
  - Vue 공식 라우터
  - npm create ... 에서 VueRouter파트를 그냥 Yes로 하면 됨
  - 라우터링크를 바꿔주는 원리임
  - 라우터링크에 연결이 되서 라우터링크의 주소에 따라서 렌더링 되는것(그러나 여전히 페이지는 하나임)

  그 결과 Vue 프로젝트 구조가 변화함
  1. App.vue 코드 견화
  2. router 폴더 신규 생성
  3. views 폴더 신규 생성

- 적용방법
  1. script에서 RouterLink와 RouterView를 vue-router로부터 불러옴
  2. template에서 <RouterLink to=""></RouterLink>를 넣어서 사용함
  3. 나타나길 원하는 위치에 <RouterView />가 있어야함

  #### RouterLink
  - HTMl의 a태그를 렌더링 하는 것임
  
  #### RouterView
  - 라우터링크 URL에 해당하는 컴포넌트를 표시(원하는 위치에 넣으면 되는 것임)

  #### router/index.js
  - Django에서의 urls.py와 같은 역할을 함

  #### Views/
  - 라우터뷰 위치에 렌더링 할 컴포넌트를 배치
  - 기존 컴포넌트 폴더와 기능적으로 다른 것은 없지만, 분류의 의미로 구성됨
  - 일반 컴포넌트와 구분하기 위해, 컴포넌트 이름을 View로 끝나도록 작성하는 것을 권장

  #### 라우팅 기본
  1. index.js에 라우터 관련 설정 작성(주소, 이름, 컴포넌트)
    - 이름이 필수 인자는 아니지만, 작성하는 것이 좋음
  2. 라우터링크의 to 속성으로 index.js에서 정의한 주소(path) 값을 사용
  3. 라우터링크 클릭 시 경로와 일치하는 컴포넌트가 라우터뷰에서 렌더링 되도록 함

  #### Named Routes
  - name 속성 값에 경로에 대한 이름을 지정
  - 경로에 연결하려면 라우터링크에 v-bind를 사용해 to props 객체로 전달
```html
<template>
<RouterLink :to={ name: 'home'}>Home</RouterLink>
</template>
```
  - 이를 통해서 하드 코딩된 URL을 안쓸 수 있음.

#### 매개변수를 사용한 동적 경로 매칭(Dynamic Route Matching)
- URL의 일부를 변수로 사용하여 경로를 동적으로 매핑
- Views폴더 내에서 Userview 컴포넌트 작성
- index.js에서, path가 '/user/:id'였다면
  - view컴포넌트에서 `<라우터링크 :to"{ name: 'user', params: {id: 1}}"User</라우터링크>`와 같은 형태로 사용이 가능함
  - id에 1 대신에 ref 객체를 넣어도 됨
  - 이후에, UserView라는 vue파일 내부에서, `{{ $route.params.id }}`와 같은 형태로도 접근할 수 있음... 그러나 좋은 방법은 아니긴함(route라는 객체에 정보가 담긴다는 것만 알면 됨)
  - script에서 useRoute를 vue-router로부터 불러온 후 const route = useRoute()를 정의 한다음 const UserId = ref(route.params.id)와 같은 형태로 사용하는 것이 권장됨!!!!!


#### Nested Routing(중첩된 라우팅)
- 앱의 UI는 여러 레벨 깊이로 중첩된 컴포넌트로 구성되기도 함
- 이 경우, URL을 중첩된 컴포넌트의 구조에 따라 변경되도록 이 관계를 표현할 수 있음
- children 옵션을 사용하여 중첩된 라우터에 컴포넌트를 등록(index.js에서 path name component가 있던 객체에 children을 만드는 것)
- {..., component: UserView, children: [ {path: ..., name: ..., component: ...}, {path: ..., name: ..., component: ...}, {path: ..., name: ..., component: ...}]}

- 첫 페이지에서 바로 표현하고 싶으면
- {name<--제거, component: UserView, children: [ {path: '공백', name: '상위이름user 넣고', component: 첫페이지해당컴포넌트}, ...]}를 추가해주면 됨

- **주의사항**
  - 컴포넌트칸 부모-자식 관계 관점이 아니라 URL에서의 중첩된 관계를 표현하는 관점으로 보기

### Programmatic Navigation
- 라우터링크 대신 자바스크립트를 사용하여 페이지를 이동하는 것
- 프로그래밍으로 URL이동하기
- 라우터의 인스턴스 메서드를 사용하여 라우터링크의 a태그를 만드는 것처럼 프로그래밍으로 네비게이션 관련 작업을 수행할 수 있음

#### 라우터의 메서드
1. router.push(): 다른 위치로 이동하기
  - 뒤로가기 가능함
  - 새 항목을 history stack에 push하므로 사용자가 브랑줘 뒤로 가기 버튼을 클릭하면 이전 URL로 이동할 수 있음
```html
<template>
  <button @click="goHome">홈으로!</button>
</template>

<script>
  import { userRouter } from 'vue-router'
  const router = useRouter()
  const goHome = function() {
    router.push({ name: 'home'})
  }
  // push안에 {name: ..., params: { username: 'alice'}} 이런식도 가능하고
  // { path: '/register', query: {plane: 'private'}} 이런 걸 넣을수도 있음
</script>
```
2. rotuer.replace(): 현재 위치 바꾸기
  - 뒤로가기 불가능
  -  사용방법은 동일

#### Navigation Guard
- 뷰 라우터를 통해 특정 URL에 접근할 때, 다른 URL로 redirect를 하거나 취소하여 내비게이션을 보호
- 라우트 전환 전/후 자동으로 실행되는 Hook
- 모든 가드는 2개의 인자를 받음
  1. to: 이동할 URL 정보가 담긴 Route객체
  2. from: 햔재 URl 정보가 담긴 Route 객체
- return
  1. false: 현재 내비게이션을 취소, 브라우저 URL이 변경된 경우(사용자가 수동으로 또는 뒤로가기 버튼을 통해) from 경로의 URL로 설정
  2. 라우트 Location: `return { name: 'About'}`, router.push()를 호출하는 것처럼 경로 위치를 전달하여 다른 위치로 redirect, return이 없다면 자동으로 to에 해당하는
- 종류
  1. Globally(전역 가드)
    - 앱 전역에서 모든 라우트 전환에 적용되는 가드
    - 작성위치, index.js
    - beforeEach(): 다른 URL로 이동하기 직전에 실행되는 함수
  2. Per-route(라우터 가드)
    - 특정 라우트에만 적용되는 가드
  3. In-component(컴포넌트 가드)
    - 컴포넌트 내에서만 적용되는 가드