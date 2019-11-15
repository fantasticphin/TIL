<template>
  <div>
    <h1>여기는 최상위 컴포넌트</h1>
    <TodoList category="취업성공"></TodoList>
    <TodoList category="SSAFY"></TodoList>
    <TodoList category="기타"></TodoList>
  </div>
</template>

<script>
import TodoList from './components/TodoList.vue' // 같은 경로상에 있는 파일을 불러온다

// 상위 경로에 적용시킴
export default {
  components: {
    TodoList,
  }  
}
</script>

<style>
</style>