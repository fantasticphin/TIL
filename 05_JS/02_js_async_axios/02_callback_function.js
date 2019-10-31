// 배열로 이루어진 숫자들을 다 더하는 함수
// const numbersAddEach = numbers => {
//   let sum = 0
//   for (const number of numbers){
//     sum += number
//   }
//   return sum 
// }

// console.log(numbersAddEach([1,2,3,4,5]))


// 배열로 이루어진 숫자들을 다 빼는 함수
// const numbersSubtract = numbers => {
//   let sub = 0
//   for (const number of numbers) {
//     sub -= number
//   }
//   return sub
// }

// console.log(numbersSubtract([1,2,3,4,5]))


// 배열로 이루어진 숫자들을 다 곱하는 함수
// const numbersMultiply = numbers => {
//   let sum = 1
//   for (const number of numbers) {
//     sum *= number
//   }
//   return sum
// }

// console.log(numbersMultiply([1,2,3,4,5]))

// 숫자로 이루어진 배열의 요소를 [??]한다.
/*
const NUMBERS = [1,2,3,4,5]

const numbersEach = (numbers, callback) => {
  let acc
  for (const number of numbers) {
    acc = callback(number, acc)
  }
  return acc
}
// 더한다
const addEach = (number, acc=0) => {
  return acc + number
}

console.log(numbersEach(NUMBERS, addEach))

// 뺀다
const subEach = (number, acc=0) => {
  return acc - number
}

console.log(numbersEach(NUMBERS, subEach))
// 곱한다
const mulEach = (number, acc=0) => {
  return acc * number
}

console.log(numbersEach(NUMBERS, mulEach))
*/

const NUMBERS = [1,2,3,4,5]

const numbersEach = (numbers, callback) => {
  let acc
  for (const number of numbers) {
    acc = callback(number, acc)
  }
  return acc
}
// 더한다, 뺀다, 곱한다
console.log(numbersEach(NUMBERS, (number, acc = 0)=> acc + number))
console.log(numbersEach(NUMBERS, (number, acc = 0)=> acc - number))
console.log(numbersEach(NUMBERS, (number, acc = 1)=> acc * number))