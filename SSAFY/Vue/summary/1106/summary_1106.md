  - 뷰의 시작
```vue
<template>
  <div class="greeting">
    {{  }}
  </div>
</template>

<!-- setup함수의 구조적 변경!!!! -->
<!-- 이제는 셋업을 편하게 할 수 있음 -->
<!-- 심지어 리턴도 안해도 됨 -->
<script setup>
import { ref } from 'vue'

const msg = ref('hello')
</script>

<!-- css는 똑같이 쓰면 됨 -->
<!-- scoped는 뭘까? -->
<!-- 동작 범위를 설정하기 위함 -->
<!-- 즉, 여기에서만 아래의 css가 적용되게 하기 위함 -->
<style lang="scss" scoped>
.greeting {
  color: red;
}
</style>
```


- SFC 구성요소

  각 뷰 파일은 세가지 유형의 최상위 언어 블록
  template script style로 구성됨

  언어 블록의 작성 순서는 상고나 없으나 일반적으로
  template script style 순서로 작성함

- template block

  각 뷰 파일은 최상의 temp 블록을 하나만 포함 가능함

- script setup block

  각 뷰 파일은 하나의 script setup 블록을 포함 할 수 있음
  (일반 script block은 여러개 가질 수 있음)

m- style scoped 블록

  뷰 파일에는 여러 style 태그가 포함될 수 있음
  scoped가 지정되면 css는 현재 컴포넌트에만 적용됨

- 컴포넌트 사용하기

  [https://play.vuejs.org/] 에서 실행 밑 미리보기 가능함
  뷰 SFC는 컴파일러는 통해 컴파일 된 후, 빌드 되어야 함

- **Vite**

  프론트엔드 개발 도구
  빠른 개발 환경을 위한 빌드 도구와 개발 서버를 제공
  https://vitejs.dev/

- **Build**

  프로젝트의 소스코드를 최적화하고 번들링하여 배포할 수 있는 형식으로 변환하는 과정
  개발 중에 사용되는 여러 소스 파일 및 리소스를 최적화된 형태로 조합하여 최종 소프트웨어 제품을 생성하는 것

  비트는 이러한 빌드 프로세스를 수행하는 데 사용되는 도구

- **Component**

  컴포넌트는 **재사용 가능한 코드 블록**임을 항상 인지!!

#### **뷰 프로젝트**
1. 뷰의 최신 프로젝트 생성하기
```bash
$ npm create vue@latest
```
- 이후 엔터를 누르면 기본 이름 쓴다는 것
- 기능에 따라서 NO/YES를 선택하면 됨

2. cd vue-project
  - npm install
    - 새로운 파일들이 생김
      - node_modules
      - package-lock.json
  - 이제부터 서버 실행가능
    - npm run dev
    - 사용하는 포트 번호가 다름(local 호스트 5173)
    - src 디렉토리의 component을 열어보면 우리가 보았던 기본 페이지의 컴포넌트들이 보이게 됨!


#### NPM(Node Package Manger)
- Node.js의 기본 패키지 관리자(파이썬에서의 PIP)

#### Node.js
- 크롬의 V8 JS 엔진을 기반으로하는 Server-Side 실행 환경

- 기존에 브라우저 안에서만 동작할 수 있었던 JavaScript를 브라우저가 아닌 서버 측에서도 실행할 수 있게 함
  - 프론트엔드와 백엔드에서 동일한 언어로 개발할 수 있게 됨

- NPM을 활용해 수많은 오픈 소스 패키지와 라이브러리를 제공하여 개발자들이 손쉽게 코드를 공유하고 재사용할 수 있게 함

- **Module**: 프로그램을 구성하는 독립적은 코드 블록(*.js 파일)
  - 필요성: 개발하는 app의 크기가 커지고 복잡해지면서, 파일 하나에 모든 기능을 담기 어려움
  - 자연스럽게 파일을 여러 개로 분리하여 관리하게 됨
  - *.js 파일 하나가 하나의 모듈

  - **한계**
    - app이 점점 발전함에 따라, 처리해야하는 JS모듈의 개수가 너무 많아짐
    - 그 결과, 병목이 발생하고 모듈간의 의존성이 깊어지면서, 문제 발생시 어떤 모듈간의 문제인지 파악하기가 어려워 짐
    - 복잡하고 깊은 모듈 간의 의존성 문제를 해결하기 위한 도구가 필요함

- **Bundler**: 여러 모듈과 파일을 하나(혹은 여러개)의 번들로 묶어 최적화하여 app에서 사용할 수 있게 만들어주는 도구
  - 역할: 의존성 관리, 코드 최적화, 리소스 관리
  - Bundler가 하는 작업을 번들링이라 함
  - Vite는 Rollup이라는 Bundler를 사용하며 개발자가 별도로 기타 환경설정에 신경 쓰지 않도록 모두 설정해두고 있음

- **node_modules**
  - 노드js 프로젝트에서 사용되는 외부 패키지들이 저장되는 디렉토리
  - 프로젝트의 의존성 모듈을 저장하고 관리하는 공간
  - 프로젝트가 실행될 때 필요한 라이브러리와 패키지들을 포함
  - .gitnore에 작성이되는 부분임
    - 대신, pakce-lock.json, package.json을 통해서 버전을 맞춤

- **package-lock.json**
  - 패키지들의 실제 설치 버전, 의존성 관계, 하위 패키지들을 포함하여 패키지 설치에 필요한 모든 정보를 포함
  - 패키지들의 정확한 버전을 보장하여, 여러 개발자가 협업하거나 서버 환경에서 일관성 있는 의존성을 유지하는 데 도움을 줌
  - npm install 명령을 통해 패키지를 설치할 때, 명시도니 버전과 의존성을 기반으로 설치
  - 수정 할 필요 없음

- **package.json**
  - 프로젝트의 메타 정보와 의존성 패키지 목록을 포함
  - 프로젝트의 이름, 버전, 작성자, 라이선스 등과 같은 메타 정보를 정의
  - package-lock.json과 함께 프로젝트의 의존성을 관리하고 버전 충돌 및 일관성을 유지하는 역할
  - 수정 할 필요 없음

- **publci 디렉토리**
  - 주로 다음 정적 파일을 위치 시킴
    - 소스코드에서 참조되지 않은
    - 항상 같은 이름을 같는
    - import 할 필요 없음
  - 항상 root **절대 경로**를 사용하여 참조
    - public/icon.png는 소스 코드에서 /icon.png로 참조 할 수 있음

- **src 디렉토리**
  - 프로젝트의 주요 소스코드를 포함하는 곳
  - 컴포넌트, 스타일, 라우팅 등 프로젝트의 핵심 코드를 관리

- **src/assets**
  - 프로젝트 내에서 사용되는 자원(이미지, 폰트, 스타일 시트 등)을 관리
  - 컴포넌트 자체체서 참조하는 내부 파일을 저장하는데 사용
  - 컴포넌트가 아닌 곳에서는 public 디렉토리에 위치한 파일을 사용

- **src/componets**: Vue 컴포넌트들을 작성하는 곳

- **src/App.vue**
  - 뷰 앱의 최상위 컴포넌트
  - 다른 하위 컴포넌트들을 포함
  - 앱 전체의 레이아웃과 공통적인 요소를 정의

- **src/main.js**
  - 뷰 인스턴스를 생성하고, 앱을 초기화하는 역할
  - 필요한 라이브러리를 import 하고, 전역 설정을 수행

- **index.html**
  - 뷰 앱의 기본 HTML 파일
  - 앱의 진입점
  - **루트 컴포넌트인 앱.vue가 해당 페이지에 마운트 되는 것임(뷰 앱이 SPA인 이유!!!)**
  - 필요한 스타일 시트, 스크림트 등의 외부 리소스를 로드 할 수 있음(bootstrap CDN)

- **기타 설정 파일**
  - jsconfig.json: 컴파일 옵션, 모듈 시스템 등 설정
  - vite.config.js: 뷰 프로젝트 설정 파일 / 플러그인, 빌드 옵션, 개발 서버 설정 등

#### 컴포넌트 사용 2단계
1. 컴포넌트 파일 생성
2. 컴포넌트 등록(import)

실습 ex ================================================
- 1. App.vue 세팅
- 2. 컴포넌트 내부에 MyComponent.vue 만들기

```Vue
<template>
  <h1>App.vue</h1>
  <!-- Step 2. -->
  <MyComponent />
</template>

<script setup>
//  Step 1.
// import MyComponent from './components/MyComponent.vue' 혹은 아래를 씀
// @를 쓰는 것이 더 권장(src를 의미함)
import MyComponent from '@/components/MyComponent.vue'

</script>

<style scoped>

</style>
```

- 추가 하위 컴포넌트 등록 후 활용
```Vue
<!-- MyComponent.vue -->
<template>
  <h1>MyComponent</h1>
  <MyComponentItem />
</template>

<script setup>
import MyComponentItem from './MyComponentItem.vue'
</script>

<style scoped>

</style>


<!-- 위와 아래의 두 vue파일은 componets폴더 안에 있음 -->


<!-- MyComponentItem.vue -->
 <template>
  <p>MyComponentItem</p>
 </template>
 
 <script setup>
 
 </script>
 
 <style scoped>
 
 </style>
```

- **권고**: 
  1. 컴포넌트의 최상위 블록은 하나만 두는 것이 좋음
  2. 싱글 파일 컴포넌트의 파일명: 파스칼 케이스(제일 좋음, 자동완성으로 인함), 케밥 케이스 
  3. 기본 컴포넌트 이름: 앱별 스타일, 규칙을 적용하는 컴포넌트는 접두사를 붙어야 함. ex) Base, App, V 사용
  4. 부모자식의 관계는, 부모 컴포넌트의 이름을 자식 컴포넌트 이름의 접두사로 사용함
    - TodoList.vue
      -TodoListItem.vue
        - TodoListItemButton.vue
  5. 컴포넌트 이름은, 일반적인 단어로 사용해야 함
    - SearchButtonClear.vue
    - SearchButtonRun.Vue
    - SearchInputQuery.vue
    - SettingCheckTerms.vue

#### Virtual Dom
- 가상의 DOM을 메모리에 저장하고 실제 DOM과 동기화하는 프로그래밍 개념
- 실제 DOM과의 변경 사항 비교를 통해 변경된 부분만 실제 DOM에 적용하는 방식
- 웹 app의 성능을 향샹시키기 위한 Vue의 내부 렌더링 기술

- 가상 DOM의 일부를 바꾸면 실제 DOM에 마운트 해버리는 느낌

- 템플릿 -> 렌더함수코드 -> 가상 DOM 트리 -> 실제 DOM
- 동시에:   렌더함수코드 <-> 컴포넌트 반응형 상태 

- 뷰를 쓸때 실제 DOM을 선태갛지 않음

- **주의 사항**
  - 실제 DOM에 접근하지 말것 
    - ex. querySelector, createElement, addEventListener 등 
  - 뷰의 ref와 Lifecycle Hooks 함수를 사용해 간접적을 접근하여 조작할 것

  - 직접 DOM 엘레먼트에 접근해야 하는 경우 
  ```vue
  <template>
    <input ref="input">
  </template>

  <script setup>
  import {ref, onMounted} from 'vue'
  // 변수명은 템플릿 ref 값과 일치해야 함
  const input = ref(null)

  onMounted(() => {
    console.log(input.value) // <input>
  })
  </script>
```
  - 여기에서 const input를 통해 null을 만든 것이 아니라 <input ref="input">을 선택한 것임을 명시하자

- Vue를 작성하는 2가지 스타일
  - Composition APi vs Option APi
  - Vue3에서는 둘 모두 지원
  - ** 뷰3에서는 Composition API를 사용하는 걸 지양함  **

  - Composition API: import 해온 APi 함수들을 사용하여 컴포넌트의 로직을  정의
  - Option API: data, methods 및 mounted 같은 객체를 사용하여 컴포넌트의 로직을 정의(Vue2에서의 작성 방식)

  - API별 권장 사항
    - Composition APi + SFC: 규모가 있는 앱의 전체를 구축하려는 경우
    - Option API: 빌드 도구를 사용하지 않거나 복잡성이 낮은 프로젝트에서 사용하려는 경우

- **모든 컴포넌트에서는 최상단 HTML 요소가 작성되는 것이 권장**
  - 가독성, 스타일링, 명확한 컴포넌트 구조를 위해 각 컴포넌트에서는 최상단 HTML 요소를 작성해야 함(Single Root Element)

- **SFC의 CSS 기능 - scoped**
  - scoped 속성을 사용하면 해당 CSS는 현재 컴포넌트의 요소에만 적용됨
    - 부모 컴포넌트의 스타일이 자식 컴포넌트로 유출되지 않음
    - 사용하지 않으면 모든 컴포넌트에 영향을 미침

  - 그러나 자식 컴포넌트의 최상위 요소는 부모 CSS와 본인 CSS 모두에게서 영향을 받음
    - 자식 컴포넌트의 최상위 요소는 부모에서 사용되기 때문
  
  - 이는 부모가 레이아웃 목적으로 자식 컴포넌트 최상위 요소의 스타일을 지정할 수 있도록 의도적으로 설계한 것

  - 다음과 같이 App 컴포넌트에 적용한 스타일에 scoped가 작성 되어 있지만, MyComponent의 최상위 요소는 부모와 본인의 CSS 모두의 영향을 받기 때문임

  - scoped 속성 사용을 권장
    - 최상위 App 컴포넌트에서 레이아웃 스타일을 전역적으로 구성할 수 있지만, 다른 모든 컴포넌트는 범위가 지정된 스타일을 사용하는 것을 권장

- **Scaffolding(스캐폴딩)**
  - 새로운 프로젝트나 모듈을 시작하기 위해 초기 구조와 기본 코드를 자동으로 생성하는 과정
  - 개발자들이 프로젝트를 시작하는 데 도움을 주는 틀이나 기반을 제공하는 작업
  - 초기 설정, 폴더 구조, 파일 템플릿, 기본 코드 등을 자동으로 생성하여 개발자가 시작할 때 시간곽 노력을 절약하고 일관된 구조를 유지할 수 있도록 도와줌.


