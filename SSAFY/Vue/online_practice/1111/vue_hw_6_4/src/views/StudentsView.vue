<template>
  <div>
    <p @click="goDetail(student.name)" v-for="student in students" :key="student.name">{{ student.name }} 학생 정보 보기</p>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const students = [
  {name: '김하나'},
  {name: '김둘'},
  {name: '김셋'},
]
const router = useRouter()
const goDetail = function (studentName) {
  router.push( { name: 'studentDetail', params: {name: studentName}})
}
</script>

<style>

</style>