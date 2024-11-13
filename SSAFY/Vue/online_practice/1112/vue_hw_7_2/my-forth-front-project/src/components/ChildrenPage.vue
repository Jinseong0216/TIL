<template>
  <div class="children">
    <h3>자식 페이지</h3>
    <p>{{ children.name }}</p>
  </div>
</template>

<script setup>
  defineProps({
    children: Object
  })
</script>

<style scoped>
  .children {
    background-color: white;
    border-style: solid;
    border-color: rgb(184, 190, 190);
    border-width: 1px;
    margin: 1rem;
    padding: 1rem;
    text-align: center;
  }

</style>