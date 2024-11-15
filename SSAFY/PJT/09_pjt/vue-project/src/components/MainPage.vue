<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark custom-navbar">
      <a class="navbar-brand" href="/">MyTube</a>
      <div class="navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link class="nav-link" to="/home">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/search">Search</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/laterVideo">Later</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/laterChannel">Channel</router-link>
          </li>
        </ul>
      </div>
    </nav>

    <!-- 뒤로가기 버튼 -->
    <button class="btn btn-light back-btn" @click="goBack">
      <i class="fas fa-arrow-left"></i> 뒤로가기
    </button>

    <!-- 라우터 뷰는 현재 경로에 맞는 컴포넌트를 렌더링 -->
    <router-view class="content"></router-view>
  </div>
</template>

<script setup>
// 뒤로가기 버튼 클릭 시 이전 페이지로 이동하는 함수
const goBack = () => {
  window.history.back()
}
</script>

<style scoped>
.custom-navbar {
  padding: 5px;
  margin: 5px;
}

.navbar-brand {
  font-size: 1rem; /* 브랜드 텍스트 크기 */
}

.navbar-nav .nav-link {
  font-size: 0.85rem; /* 네비게이션 링크 텍스트 크기 */
}

.back-btn {
  margin: 10px 50px; /* 양쪽 50px 마진 */
  padding: 5px 12px; /* 버튼 크기 줄임 */
  font-size: 0.75rem; /* 버튼 텍스트 크기 줄임 */
  display: flex;
  align-items: center;
  justify-content: center;
}

.back-btn i {
  margin-right: 5px; /* 아이콘과 텍스트 간 간격 줄이기 */
  font-size: 0.9rem; /* 아이콘 크기 줄임 */
}

/* router-view 콘텐츠 양쪽 마진 추가 */
.content {
  margin: 0 50px; /* 양쪽 50px 마진 */
}
</style>
