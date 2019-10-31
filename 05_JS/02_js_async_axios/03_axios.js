// Promise 엑시오스로 요청시 돌아오는 것
const axios = require('axios')

axios.get('https://jsonplaceholder.typicode.com/posts')
.then(res => {
  console.log(res)
})
.catch(err => {
  console.log(err)
})