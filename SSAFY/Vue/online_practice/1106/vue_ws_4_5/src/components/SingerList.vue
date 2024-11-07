  <template>
    <div class="container">
      <p class="display-4">가수 정보 페이지에 오신 것을 환영합니다.</p>
      <div class="col-12">여러분이 좋아하는 가수와 아티스트에 대한 정보를 탐색해보세요.</div>
      <img src="@/assets/microphone.jpg " alt="이미지가 없네용...">
      <h1>가수 목록 </h1>
      
        <span v-for="singer in singers" :key="singer.name">
          <!-- singer 전달하는 법 -->
          <SingerDetail :singer="singer"/>
        </span>
    </div>
  </template>

  <script setup>
  import SingerDetail from "@/components/singers/SingerDetail.vue"
  import {ref} from 'vue'

  const singers = ref([
    {
      name: 'Adel',
      Albums: [
        {
          name: '앨범 1',
          songs: ['노래 목록 1', '노래 목록 2', '노래 목록 3']
        },
        {
          name: '앨범 2',
          songs: ['노래 목록 1', '노래 목록 2', '노래 목록 3']
        },
      ]
    },
    {
      name: 'Maroon5',
      Albums: [
        {
          name: '앨범 1',
          songs: ['노래 목록 1', '노래 목록 2', '노래 목록 3']
        },
        {
          name: '앨범 2',
          songs: ['노래 목록 1', '노래 목록 2', '노래 목록 3']
        },
      ]
    },
    {
      name: 'Dua Lipa',
      Albums: [
        {
          name: '앨범 1',
          songs: ['노래 목록 1', '노래 목록 2', '노래 목록 3']
        },
        {
          name: '앨범 2',
          songs: ['노래 목록 1', '노래 목록 2', '노래 목록 3']
        },
      ]
    }
  ])
  </script>

  <style lang="scss" scoped>
  // from GPT
  .container {
    margin-top: 50px;
    text-align: center;
    background-color: #f7f9fc;
    border-radius: 8px;
    padding: 30px;
  }

  h1 {
    font-size: 2.5rem;
    font-weight: 800; 
    color: orangered;
  };

  h2 {
    font-size: 2rem;
    font-weight: 800; 
    color: #000000; 
  };

  .col-12 {
    font-size: 1.2rem;
    font-weight: 800;
    color: #6c757d;
  };

  img {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    margin-top: 20px;
    border-style: dotted;
  };

  .card {
    display: inline-block;
    width: 40%;
    margin: 20px;
  }

  </style>
