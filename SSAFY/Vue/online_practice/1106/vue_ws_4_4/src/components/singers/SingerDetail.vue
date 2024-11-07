<template>
  <div class="card">
    <br>
    <h1 class="singerName">가수 이름</h1>
    <img src="@/assets/singer.jpg " alt="이미지가 없네용...">
    <p class="singerDetail">가수 소개글</p>
  </div>
</template>

<script setup>
</script>

<style lang="scss" scoped>
div {
  border-style: solid;
};

img {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  margin: 20px;
  // border-style: dotted;
};

.singerName {
  font-size: 1.8rem;
  font-weight: 800; 
  color: #000000;
};

</style>  