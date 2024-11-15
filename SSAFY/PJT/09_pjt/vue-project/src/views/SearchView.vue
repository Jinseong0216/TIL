<template>
  <div>
    <h3>비디오 검색</h3>
    <!-- 검색어 입력 필드와 '찾기' 버튼 -->
    <div>
      <input
        v-model="searchQuery"
        type="text"
        placeholder="검색어를 입력하세요"
        class="search-input"
        @keydown.enter="searchVideos"
      />
      <button @click="searchVideos" class="search-btn">찾기</button>
      
      <!-- 검색어가 없을 때 오류 메시지 표시 -->
      <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
    </div>
    
    <!-- 검색어 기록 표시 -->
    <div v-if="recentSearches.length > 0" class="recent-searches">
      <h4>최근 검색어: </h4>
        <a v-for="(query, index) in recentSearches" :key="index" @click="searchFromHistory(query)" class="recent-searchs">
          [{{ query }}]
        </a> 

    </div>
    
    <!-- 검색 결과로 나온 비디오 썸네일들 -->
    <div class="video-thumbnails">
      <div v-if="videos.length > 0" class="thumbnails-container">
        <div v-for="(video, index) in videos" :key="index" class="thumbnail-item">
          <div class="card">
            <!-- 비디오 썸네일 클릭 시 해당 동영상 상세 페이지로 이동 -->
            <router-link :to="{ name: 'ContentDetail', params: { videoId: video.id.videoId } }">
              <img :src="video.snippet.thumbnails.medium.url" :alt="video.snippet.title" class="thumbnail-img" />
            </router-link>
            <div class="card-body">
              <h4 class="card-title">{{ video.snippet.title }}</h4>
              <p class="card-description">{{ video.snippet.description.substring(0, 100) }}...</p>
            </div>
          </div>
        </div>
      </div>
      <p v-else>검색 결과가 없습니다.</p>
    </div>
    
    <!-- 다음 페이지 버튼 -->
    <div v-if="nextPageToken && nextPageToken !== 'undefined'" class="pagination">
      <button @click="loadNextPage" class="pagination-btn">↓</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const searchQuery = ref('')
const videos = ref([])
const errorMessage = ref('')
const nextPageToken = ref(null)
const isInitialSearch = ref(true)
const recentSearches = ref([])

// YouTube API URL과 API 키 (자신의 API 키로 교체)
const apiKey = 'AIzaSyBYx589z1Cpdb8LDVwRdrNqRKFpbPfqBHI'
const apiUrl = 'https://www.googleapis.com/youtube/v3/search'

// 로컬스토리지에 저장된 검색 결과와 검색어 불러오기
const loadStoredResults = () => {
  const storedQuery = localStorage.getItem('searchQuery')
  const storedVideos = JSON.parse(localStorage.getItem('videos'))
  const storedToken = localStorage.getItem('nextPageToken')
  const storedRecentSearches = JSON.parse(localStorage.getItem('recentSearches'))

  if (storedQuery) searchQuery.value = storedQuery
  if (storedVideos) videos.value = storedVideos
  if (storedToken) nextPageToken.value = storedToken
  if (storedRecentSearches) recentSearches.value = storedRecentSearches
}

// 로컬스토리지에 검색 결과 및 검색어 목록 저장
const saveResultsToLocalStorage = () => {
  localStorage.setItem('searchQuery', searchQuery.value)
  localStorage.setItem('videos', JSON.stringify(videos.value))
  localStorage.setItem('nextPageToken', nextPageToken.value)
  localStorage.setItem('recentSearches', JSON.stringify(recentSearches.value))
}

// 비디오 검색 함수
const searchVideos = async () => {
  if (searchQuery.value.trim() === '') {
    errorMessage.value = '검색어를 입력해주세요.'
    videos.value = []
    nextPageToken.value = null
    return
  }

  errorMessage.value = ''
  isInitialSearch.value = true
  videos.value = []  // 기존 검색 결과 지우기
  nextPageToken.value = null

  try {
    const maxResults = isInitialSearch.value ? 12 : 6

    const response = await fetch(`${apiUrl}?part=snippet&q=${searchQuery.value}&type=video&maxResults=${maxResults}&key=${apiKey}`)
    const data = await response.json()
    
    videos.value = data.items
    nextPageToken.value = data.nextPageToken || null

    // 최근 검색어 처리
    updateRecentSearches(searchQuery.value)

    saveResultsToLocalStorage() // 검색 결과 저장
    isInitialSearch.value = false
  } catch (error) {
    console.error('검색 중 오류 발생:', error)
    errorMessage.value = '검색 중 오류가 발생했습니다.'
    videos.value = []
    nextPageToken.value = null
  }
}

// 최근 검색어 목록 갱신
const updateRecentSearches = (newQuery) => {
  const index = recentSearches.value.indexOf(newQuery)
  if (index !== -1) {
    // 이미 있는 검색어는 가장 앞에 오도록 이동
    recentSearches.value.splice(index, 1)
  }
  recentSearches.value.unshift(newQuery)
  
  // 최근 검색어가 10개를 초과하면 마지막 항목 삭제
  if (recentSearches.value.length > 10) {
    recentSearches.value.pop()
  }
}

// 저장된 검색어로 검색
const searchFromHistory = (query) => {
  searchQuery.value = query
  searchVideos()
}

// 다음 페이지 로드 함수
const loadNextPage = async () => {
  if (!nextPageToken.value) return

  try {
    const response = await fetch(`${apiUrl}?part=snippet&q=${searchQuery.value}&type=video&maxResults=6&pageToken=${nextPageToken.value}&key=${apiKey}`)
    const data = await response.json()

    videos.value = [...videos.value, ...data.items]
    nextPageToken.value = data.nextPageToken
    saveResultsToLocalStorage() // 추가된 검색 결과 저장
  } catch (error) {
    console.error('다음 페이지 로드 중 오류 발생:', error)
  }
}

// 컴포넌트가 로드될 때 로컬스토리지에 저장된 검색 결과와 최근 검색어 목록 불러오기
onMounted(loadStoredResults)
</script>

<style scoped>
.search-input {
  padding: 8px 12px;
  margin-right: 10px;
  font-size: 1rem;
  width: 600px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

.search-btn {
  padding: 8px 20px;
  background-color: #4CAF50;
  color: white;
  font-size: 1rem;
  border: none;
  cursor: pointer;
  border-radius: 5px;
  height: 40px;
}

.search-btn:hover {
  background-color: #45a049;
}

.error-message {
  color: red;
  font-size: 0.9rem;
  margin-top: 10px;
}

.video-thumbnails {
  margin-top: 20px;
}

.thumbnails-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 20px;
  padding: 0 10px;
}

.thumbnail-item {
  display: flex;
  justify-content: center;
}

.card {
  background-color: #fff;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.thumbnail-img {
  width: 100%;
  height: 180px;
  object-fit: cover;
}

.card-body {
  padding: 15px;
}

.card-title {
  font-size: 1.1rem;
  font-weight: bold;
  color: #333;
}

.card-description {
  font-size: 0.9rem;
  color: #555;
}

.recent-searches {
  margin-top: 20px;
}

.recent-searches h4 {
  font-size: 1.2rem;
  margin-bottom: 10px;
}

.recent-searches ul {
  list-style-type: none;
  padding: 0;
}

.recent-searches li {
  font-size: 1rem;
  color: #007BFF;
  cursor: pointer;
  margin-bottom: 5px;
}

.recent-searches li:hover {
  text-decoration: underline;
}

.pagination {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.pagination-btn {
  padding: 10px 20px;
  font-size: 1rem;
  background-color: #007BFF;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 5px;
}

.pagination-btn:hover {
  background-color: #0056b3;
}

</style>
