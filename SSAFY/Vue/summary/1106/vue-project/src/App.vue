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