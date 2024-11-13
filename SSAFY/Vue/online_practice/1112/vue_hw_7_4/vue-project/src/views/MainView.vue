<script setup>
  import MainPage from '@/components/MainPage.vue';
  import { useBalanceStore } from '@/stores/balance'
  const store = useBalanceStore()
</script>

<template>
  <h2>메인 페이지</h2>
  <MainPage 
   v-for="balance in store.balances" 
   :balance="balance"
  />
</template>
