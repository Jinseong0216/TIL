<template>
  <div class="card">
    <br>
    <h1 class="singerName">{{ singer.name }}</h1>
    <img src="@/assets/singer.jpg" alt="이미지가 없네용..." class="singerImage">
    <p class="singerDetail">가수 소개글</p>

    <!-- 앨범을 좌우로 배치 -->
    <div class="album-container">
      <div v-for="album in singer.Albums" :key="album.name" class="album-card">
        <h3>{{ album.name }}</h3>
        <p class="song-name" v-for="song in album.songs" :key="song">{{ song }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  singer: {
    type: Object,
    required: true,
  }
})
</script>

<style lang="scss" scoped>
.card {
  border: 1px solid #ccc;
  padding: 20px;
  border-radius: 10px;
  margin: 20px;
  background-color: #f7f9fc;
  text-align: center;
}

.singerName {
  font-size: 2rem;
  font-weight: 800;
  color: #333;
}

.singerDetail {
  font-size: 1.2rem;
  color: #555;
}

img.singerImage {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  margin: 20px;
}


.album-container {
  display: flex;
  justify-content: center; 
  flex-wrap: wrap;  /* 화면 크기에 맞게 카드들이 자동으로 줄바꿈 되도록 */
  gap: 20px; 
}

.album-card {
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 15px;
  text-align: center;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);  /* 카드에 그림자 추가 */
}

.song-name {
  color: orangered;
}
</style>
