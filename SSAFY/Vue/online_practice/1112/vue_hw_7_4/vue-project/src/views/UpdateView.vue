<template>
  <div>
    <h2>데이터 수정 페이지</h2>
    <p>이름" {{ name }}</p>
    <p>잔고: {{ balanceStore.getBalanceByName(name).balance }}</p>
    <button @click="balanceStore.increamentBalance(name)">+</button>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { useBalanceStore } from '@/stores/balance'

const route = useRoute()
const name = route.params.name
const balanceStore = useBalanceStore()

</script>

<style scoped>
</style>
