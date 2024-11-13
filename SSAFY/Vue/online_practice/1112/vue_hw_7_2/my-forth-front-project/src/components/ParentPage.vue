<template>
  <div class="parents">
    <h2>부모 컴포넌트</h2>
    <p>{{ family.father }}</p>
    <p>{{ family.mother }}</p>
    <ChildrenPage
    v-for="children in family.children" 
    :key="index" 
    :children="children" 
    />
  </div>
</template>

<script setup>
  import ChildrenPage from '@/components/ChildrenPage.vue';
  
  defineProps({
    family: Object
  })
</script>

<style scoped>
  .parents {
    background-color: rgb(228, 235, 248);
    text-align: center;
    margin: 1rem;
    padding: 1rem;
  }
</style>