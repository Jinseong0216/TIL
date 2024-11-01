<template>
  <div class="slot-machine">
    <h1>Node.js 와 Vue 기능 구현 테스트</h1>
    <div class="reels">
      <div class="reel" v-for="(symbol, index) in reels" :key="index">
        <span>{{ symbol }}</span>
      </div>
    </div>
    <button @click="spinReels">💲💲Spin💲💲</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      symbols: ['🍒', '🍋', '🍊', '🔔', '🍇', '⭐'],
      reels: ['⭐', '⭐', '⭐'], // 초기화 시 플레이스홀더로 설정
      spinCount: 50, // 회전 횟수
    };
  },
  methods: {
    spinReels() {
      this.reels = ['⭐', '⭐', '⭐']; // 릴 초기화
      let count = 0;

      const interval = setInterval(() => {
        this.reels = this.reels.map(() => 
          this.symbols[Math.floor(Math.random() * this.symbols.length)]
        );
        count++;

        // 회전한 후 결과 확인
        if (count >= this.spinCount) {
          clearInterval(interval);
          setTimeout(this.finalizeReels, 100); // 약간의 지연 후 최종 결과 결정
        }
      }, 50); // 50ms마다 회전
    },
    finalizeReels() {
      for (let i = 0; i < 3; i++) {
        setTimeout(() => {
          this.reels[i] = this.symbols[Math.floor(Math.random() * this.symbols.length)];
          // 마지막 릴 업데이트 후 결과 체크
          if (i === 2) {
            setTimeout(this.checkResult, 1000)
            // this.checkResult();
          }
        }, 1000 * (i + 1)); // 1초 간격으로 지연
      }
    },
    checkResult() {
      let message;
      if (this.reels[0] === this.reels[1] && this.reels[1] === this.reels[2]) {
        message = '당첨!';
      } else {
        message = '아쉽네요.';
      }
      alert(message); // 결과 메시지를 alert로 표시
    },
  },
};
</script>

<style scoped>
.slot-machine {
  text-align: center;
  margin: 20px;
}

.reels {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.reel {
  font-size: 2rem;
  margin: 0 10px;
}
</style>
