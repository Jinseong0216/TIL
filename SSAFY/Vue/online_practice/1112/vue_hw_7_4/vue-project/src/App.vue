<template>
  <div>
    <RouterLink :to="{ name: 'main' }" class="router-link">main</RouterLink>
    <h1>pinia + router 연습하기</h1>
    <RouterView />
  </div>
</template>

<script setup>
  import { RouterLink, RouterView } from 'vue-router';
  import { useBalanceStore } from '@/stores/balance';

  const store = useBalanceStore()
  const balances = store.balances
</script>

<style scoped>
.router-link {
  margin-right: 5px;
}
</style>