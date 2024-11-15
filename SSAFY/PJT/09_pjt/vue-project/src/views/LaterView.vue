<template>
  <div>
    <h3>나중에 볼 동영상</h3>

    <!-- 저장된 동영상이 없을 때 메시지 출력 -->
    <p v-if="savedVideos.length === 0">등록된 비디오 없음</p>

    <!-- 저장된 동영상 목록 -->
    <div v-if="savedVideos.length > 0" class="video-thumbnails">
      <div class="thumbnails-container">
        <div v-for="(video, index) in savedVideos" :key="index" class="thumbnail-item">
          <div class="card">
            <router-link :to="{ name: 'ContentDetail', params: { videoId: video.id } }">
              <img :src="video.snippet.thumbnails.medium.url" :alt="video.snippet.title" class="thumbnail-img" />
            </router-link>
            <div class="card-body">
              <h4 class="card-title">{{ video.snippet.title }}</h4>
              <p class="card-description">{{ video.snippet.description.substring(0, 100) }}...</p>
              <button @click="removeFromSavedVideos(video.id)" class="remove-btn">삭제</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

// 저장된 비디오 목록을 관리하는 상태 변수
const savedVideos = ref([])

// LocalStorage에서 저장된 나중에 볼 동영상 목록 불러오기
const loadSavedVideos = () => {
  const saved = localStorage.getItem('latervideos')
  console.log("불러온 로컬스토리지 데이터:", saved) // 콘솔 로그로 데이터 확인
  if (saved) {
    savedVideos.value = JSON.parse(saved)  // JSON 데이터를 객체로 변환하여 저장
  } else {
    console.log("저장된 비디오 없음")
  }
}

// 동영상을 저장 목록에서 삭제하는 함수
const removeFromSavedVideos = (videoId) => {
  const updatedVideos = savedVideos.value.filter((video) => video.id !== videoId)
  savedVideos.value = updatedVideos
  localStorage.setItem('latervideos', JSON.stringify(updatedVideos))
  console.log("삭제된 후 저장된 비디오 목록:", updatedVideos) // 삭제 후 목록 확인
}

// 페이지가 로드될 때 저장된 나중에 볼 동영상 목록 불러오기
onMounted(() => {
  loadSavedVideos()
})
</script>

<style scoped>


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
  position: relative; /* 카드 내부에서 버튼 위치를 기준으로 설정 */
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
  position: relative; /* 삭제 버튼을 카드 내에서 절대 위치로 배치하기 위해 필요 */
}

.card-title {
  font-size: 1.1rem;
  font-weight: bold;
  margin-bottom: 10px;
}

.card-description {
  font-size: 0.9rem;
  color: #555;
}

.remove-btn {
  background-color: red;
  color: white;
  font-size: 1rem;
  border: none;
  cursor: pointer;
  border-radius: 5px;
  padding: 5px 10px;
  position: absolute; /* 절대 위치 설정 */
  bottom: 10px; /* 카드 하단에 10px */
  right: 10px; /* 카드 오른쪽에 10px */
}

.remove-btn:hover {
  background-color: darkred;
}
</style>
