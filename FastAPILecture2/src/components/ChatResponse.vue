<template>
  <div class="chat-response">
    <h2>AI 回復:</h2>
    <p>{{ response || '等待回復...' }}</p>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  response: string
}>();
</script>

<style scoped>
.chat-response {
  background-color: #f0f0f0;
  padding: 20px;
  border-radius: 5px;
}

h2 {
  margin-top: 0;
  color: #00bd7e;
}
</style>
<!--這是一個 Vue 3 組件，用於顯示 AI 的回覆。以下是代碼的主要部分解釋：-->
<!--模板部分（<template>）：-->
<!--定義了一個包含標題和段落的 div。-->
<!--標題固定顯示「AI 回覆:」。-->
<!--段落使用插值表達式 {{ response || '等待回覆...' }}，顯示 AI 的回覆內容。如果 response 為空，則顯示「等待回覆...」。-->
<!--腳本部分（<script setup lang="ts">）：-->
<!--使用 defineProps 定義了一個名為 response 的 prop，類型為字符串。-->
<!--這個 prop 用於接收父組件傳遞的 AI 回覆內容。-->
<!--樣式部分（<style scoped>）：-->
<!--為整個回覆區域設置了基本樣式：-->
<!--背景色設為淺灰色（#f0f0f0）。-->
<!--內邊距設為 20 像素。-->
<!--邊角設為圓角（5 像素）。-->
<!--標題樣式：-->
<!--上邊距設為 0。-->
<!--顏色設為綠色（#00bd7e）。-->
<!--這個組件的主要功能是顯示 AI 的回覆。它接收一個名為 response 的 prop，用於顯示回覆內容。如果沒有回覆（即 response 為空），則顯示「等待回覆...」。這種設計使得組件可以很容易地在等待回覆和顯示回覆之間切換，提供了良好的用戶體驗。-->
<!--組件使用了 scoped 樣式，確保樣式只應用於此組件，避免影響其他部分的頁面樣式。整體設計簡潔明了，易於理解和使用。-->
