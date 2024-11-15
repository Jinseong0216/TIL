<template>
  <div>
    <h3>Home</h3>
    <hr>
    <!-- 최근 검색기록 -->
    <div>
      <h4>최근 검색기록</h4>
      <ul>
        <li v-for="(query, index) in recentSearches.slice(0, 10)" :key="index">{{ index + 1 }}. {{ query }}</li>
      </ul>
    </div>
    <hr>

    <!-- 저장된 동영상 -->
    <div>
      <h4>저장된 동영상</h4>
      <ul>
        <li v-for="(video, index) in savedVideos.slice(0, 10)" :key="index">{{ index + 1 }}. {{ video.snippet.title }}</li>
      </ul>
    </div>
    <hr>
    <!-- 저장된 채널 -->
    <div>
      <h4>저장된 채널</h4>
      <ul>
        <li v-for="(channel, index) in savedChannels.slice(0, 10)" :key="index">{{ index + 1 }}. {{ channel.title }}</li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

// 저장된 최근 검색어, 동영상, 채널을 관리할 ref 변수
const recentSearches = ref([])  // 최근 검색어
const savedVideos = ref([])     // 저장된 동영상
const savedChannels = ref([])   // 저장된 채널

// 로컬스토리지에서 최근 검색어, 저장된 동영상, 저장된 채널을 불러오는 함수
const loadStoredData = () => {
  const storedSearches = JSON.parse(localStorage.getItem('recentSearches')) || []
  const storedVideos = JSON.parse(localStorage.getItem('latervideos')) || []
  console.log(savedVideos)
  const storedChannels = JSON.parse(localStorage.getItem('laterChannels')) || []
  console.log(savedChannels)
  recentSearches.value = storedSearches
  savedVideos.value = storedVideos
  savedChannels.value = storedChannels
}

// 컴포넌트가 마운트될 때 로컬스토리지에서 데이터 로드
onMounted(loadStoredData)
</script>

<style scoped>
h4 {
  margin-top: 20px;
  font-size: 1.2rem;
  font-weight: bold;
}

ul {
  list-style-type: none;
  padding-left: 0;
}

li {
  margin-bottom: 10px;
}
</style>
