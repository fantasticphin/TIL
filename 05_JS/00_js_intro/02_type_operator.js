// primitive(원시)타입

/*
const a = 13
const b = -5
const c = 3.14
const d = 2.99e8 // 10^8
const e = Infinity
const f = -Infinity
const g = NaN // Not a Number
console.log(a,b,c,d,e,f,g)


//string
const sentence1 = 'Ask and go to the blue' // single
const sentence2 = "Ask and go to the blue" // double
const sentence3 = `Ask and go to the blue` // backtick
console.log(sentence1)
console.log(sentence2)
console.log(sentence3)

// 따옴표를 사용하면 줄바꿈 불가 -> 백틱 사용 // 혹은 이스케이프 문 /n 사용
const word = "안녕
하세요"
console.log(word)


const word1 = `안녕
하세요`
console.log(word1)
// 백틱 사용 -> 줄바꿈 + 문자열 사이에 변수도 넣을 수 있다 (python -f'string)단, 이스케이프 문자열은 사용 불가
const word2 = `안녕
하세요`
console.log(word2)

const age = 10
const message = `홍길동은 ${age}
세 입니다.`
console.log(message)


const happy = 'Will you join us?'
const hacking = 'Happy' + 'Hacking' + '!'
console.log(happy, hacking)


// Boolean  -참, 거짓
const truthy = true
const falsy = false
console.log(truthy, falsy)
console.log(typeof truthy)
console.log(typeof falsy)


// Empty value
// JS 에서 null 값은 -> null, undefined 로 구분됌

let first_name
console.log(first_name)

let last_name = null // 의도적으로 값이 없음을 명시함
console.log(last_name)


console.log(typeof null)
console.log(typeof undefined)

console.log(null == undefined) //동등 비교 연산자
console.log(null === undefined) // 일치 연산자


// 연산자

// 할당 연산자
let c = 0

c += 10
console.log(c)

c -= 3
console.log(c)

c += 10
console.log(c)

c ++
console.log(c)

c --
console.log(c)


// 비교 연산자
// 변수 안에 var, let, const를 명시하지 않으면 JS 는 자동으로 var를 붙여줌
console.log(3 > 2)
console.log(3 < 2)

console.log('A' < 'B')
console.log('Z' < 'a')
console.log('가' < '나)

// 동등 비교 연산자
// 느슨 평가, 사용 지향
const a = 1
const b = "1"

console.log(a == b)
console.log(a != b)
console.log(a == Number(b))

// 자동 형변환 예시
console.log(8 * null) // 0
console.log("5" - 1) // 4(number)
console.log("5" + 1) // 51(string)
console.log("five" * 2) // NaN



// 일치 연산자
// 엄격 평가

const a = 1
const b = "1"

console.log(a === b)
console.log(a === Number(b))


// 논리 연산자

console.log(true && false) // 
console.log(true && true)

console.log(1 && 0) // 0
console.log(0 && 1) // 0
console.log(4 && 7) // 7

// or
console.log(false || true) // true
console.log(false || false) // false
console.log(1 || 0) // 1
console.log(0 || 1) // 1
console.log(4 || 7) // 4

// not
console.log(!true) // false
console.log(!false) // true


// 삼항 연산자
// 가장 앞의 boolean 값이 참이면 : 앞의 값이 반환되고 반대일 경우에는 : 뒤의 값이 반환
console.log(true ? 1 : 2) // 1
console.log(false ? 1 : 2) // 2
console.log('nyapy' ? 'awesome' : 'nice') // awesome

// 상황 연산의 결과를 변수에 할당할 수 있다!
console result = Math.PI > 4 ? 'Yep' : 'Nope' // nope
console.log(result)
*/