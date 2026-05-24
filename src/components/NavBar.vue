<template>
  <nav class="fixed top-0 w-full z-50 bg-slate-50/80 backdrop-blur-md shadow-sm">
    <div class="flex justify-between items-center w-full px-8 py-4 max-w-7xl mx-auto">
      <router-link to="/" class="text-xl font-extrabold tracking-tight text-blue-950">
        Solvia One LLC
      </router-link>
      <div class="hidden md:flex items-center space-x-8">
        <router-link
          to="/"
          class="nav-link"
          :class="{ 'active': $route.path === '/' }"
        >
          Home
        </router-link>
        <router-link
          to="/about"
          class="nav-link"
          :class="{ 'active': $route.path === '/about' }"
        >
          About
        </router-link>
        <router-link
          to="/services"
          class="nav-link"
          :class="{ 'active': $route.path === '/services' }"
        >
          Services
        </router-link>
        <router-link
          to="/cases"
          class="nav-link"
          :class="{ 'active': $route.path === '/cases' }"
        >
          Success Cases
        </router-link>
        <router-link
          to="/advantages"
          class="nav-link"
          :class="{ 'active': $route.path === '/advantages' }"
        >
          Service Advantages
        </router-link>
        <router-link
          to="/news"
          class="nav-link"
          :class="{ 'active': $route.path === '/news' }"
        >
          News
        </router-link>
      </div>
      <router-link
        to="/contact"
        class="bg-primary text-on-primary px-6 py-2 rounded-lg font-semibold hover:bg-primary-container transition-all scale-95 active:opacity-80"
      >
        Contact Us
      </router-link>
    </div>
  </nav>
</template>

<script setup>
</script>

<style scoped>
.nav-link {
  @apply text-slate-600 hover:text-blue-900 transition-colors uppercase tracking-wider text-xs font-semibold;
}

.nav-link.router-link-exact-active {
  @apply text-blue-900 font-bold border-b-2 border-blue-900 pb-1;
}
</style>