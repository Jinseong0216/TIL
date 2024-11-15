import { createRouter, createWebHistory } from 'vue-router'

import mainView from '@/views/MainView.vue'
import homeView from '@/views/homeView.vue'
import searchView from '@/views/searchView.vue'
import laterView from '@/views/laterView.vue'
import LaterChanel from '@/views/LaterChanel.vue'
import ContentDetail from '@/components/ContentDetail.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: mainView,
    },
    {
      path: '/home',
      name: 'home',  // 홈 페이지
      component: homeView,  // homeView 컴포넌트
    },
    {
      path: '/search',
      name: 'search',
      component: searchView,
    },
    {
      path: '/laterVideo',
      name: 'later',
      component: laterView,  // laterView 컴포넌트
    },
    {
      path: '/laterChannel',  // 동영상 상세 페이지
      name: 'laterChanel',
      component: LaterChanel,
      props: true  // URL 파라미터를 props로 전달
    },
    {
      path: '/video/:videoId',  // 동영상 상세 페이지
      name: 'ContentDetail',
      component: ContentDetail,
      props: true  // URL 파라미터를 props로 전달
    },
  ],
})

export default router
