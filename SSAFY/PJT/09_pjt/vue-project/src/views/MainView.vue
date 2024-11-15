<script setup>
import { ref, onMounted } from 'vue'
import { marked } from 'marked'  // 수정: 명명된 export 방식으로 임포트

// 파일을 읽어오는 함수 (Node.js의 fs를 사용할 수 없으므로 브라우저에서는 fetch 사용)
const readMarkdownFile = async (filePath) => {
  try {
    const response = await fetch(filePath)
    const text = await response.text()
    return text
  } catch (error) {
    console.error("파일을 읽는 데 문제가 발생했습니다:", error)
    return ''
  }
}

// 마크다운 내용을 HTML로 변환
const markdownContent = ref('')

// 컴포넌트가 로드될 때 README.md 파일을 불러옵니다.
onMounted(async () => {
  const markdown = await readMarkdownFile('/README.md')  // 'public/README.md' 파일 경로로 접근
  markdownContent.value = marked(markdown)  // 'marked'를 사용하여 HTML로 변환
})
</script>

<template>
  <main>
    <!-- README 내용이 로딩되었을 때 출력 -->
    <div v-html="markdownContent"></div>
  </main>
</template>

<style scoped>
main {
  font-family: 'Arial', sans-serif;
  padding: 20px;
  background-color: #f4f4f4;
  border-radius: 8px;
  margin: 0 auto;
  max-width: 1200px;
}

h1, h2, h3 {
  color: #333;
}

code {
  background-color: #f4f4f4;
  padding: 2px 4px;
  font-size: 0.9rem;
  border-radius: 4px;
}

pre {
  background-color: #2d2d2d;
  color: #fff;
  padding: 10px;
  border-radius: 6px;
  overflow: auto;
  white-space: pre-wrap;
  word-wrap: break-word;
}

a {
  color: #007bff;
}
</style>
