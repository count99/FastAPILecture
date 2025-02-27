import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'


// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
  ],
  base: '/static/', // 关键配置！
  build: {
    outDir: '../static', // 直接输出到 FastAPI 的静态目录
    assetsDir: 'assets',
    emptyOutDir: true,
    terserOptions: {
      compress: {
        drop_console: true, // 移除 console 语句
        drop_debugger: true, // 移除 debugger 语句
      },
    },
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
})
