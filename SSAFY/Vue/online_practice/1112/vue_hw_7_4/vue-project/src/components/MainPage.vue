<script setup>
  import { useRouter } from 'vue-router';
  
  const props = defineProps({
    balance: Object
  })
  console.log(props)
  const router = useRouter()

  const goUpdate = function() {
    router.push({name: 'update', params: { name: props.balance.name }})
  }
</script>

<template>
  <div>
    <p>이름: {{ balance.name }}</p>
    <p>잔고: {{ balance.balance }}</p>
    <button @click="goUpdate">updateBalance</button>
    <hr>
  </div>
</template>

<style scoped>
  button {
    background-color: rgb(25, 125, 255);
    color: white;
    border-style: none;
    border-radius: 7%;
  }
</style>