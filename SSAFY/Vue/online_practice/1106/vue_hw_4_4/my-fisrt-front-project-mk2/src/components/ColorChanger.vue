<template>
  <div>
    <input type="text" v-model="input" id="test">
    <p 
    :class="[
      input == 'red' || input == 'blue' || input == 'green' 
      ? input
      : '']"
      >입력창에 올바른 색상 명을 입력하면 글자색이 바껴요.</p>
  </div>  
</template>

<script setup>
import { ref } from 'vue'
const input = ref(null)
</script>

<style lang="scss" scoped>
.red {
  color: red;
}
.blue {
  color: blue;
}
.green {
  color: green;
}
</style>