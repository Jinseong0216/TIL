<template>
  <div class="container">
    <h1 class="display-4">가수 정보 페이지에 오신 것을 환영합니다.</h1>
    <div class="col-12">여러분이 좋아하는 가수와 아티스트에 대한 정보를 탐색해보세요.</div>
    <img src="@/assets/microphone.jpg " alt="이미지가 없네용...">
  </div>
</template>

<script setup>
  // 특별히 추가할 내용이 없다면 이 부분은 그대로 두어도 됩니다.
</script>

<style lang="scss" scoped>
// from GPT
.container {
  margin-top: 50px;
  text-align: center;
  background-color: #f7f9fc; /* 밝은 배경 */
  border-radius: 8px; /* 둥근 모서리 */
  padding: 30px;
}

h1 {
  font-size: 2.5rem;
  font-weight: 800; 
  color: #000000; /* 어두운 텍스트 */
}

.col-12 {
  font-size: 1.2rem;
  font-weight: 800;
  color: #6c757d; /* 어두운 회색 */
}

img {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  margin-top: 20px;
}

</style>
