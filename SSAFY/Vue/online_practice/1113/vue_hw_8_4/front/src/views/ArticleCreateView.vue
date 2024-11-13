<template>
  <div>
    <h1>게시글 생성 페이지</h1>
    <form @submit.prevent="store.createArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title">
      <label for="content">내용 : </label>
      <input type="text" id="content" v-model.trim="content">
      <button type="submit">create</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useArticleStore } from '@/stores/articles'

const store = useArticleStore()
const title = ref(null)
const content = ref(null)

</script>

<style scoped>

</style>