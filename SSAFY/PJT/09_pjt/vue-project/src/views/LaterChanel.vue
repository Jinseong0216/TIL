<template>
  <div class="later-channel-view">
    <h3>저장된 채널</h3>

    <!-- 저장된 채널이 없으면 메시지 표시 -->
    <p v-if="channels.length === 0">저장된 채널이 없습니다.</p>

    <!-- 저장된 채널 목록 -->
    <div class="channel-list" v-if="channels.length > 0">
      <div v-for="(channel, index) in channels" :key="index" class="channel-card">
        <div class="channel-content">
          <span class="channel-title">{{ channel.title }}</span>
          <hr>
          <p class="channel-description">{{ truncateDescription(channel.description) }}</p>
        </div>
        <button @click="removeChannel(channel.id)" class="delete-btn">삭제</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

// 로컬 스토리지에서 저장된 채널 목록을 가져옵니다
const channels = ref([])

// 채널 목록을 로컬 스토리지에서 불러오는 함수
const loadChannels = () => {
  const savedChannels = JSON.parse(localStorage.getItem('laterChannels') || '[]')
  channels.value = savedChannels
}

// 채널 삭제 함수
const removeChannel = (channelId) => {
  const updatedChannels = channels.value.filter(channel => channel.id !== channelId)
  localStorage.setItem('laterChannels', JSON.stringify(updatedChannels))
  loadChannels()  // 삭제 후 채널 목록을 다시 로드
}

// 설명이 100자 이상이면 잘라서 '...' 추가하는 함수
const truncateDescription = (description) => {
  if (description.length > 100) {
    return description.slice(0, 100) + '...'
  }
  return description
}

// 컴포넌트가 로드될 때 채널 목록 불러오기
onMounted(loadChannels)
</script>

<style scoped>
.later-channel-view {
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  margin: 0 auto;
  max-width: 1200px;
}

h3 {
  font-size: 2.5rem; /* 글씨 크기 크게 */
  font-weight: bold; /* 글씨 두껍게 */
  color: #333; /* 어두운 색으로 깔끔하게 */
  text-align: center;
  margin-bottom: 20px;
  font-family: 'Gulim', '굴림', sans-serif; /* 굴림체 폰트 설정 */
  letter-spacing: 1px; /* 글자 간격을 살짝 넓힘 */
  text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1); /* 부드러운 그림자 추가 */
}

.channel-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
}

.channel-card {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
  padding: 22px;  /* 패딩을 더 넉넉하게 */
  width: 300px;  /* 카드 너비를 1.5배로 조정 */
  height: 200px; /* 카드의 높이를 1.5배로 설정 */
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  text-align: center;
  position: relative;  /* 버튼의 절대 위치를 기준으로 설정 */
  overflow: hidden;
}

.channel-card:hover {
  transform: scale(1.05);
}

.channel-content {
  flex-grow: 1;
}

.channel-title {
  font-size: 1.2rem;
  font-weight: bold;
  color: #333;
}

.channel-description {
  font-size: 1rem; /* 설명 크기 증가 */
  color: #666;
  margin-top: 5px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.delete-btn {
  background-color: #f44336;
  color: white;
  border: none;
  padding: 4px 8px;  /* 버튼 크기 절반으로 줄임 */
  font-size: 0.8rem;  /* 더 작은 폰트 크기 */
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
  position: absolute; /* 절대 위치 설정 */
  bottom: 10px; /* 카드의 하단 10px */
  right: 10px; /* 카드의 오른쪽 10px */
}

.delete-btn:hover {
  background-color: #d32f2f;
}
</style>
