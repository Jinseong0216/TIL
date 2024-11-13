import { createRouter, createWebHistory } from 'vue-router'
import SomeView from '@/views/SomeView.vue'
import OtherView from '@/views/OtherView.vue'
import StudentsView from '@/views/StudentsView.vue'
import StudentDetailView from '@/views/StudentDetailView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {path: '/',
     name: 'some',
     component: SomeView,
    },
    {path: '/other',
     name: 'other',
     component: OtherView,
    },
    {path: '/students',
     name: 'students',
     component: StudentsView,
    },
    {path: '/stdudents/:name',
     name: 'studentDetail',
     component: StudentDetailView,
    },
  ]
})

export default router
