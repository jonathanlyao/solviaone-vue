<template>
  <footer class="bg-slate-100 w-full border-t-0">
    <div class="grid grid-cols-1 md:grid-cols-4 gap-8 px-8 py-12 max-w-7xl mx-auto">
      <div class="md:col-span-1">
        <div class="text-lg font-bold text-blue-950 mb-4">Solvia One LLC</div>
        <p class="text-slate-500 text-sm mb-6 leading-relaxed">
          Precision in Digital Architecture. Providing reliable tech solutions for the next generation of local businesses.
        </p>
        <router-link to="/contact" class="text-blue-900 font-bold underline hover:text-blue-800 transition-colors uppercase tracking-wider text-xs">
          Contact Now
        </router-link>
      </div>
      <div class="flex flex-col space-y-3">
        <span class="text-blue-900 font-semibold uppercase text-xs tracking-widest mb-2">Connect</span>
        <a class="text-slate-500 text-sm hover:text-blue-800 transition-colors" href="#">Address: 24850 Van Zandt Ave.Little Neck NY 11362</a>
        <a class="text-slate-500 text-sm hover:text-blue-800 transition-colors" href="#">Phone: +1(929)608-6298</a>
        <a class="text-slate-500 text-sm hover:text-blue-800 transition-colors" href="#">Email: vicky@solvia-one.com</a>
        <a class="text-slate-500 text-sm hover:text-blue-800 transition-colors" href="#">Hours: Mon-Fri 9AM-6PM</a>
      </div>
      <div class="flex flex-col space-y-3">
        <span class="text-blue-900 font-semibold uppercase text-xs tracking-widest mb-2">Quick Links</span>
        <router-link to="/" class="text-slate-500 text-sm hover:text-blue-800 transition-colors">Home</router-link>
        <router-link to="/about" class="text-slate-500 text-sm hover:text-blue-800 transition-colors">About</router-link>
        <router-link to="/services" class="text-slate-500 text-sm hover:text-blue-800 transition-colors">Services</router-link>
        <router-link to="/cases" class="text-slate-500 text-sm hover:text-blue-800 transition-colors">Cases</router-link>
        <router-link to="/news" class="text-slate-500 text-sm hover:text-blue-800 transition-colors">News</router-link>
      </div>
      <div class="flex flex-col space-y-4">
        <span class="text-blue-900 font-semibold uppercase text-xs tracking-widest mb-2">Newsletter</span>
        <div class="flex h-10">
          <input class="bg-surface-container-highest border-none text-sm w-full focus:ring-1 focus:ring-primary px-2" placeholder="Email Address" type="email"/>
          <button class="bg-primary text-on-primary px-4 flex items-center justify-center">
            <span class="material-symbols-outlined text-sm">send</span>
          </button>
        </div>
        <p class="text-[10px] text-slate-400 uppercase tracking-tight">Stay updated with local tech insights.</p>
      </div>
    </div>
    <div class="border-t border-slate-200 py-6 px-8 max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-4">
      <div class="text-slate-500 text-xs italic">
        © 2026 Solvia One LLC. All rights reserved. Precision in Digital Architecture.
      </div>
      <div class="flex gap-6">
        <span class="material-symbols-outlined text-slate-400 cursor-pointer hover:text-primary transition-colors">social_leaderboard</span>
        <span class="material-symbols-outlined text-slate-400 cursor-pointer hover:text-primary transition-colors">language</span>
        <span class="material-symbols-outlined text-slate-400 cursor-pointer hover:text-primary transition-colors">alternate_email</span>
      </div>
    </div>
  </footer>
</template>

<script setup>
</script>
