<template>
  <div>
    <div v-if="videoDetails">
      <h4>{{ videoDetails.snippet.title }}</h4>
      <hr>
    </div>
    <!-- 동영상 `iframe` -->
    <div v-if="videoDetails">
      <div class="video-player">
        <iframe
          :src="`https://www.youtube.com/embed/${videoDetails.id}`"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
        ></iframe>
      </div>

      <!-- 동영상 정보 -->
      <div class="video-info">
        <!-- 채널 정보 추가 -->
        <div class="channel-info">
          <hr>
          <p><strong>채널 이름:</strong> {{ videoDetails.snippet.channelTitle }}</p>
          <p><strong>채널 ID:</strong> {{ videoDetails.snippet.channelId }}</p>
          <p><strong>게시일:</strong> {{ new Date(videoDetails.snippet.publishedAt).toLocaleDateString() }}</p>
          <hr>
        </div>
      </div>

      <!-- 채널 저장/삭제 버튼 -->
      <button v-if="isChannelSaved !== null" @click="toggleSaveChannel" class="save-btn">
        {{ isChannelSaved ? '채널 삭제' : '채널 저장' }}
      </button>

      <!-- 동영상 저장/취소 버튼 -->
      <button v-if="isSaved !== null" @click="toggleSaveVideo" class="save-btn">
        {{ isSaved ? '저장 취소' : '동영상 저장' }}
      </button>
    </div>

    <!-- 저장된 동영상 없을 경우 메시지 -->
    <p v-else>동영상 상세 정보를 로드할 수 없습니다.</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

// 동영상 상세 정보와 저장 상태를 관리
const videoDetails = ref(null)
const isSaved = ref(null)  // 동영상 저장 여부
const isChannelSaved = ref(null)  // 채널 저장 여부
const route = useRoute() // 라우터 정보를 가져옵니다

// URL 파라미터에서 비디오 ID 가져오기
const videoId = route.params.videoId // 라우터에서 videoId를 가져옵니다

// 동영상 저장 여부 확인 함수
const checkIfSaved = () => {
  if (!videoDetails.value) return false;  // videoDetails가 아직 로드되지 않았으면 false를 반환

  const savedVideos = JSON.parse(localStorage.getItem('latervideos') || '[]');
  console.log("저장된 비디오 목록:", savedVideos);  // 로컬스토리지에서 불러온 데이터 확인

  // videoDetails.value.id.videoId와 저장된 비디오의 id.videoId를 비교
  return savedVideos.some(video => video.id === videoDetails.value.id);
};

// 채널 저장 여부 확인 함수
const checkIfChannelSaved = () => {
  const savedChannels = JSON.parse(localStorage.getItem('laterChannels') || '[]');
  console.log("저장된 채널 목록:", savedChannels);

  // 채널 ID로 저장된 채널을 찾기
  return savedChannels.some(channel => channel.id === videoDetails.value.snippet.channelId);
};

// 동영상 저장/취소 함수
const toggleSaveVideo = () => {
  const savedVideos = JSON.parse(localStorage.getItem('latervideos') || '[]');
  console.log("저장된 비디오 목록:", savedVideos);  // 저장된 목록을 확인

  if (isSaved.value) {
    // 비디오가 이미 저장되어 있는 경우, 해당 비디오 삭제 (일치하는 항목만)
    const updatedVideos = savedVideos.filter(video => video.id !== videoDetails.value.id);
    localStorage.setItem('latervideos', JSON.stringify(updatedVideos));
    isSaved.value = false;  // 상태 변경
  } else {
    // 비디오 전체 정보를 저장
    savedVideos.push({
      id: videoDetails.value.id,  // 비디오 ID만 저장
      snippet: videoDetails.value.snippet,  // 비디오 설명 정보
      thumbnails: videoDetails.value.snippet.thumbnails // 썸네일 정보
    });
    localStorage.setItem('latervideos', JSON.stringify(savedVideos));
    isSaved.value = true;  // 상태 변경
  }
};

// 채널 저장/삭제 함수
const toggleSaveChannel = () => {
  const savedChannels = JSON.parse(localStorage.getItem('laterChannels') || '[]');
  console.log("저장된 채널 목록:", savedChannels);  // 저장된 채널 목록을 확인

  if (isChannelSaved.value) {
    // 채널이 이미 저장되어 있는 경우, 해당 채널 삭제
    const updatedChannels = savedChannels.filter(channel => channel.id !== videoDetails.value.snippet.channelId);
    localStorage.setItem('laterChannels', JSON.stringify(updatedChannels));
    isChannelSaved.value = false;  // 상태 변경
  } else {
    // 채널 전체 정보를 저장
    savedChannels.push({
      id: videoDetails.value.snippet.channelId,  // 채널 ID만 저장
      title: videoDetails.value.snippet.channelTitle,  // 채널 이름
      description: videoDetails.value.snippet.description,  // 채널 설명
    });
    localStorage.setItem('laterChannels', JSON.stringify(savedChannels));
    isChannelSaved.value = true;  // 상태 변경
  }
};

// 동영상 상세 정보 가져오는 함수
const fetchVideoDetails = async () => {
  const apiKey = 'AIzaSyBYx589z1Cpdb8LDVwRdrNqRKFpbPfqBHI'
  const apiUrl = `https://www.googleapis.com/youtube/v3/videos?part=snippet&id=${videoId}&key=${apiKey}`

  try {
    const response = await fetch(apiUrl)
    const data = await response.json()

    if (data.items.length > 0) {
      videoDetails.value = data.items[0] // 동영상 상세 정보

      // 동영상 정보가 로드된 후 저장 여부 확인
      isSaved.value = checkIfSaved()  // 비디오 ID가 일치하는지 확인
      isChannelSaved.value = checkIfChannelSaved()  // 채널 ID가 일치하는지 확인
    }
  } catch (error) {
    console.error('동영상 정보를 가져오는 중 오류 발생:', error)
  }
}

// 컴포넌트가 처음 로드되었을 때 상세 정보 가져오기
onMounted(fetchVideoDetails)

</script>

<style scoped>

.video-player {
  text-align: center;
  margin-bottom: 20px;
}

.video-player iframe {
  width: 100%;
  max-width: 800px;
  height: 450px;
}

.video-info {
  margin-bottom: 20px;
}

.channel-info {
  margin-top: 10px;
  color: #555;
}

.save-btn {
  padding: 10px 20px;
  margin-left: 10px;
  background-color: #4CAF50;
  color: white;
  font-size: 1rem;
  border: none;
  cursor: pointer;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.save-btn:hover {
  background-color: #45a049;
}

.save-btn:focus {
  outline: none;
}
</style>
