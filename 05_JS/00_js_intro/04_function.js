/*
// Function

// 선언식
function add(num1, num2){
  return num1 + num2
}

console.log(add(2, 7))

// 표현식 || 객체는 전부 변수에 담을 수 있기 때문에 아래 표현식이 가능하다
const sub = function(num1, num2){
  return num1 - num2
}

console.log(sub(7,2))

// JS 에서는 함수도 하나의 값!! --- function 을 사용해 함수를 정의
console.log(typeof add) // function
console.log(typeof sub) // function


//Arrow function(화살표 함수)
// why arrow function?
// 화살표 함수는 항상 익명 함수
//1. function keyword 생략 가능
//2. 함수의 매개변수가 1개라면 () 생략가능
//3. 함수 바디의 표현식이 하나라면 {} 와 return 생략 가능

// 함수 표현식
const ssafy1 = function(){
  return 'Hello'
}
console.log(ssafy1())


//화살표 함수로 바꿔보기
//1. function 키워드를 삭제할 수 있음!
const ssafy1 = (name) => { return 'Hello! ${name}'}
console.log(ssafy1(`phin`))


//2/ () 생략할 수 있다! (인자가 1개 있을 때)
const ssafy1 = name => {return `Hello! ${name}`}
console.log(ssafy1('Phin'))


//3. {}와 return 생략
const ssafy1 = name => `Hello! ${name}`
console.log(ssafy1('Phin'))


let square = function(num){
  return num ** 2
}


//1. function 키워드 삭제
square = (num) => { return num ** 2}
//2. 인자 1개 일 () 삭제
square = num => { return num ** 2}
//3. {}와 return 을 삭제
square = num => num ** 2
console.log(square(2))


//4. 인자가 없을 때 -> (), _표현 가능
let noArgs = () => 'No args'
console.log(noArgs())

noArgs = _ => 'No args'
console.log(noArgs())


// 5-1. object 리턴하려고 한다면 -> return 을 명시적으로!
let returnObject = () => { return {key: 'value'}}
console.log(returnObject())
console.log(typeof returnObject())

// 5-2 return을 적지않고 object를 return 하고 싶다면 ()를 활용
returnObject = () => ({ key: 'value' })
console.log(returnObject())
console.log(typeof returnObject()) //object

// 5-3 return 문을 적지 않았을 때 // 함수의 문으로 판단함
returnObject = () => { key: 'value'}
console.log(returnObject())
console.log(typeof returnObject())

function () {
  key: 'value'
}


// 기본 인자를 줄 때는 인자 개수와 상관없이 괄호를 꼭 해야 한다.
// 괄호가 없으면 syntax error 발생
const sayHello = (name='noName') => `hi ${name}`

console.log(sayHello('Phin'))
console.log(sayHello())


// 익명 함수/ 1회용 함수
// 즉시 실행 함수는 초기화에 많이 사용된다.

function(num) { return num ** 3}

//1. 기명함수로 먼저 만들어보자!
const cube = function(num) { return num ** 3} // 8
const squareRoot = num => num ** 0.5 

console.log(cube(2))
console.log(squareRoot(4))

//2. 즉시실행함수 -> 주로, 초기화에 많이 사용
console.log((function (num) { return num ** 3 })(2))
console.log((num => num ** 0.5)(4)) //2


// 함수 호이스팅

sasfy()

function sasfy(){
  console.log('hoisting!')
}


ssafy2()

let ssafy2 = function() {
  console.log('hoisting!')
}

// JS 엔진이 코드를 해석하는 과정
let ssafy2 //1. 변수 선언 -> let은 var와 다르게 초기화가 동시에 진행되지 않음!

ssafy2() //2. 함수 호출 -> ssafy2가 초기화 안됌 (현재 TDZ 상태)

ssafy2 = function(){
  console.log('hoisting!')
} //3. 변수에 할당

ssafy3()

var ssafy3 = function(){
  console.log('hoisting!')
}

// JS 엔진이 코드를 해석하는 과정

var ssafy3 //1. 변수 호이스팅(선언 + 초기화)

ssafy3() //2. 함수 호출 -> let과 다르게 초기값 undefined가 들어감.
// 함수 호출하는 시점에서 ssafy3라는 변수에는 함수가 아닌 undefined 가 들어 있기 때문에
// 함수 아닌딩 이라는 에러 메시지를 보냄!

ssafy3 = function(){
  console.log('hoisting!')
}
*/
