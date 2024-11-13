<template>
  <div>
    <button @click="goCreate">게시글 생성</button>
    <div class="articles">
      <div v-for="article in store.articles" :key="article.title" class="article">
        <h3>{{ articleOrder++ }}번 게시글</h3>
        <p>제목:  {{ article.title }}</p>
        <p>내용: {{ article.content }}</p>
        <hr>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useArticleStore } from '@/stores/articles'
import { useRouter } from 'vue-router'

const store = useArticleStore()
const articleOrder = 1

onMounted(() => {
  store.getArticles()
})

const router = useRouter()
const goCreate = function () {
  router.push({ name: 'create' })
}
</script>

<style lang="scss" scoped>
.articles {
  margin-top: 1rem;
}

.article {
  margin-left: 2rem;
}
</style>