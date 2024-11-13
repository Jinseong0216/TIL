import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'

export const useArticleStore = defineStore('article', () => {
  const articles = ref([])
  const router = useRouter()
  
  const getArticles = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/articles/'
    })
    .then(res => {
      console.log(res)
      articles.value = res.data
    })
  }

  const createArticle = function () {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/api/v1/articles/',
      data : {
        title: title.value,
        content: content.value
      },
    }).then(() => {
      router.push({ name: 'home'})
    })
  }
  return { 
    articles, 
    getArticles, createArticle, 
  }
})
