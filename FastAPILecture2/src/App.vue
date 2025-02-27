<template>
  <div class="app">
    <h1>AI 對話系統</h1>
    <ChatInput @send-message="sendMessage" :isLoading="isLoading" />
    <ChatResponse :response="aiResponse" />
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import ChatInput from './components/ChatInput.vue';
import ChatResponse from './components/ChatResponse.vue';
// aiResponse: 用於存儲 AI 的回應
const aiResponse = ref('');
// isLoading: 用於追蹤請求的加載狀態
const isLoading = ref(false);

const sendMessage = async (message: string) => {
  if (isLoading.value || !message.trim()) return;

  isLoading.value = true;
  aiResponse.value = '正在處理...';

  try {
    // 添加請求超時控制
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 5000);

    const response = await fetch('http://127.0.0.1:8000/api/data', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify({ message: message.trim() }),
      signal: controller.signal
    });

    clearTimeout(timeoutId);

    // 強化狀態碼檢查
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.detail || `HTTP 錯誤！狀態碼：${response.status}`);
    }

    const data = await response.json();
    aiResponse.value = data.message.replace('Message(message=', '').replace(')', ''); // 修復 FastAPI 返回格式問題
  } catch (error) {
    console.error('API 請求失敗:', error);
    aiResponse.value = error instanceof Error ?
      `錯誤：${error.message}` :
      '網路連接異常，請檢查後重試';
  } finally {
    isLoading.value = false;
  }
};

</script>

<style scoped>
.app {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

h1 {
  text-align: center;
  color: #00bd7e;
}
</style>
<!--模板部分（<template>）：-->
<!--定義了應用的基本結構，包含一個標題和兩個子組件：ChatInput 和 ChatResponse。-->
<!--ChatInput 組件綁定了 sendMessage 方法和 isLoading 狀態。-->
<!--ChatResponse 組件接收 aiResponse 作為 prop。-->
<!--腳本部分（<script setup lang="ts">）：-->
<!--導入了必要的 Vue 函數和子組件。-->
<!--定義了兩個響應式變數：aiResponse 和 isLoading。-->
<!--sendMessage 函數是核心邏輯：-->
<!--設置載入狀態。-->
<!--使用 fetch API 發送 POST 請求到後端。-->
<!--包含了請求超時控制（5秒）。-->
<!--處理響應，更新 aiResponse。-->
<!--包含錯誤處理邏輯。-->
<!--樣式部分（<style scoped>）：-->
<!--為應用設置了基本樣式，包括最大寬度、居中對齊等。-->
<!--設置了標題的樣式。-->
<!--主要功能和特點：-->
<!--整合了輸入（ChatInput）和回應（ChatResponse）組件。-->
<!--實現了與後端 API 的通信，使用 fetch 發送 POST 請求。-->
<!--加入了錯誤處理和載入狀態管理，提高了用戶體驗。-->
<!--使用了請求超時控制，避免長時間等待。-->
<!--處理了 FastAPI 返回格式的問題，確保正確顯示回應。-->
<!--這個組件作為應用的主要入口，協調了用戶輸入、API 請求和回應顯示的整個流程。它的設計考慮到了多種情況，包括載入狀態、錯誤處理和數據格式化，使得整個 AI 對話系統能夠順暢運行。-->
