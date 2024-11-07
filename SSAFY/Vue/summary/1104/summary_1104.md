### Vue

#### Template Syntax
1. Text Interpolation
  - 콧수염 구문
2. Raw HTMl
  - 콧수염 구문은 데이터를 일반 텍스트로 해석,
  - 실제 HTML을 출력하려면 v-html을 써야함 `v-html="rawHtml"`
3. Attribute Bindings
  - 콧수염 구문은 HTML 속성 내에서 사용할 수 없기 때문에 v-bind를 사용하여야 함
  - HTML id 속성 값을 vue의 dynamicId 속성과 동기화
  - 바인딩 값이 null undefind면 렌더링 요소에서 제거됨

4. JavaScript Expressions
  - 제어문은 삼항 표현식을 사용해야 함
  - 각 바인딩에는 하나의 단일 표현식만 포함 될수 있음


- Directive의 특징
  - 단일 javascript의 표현식이어야 함(v-for, v-on 제외)
  - 표현식의 값이 변경될 때 DOM에 반응적을 업데이트 적용
  ```js
  <p v-if="seen">Hi There</p>
  ```

  ```js
    <!-- 조건? 에 대한 -->
    <p v-if="seen">Hi there</p>
    <!-- 속성에 대한 bind -->
    <a v-bind:href="myUrl">Link</a>
```

- Directive 전체 구문
  - v-on: submit.prevent="onSubmit"
  - name: Argument.Modifiers="Value"

  - Arguments
    - 일부 directive는 뒤에 :으로 표시되는 인자를 사용 할 수있음

  - Modifier
    - .로 표시되는 특수 접미사로 directive가 틀별한 방식으로 바인딩되어야 함을 나타냄
    - 아래 예시의 .prevent는 발생한 event.preventDefault()를 호출하도록 v-on에 지시하는 modifier
```js
<form v-on:submit.prevent="onSubmit">
  <input type="submit">
</form>
```


#### Dynamically data binding
##### v-bind
- v-bind: 하나 이상의 속성 또는 컴포넌트 데이터를 표현식에 동적으로 바인딩
- 사용처: 속성 연결, 클래스 연결, 스타일 연결

- 속성 바인딩
  ```js
  <img v-bind:src="imageSrc">
  <a v-bind:href="myUrl">Move to url</a>
  {/* 생략도 가능함 */}
  <img :src="imageSrc">
  <a :href="myUrl">Move to url</a>
```

- 동적으로 속성 바인딩
  - 대괄호[]로 감싸서 directive argument에 표현식을 사용할 수 있음
  - 표현식에 따라 동적으로 평가된 값이 최종
  - 대괄호 안에 작성하는 이름은 반드시 소문자로만 구성 가능(브라우저가 속성이름을 소문자로 강제변환함)
  ```js
  <p :[dynamicattr]="dynamicValue">Dynamic Attr</p>
  ```

- Class and Style Bindings
  - class와 style은 모두 HTML 속성이므로 다른 속성과 마찬가지로 v-bind를 사용하여 동적으로 문자열 값을 할당가능
  - Vue는 class및 style속성 값을 v-bind로 사용할 때, 객체 또는 배열을 활용하여 작성할 수 있도록 함

  - Binding HTML Classes
    1. Binding to Objects
    ```js
    <!-- 아래의 두개는 같은 결과 -->
    <div class="active">Text</div>
    <div :class="{active: isActive}">Text</div>    

    <div class="static" :class="{active: isActive, 'text-primary': hasInfo}">Text</div>    
    ```
    2. Binding to Arrays
    ```js
    <!-- 배열의 값으로 넣음 -->
    <div :class="[activeClass, infoClass]">Text</div>
    <!-- 배열의 값으로 객체를 넣음 -->
    <div :class="[{ active: isActive}, infoClass]">Text</div>
    <div class="static" :class="classObj">Text</div>
    ```

  - Binding Inline Styles
    1. Binding to Objects
    ```js
    <div style="color: crimson; font-size: 50px;">Text</div>
    <!-- 바인딩 적용 -->
    <div :style="{ color: activeColor, fonSize: fonSize + 'px'}">Text</div>
    <div :style="{ color: activeColor, 'font-size': fonSize + 'px'}">Text</div>
    ```
    2. Binding to Arrays
    ```js
    <div :style=styleObj>Text</div>

    <!-- ... -->
    <!-- ... -->
        const styObj = ref({
          color: activeColor,
          fontSize: fontSize.value + "px"
        })

        const styObj2 = ref({
          color: "blue",
          border: "1px solid black"
        })
        return {
          activeColor,
          fonSize,
          styObj,
          styObj2
        }}
    ```


#### Event Handling

##### v-on
- DOM 요소에 이벤트 리스너를 연결 및 수신
- v-on:submit.prevent="onSubmnit"
- Name:Argument.modifier = value

1. Inline handler: 이벤트가 트리거가 될 떄 실행 될 JS코드
  - 주로 간단환 상황에서 사용
2. Method handler: 컴포넌트에 정의된 메서드 이름

**약어**:
```JS
<div v-on:event="handler"></div>
<div @event="handler"></div>
``` 
$ <<< 붙은 변수 ex. $event는 변수로 만든 이벤트가 아니라
내장되어있는 글로벌 변수임

- Event Modifiers
  - 이를 활용해 event.preventDefault()와 같은 구문을 메서드에서 작성하지 않도록 함
  - stop, prevent, self등 다양한 modifiers 제공함
  - modifer의 경우 chained가 될 수 있으므로, 순서에 유의해야 함

- Key Modifiers
  - 키보드 이벤트를 수신할 때특정 키에 관한 별도 modifier을 사용할 수 있음
  - ex. `<input @keyup.enter="onSubmit">`


#### Form Input Bindings
- form을 처리할 때 사용자가 input에 입력하는 값을 실사간으로 JS에 상태에 동기화해야 하는 경우(양방향 바인딩)

- 양방향 바인딩 방법
  1. v-bind v-on을 함께 사용
  2. v-model 사용


```javascript
/*주석
주석*/
```