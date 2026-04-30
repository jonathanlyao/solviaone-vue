<template>
  <div class="min-h-screen bg-surface flex flex-col">
    <NavBar />
    <router-view class="flex-grow" />
    <Footer />
  </div>
</template>

<script setup>
import NavBar from './components/NavBar.vue'
import Footer from './components/Footer.vue'
</script>