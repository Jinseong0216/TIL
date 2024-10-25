### 10/24 라이브강의 정리

#### Tips
1. 
```js
user = {
    name : 'JavaScript',
    'key with space': true
}

console.log(user.'key with space') // 에러발생
console.log(user['key with space']) // 가능
```

2.
    - 단순 호출시의 this는 window를 가리킴
    - 메서드 호출시의 this는 해당 객체
    - 주의
```js
const myObj2 = {
    numbers: [1, 2, 3],
    myFunc: function () {
        this.numbers.forEach(function (number) {
            console.log(this) // window를 가리키게 됨... 
        })
    }
}

const myObj3 = {
    numbers: [1, 2, 3],
    myFunc: function () {
        this.numbers.forEach( (number) = > {
            console.log(this) // myObj3를 가리킴
        }

        )
    }
}
```