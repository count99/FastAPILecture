<template>
  <div class="chat-input">
    <input
      v-model="message"
      @keyup.enter="sendMessage"
      :disabled="isLoading"
      placeholder="輸入你的問題..."
    />
    <button @click="sendMessage" :disabled="isLoading">
      {{ isLoading ? '加載中...' : '發送' }}
    </button>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const message = ref('');
const emit = defineEmits(['send-message']);
const props = defineProps<{
  isLoading: boolean
}>();

const sendMessage = () => {
  if (message.value.trim() && !props.isLoading) {
    emit('send-message', message.value);
    message.value = '';
  }
};
</script>

<style scoped>
.chat-input {
  display: flex;
  margin-bottom: 20px;
}

input {
  flex-grow: 1;
  padding: 10px;
  font-size: 16px;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  background-color: #00bd7e;
  color: white;
  border: none;
  cursor: pointer;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
</style>
<!--這是一個 Vue 3 組件，使用了組合式 API（Composition API）。它實現了一個聊天輸入框的功能。以下是代碼的主要部分解釋：-->
<!--模板部分（<template>）：-->
<!--定義了一個包含輸入框和按鈕的 div。-->
<!--輸入框使用 v-model 綁定了 message 變數，並在按下 Enter 鍵時觸發 sendMessage 方法。-->
<!--按鈕點擊時也會觸發 sendMessage 方法。-->
<!--腳本部分（<script setup lang="ts">）：-->
<!--導入 Vue 3 的 ref 函數。-->
<!--創建一個響應式變數 message 用於存儲輸入的訊息。-->
<!--定義一個 emit 函數，用於向父組件發送事件。-->
<!--sendMessage 函數檢查訊息是否為空，如果不為空則發送訊息並清空輸入框。-->
<!--樣式部分（<style scoped>）：-->
<!--為聊天輸入框設置了基本的樣式，包括佈局、間距和顏色等。-->
<!--使用 scoped 確保樣式只應用於此組件。-->
<!--這個組件的主要功能是允許用戶輸入訊息並發送。當用戶輸入訊息並按下 Enter 鍵或點擊發送按鈕時，-->
<!--組件會觸發一個事件，將訊息傳遞給父組件處理。這種設計使得組件可以很容易地集成到更大的聊天應用中。-->
