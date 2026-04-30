<template>
  <main class="bg-surface text-on-surface antialiased pt-24 pb-20">
    <header class="max-w-7xl mx-auto px-8 py-16">
      <div class="max-w-3xl">
        <span class="text-primary font-bold tracking-widest text-xs uppercase mb-4 block">Information & Updates</span>
        <h1 class="text-5xl md:text-7xl font-extrabold tracking-tight text-primary leading-tight mb-6">Practical Insights for Your Business.</h1>
        <p class="text-lg text-on-surface-variant leading-relaxed">Stay informed with grounded technical advice, company milestones, and exclusive service opportunities tailored for the modern enterprise.</p>
      </div>
    </header>

    <section class="max-w-7xl mx-auto px-8 mb-20">
      <div class="grid grid-cols-1 md:grid-cols-12 gap-6 h-auto md:h-[500px]">
        <div class="md:col-span-8 relative group overflow-hidden rounded-xl bg-primary-container">
          <img class="absolute inset-0 w-full h-full object-cover opacity-40 mix-blend-overlay group-hover:scale-105 transition-transform duration-700" src="/images/server-room.jpg" alt="Server room"/>
          <div class="absolute inset-0 bg-gradient-to-t from-primary via-primary/20 to-transparent"></div>
          <div class="relative h-full flex flex-col justify-end p-10">
            <span class="bg-white/10 backdrop-blur-md text-white px-3 py-1 text-xs font-bold rounded mb-4 self-start">SERVICE ANNOUNCEMENT</span>
            <h2 class="text-3xl md:text-4xl font-bold text-white mb-4">Enhanced Managed Support for Multi-Site Offices</h2>
            <p class="text-white/80 max-w-lg mb-6">We've expanded our regional response team to provide onsite support for businesses with up to five satellite locations within the tri-state area.</p>
            <a class="flex items-center text-white font-bold group" href="#">
              Read more <span class="material-symbols-outlined ml-2 group-hover:translate-x-1 transition-transform">arrow_forward</span>
            </a>
          </div>
        </div>

        <div class="md:col-span-4 bg-surface-container-low p-8 rounded-xl flex flex-col">
          <span class="text-primary font-bold text-xs uppercase mb-4">Local Benefit</span>
          <h3 class="text-2xl font-bold text-primary mb-4 leading-snug">Spring Hardware Refresh Program</h3>
          <p class="text-on-surface-variant mb-auto">Active local partners are eligible for a 15% reduction on workstation upgrades through May 31st. Contact your account manager for details.</p>
          <div class="mt-8 pt-6 border-t border-outline-variant/30">
            <p class="text-xs text-secondary font-medium italic">Available for Innovation City regional clients only.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="bg-surface-container-low py-24">
      <div class="max-w-7xl mx-auto px-8">
        <div class="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-6">
          <div>
            <h2 class="text-3xl font-bold text-primary mb-2">Latest Updates</h2>
            <p class="text-on-surface-variant">Chronological archive of technical guides and company news.</p>
          </div>
          <div class="flex gap-2">
            <button class="px-4 py-2 bg-surface-container-highest text-primary font-semibold text-sm rounded transition-all">All Posts</button>
            <button class="px-4 py-2 hover:bg-surface-container-highest text-secondary font-semibold text-sm rounded transition-all">Tech Tips</button>
            <button class="px-4 py-2 hover:bg-surface-container-highest text-secondary font-semibold text-sm rounded transition-all">Events</button>
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <article class="bg-surface-container-lowest rounded-xl overflow-hidden group">
            <div class="aspect-video bg-primary-container/20 overflow-hidden">
              <img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" src="/images/hero-team.jpg" alt="Cloud infrastructure"/>
            </div>
            <div class="p-6">
              <span class="text-primary text-xs font-bold uppercase tracking-widest">Tech Tips</span>
              <h3 class="text-xl font-bold text-primary mt-2 mb-3">Optimizing Cloud Costs for Small Businesses</h3>
              <p class="text-secondary text-sm mb-4">Learn practical strategies to reduce your cloud spending without sacrificing performance or reliability.</p>
              <a class="text-primary font-bold text-sm flex items-center gap-2 hover:underline" href="#">
                Read More <span class="material-symbols-outlined text-sm">arrow_forward</span>
              </a>
            </div>
          </article>

          <article class="bg-surface-container-lowest rounded-xl overflow-hidden group">
            <div class="aspect-video bg-primary-container/20 overflow-hidden">
              <img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" src="/images/modern-office.jpg" alt="Office"/>
            </div>
            <div class="p-6">
              <span class="text-primary text-xs font-bold uppercase tracking-widest">Company News</span>
              <h3 class="text-xl font-bold text-primary mt-2 mb-3">Solvia One Expands Regional Support Coverage</h3>
              <p class="text-secondary text-sm mb-4">We're proud to announce expanded onsite support for businesses with multiple satellite locations.</p>
              <a class="text-primary font-bold text-sm flex items-center gap-2 hover:underline" href="#">
                Read More <span class="material-symbols-outlined text-sm">arrow_forward</span>
              </a>
            </div>
          </article>

          <article class="bg-surface-container-lowest rounded-xl overflow-hidden group">
            <div class="aspect-video bg-primary-container/20 overflow-hidden">
              <img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" src="/images/office-meeting.jpg" alt="Security"/>
            </div>
            <div class="p-6">
              <span class="text-primary text-xs font-bold uppercase tracking-widest">Security</span>
              <h3 class="text-xl font-bold text-primary mt-2 mb-3">Essential Security Practices for Remote Teams</h3>
              <p class="text-secondary text-sm mb-4">Protect your business data with these fundamental security measures for distributed workforces.</p>
              <a class="text-primary font-bold text-sm flex items-center gap-2 hover:underline" href="#">
                Read More <span class="material-symbols-outlined text-sm">arrow_forward</span>
              </a>
            </div>
          </article>
        </div>
      </div>
    </section>

    <section class="py-24 px-8 bg-surface">
      <div class="max-w-7xl mx-auto">
        <div class="grid grid-cols-1 md:grid-cols-12 gap-12">
          <div class="md:col-span-5">
            <h2 class="text-3xl font-extrabold text-primary mb-6">Previous Announcements</h2>
            <p class="text-secondary mb-8">A chronological archive of past updates, service changes, and company milestones.</p>
            <div class="space-y-6">
              <div class="flex gap-4 items-start group cursor-pointer">
                <div class="w-12 h-12 bg-surface-container flex items-center justify-center rounded-lg flex-shrink-0">
                  <span class="material-symbols-outlined text-primary">campaign</span>
                </div>
                <div>
                  <h4 class="font-bold text-primary group-hover:underline">Q1 Service Expansion</h4>
                  <p class="text-secondary text-sm">January 15, 2024</p>
                </div>
              </div>
              <div class="flex gap-4 items-start group cursor-pointer">
                <div class="w-12 h-12 bg-surface-container flex items-center justify-center rounded-lg flex-shrink-0">
                  <span class="material-symbols-outlined text-primary">security</span>
                </div>
                <div>
                  <h4 class="font-bold text-primary group-hover:underline">Security Protocol Update</h4>
                  <p class="text-secondary text-sm">December 20, 2023</p>
                </div>
              </div>
              <div class="flex gap-4 items-start group cursor-pointer">
                <div class="w-12 h-12 bg-surface-container flex items-center justify-center rounded-lg flex-shrink-0">
                  <span class="material-symbols-outlined text-primary">handshake</span>
                </div>
                <div>
                  <h4 class="font-bold text-primary group-hover:underline">New Partnership Announcement</h4>
                  <p class="text-secondary text-sm">November 5, 2023</p>
                </div>
              </div>
              <div class="flex gap-4 items-start group cursor-pointer">
                <div class="w-12 h-12 bg-surface-container flex items-center justify-center rounded-lg flex-shrink-0">
                  <span class="material-symbols-outlined text-primary">celebration</span>
                </div>
                <div>
                  <h4 class="font-bold text-primary group-hover:underline">Company Milestone: 50+ Projects</h4>
                  <p class="text-secondary text-sm">October 12, 2023</p>
                </div>
              </div>
            </div>
          </div>
          <div class="md:col-span-7">
            <div class="bg-surface-container-low rounded-2xl p-10">
              <div class="flex items-center gap-3 mb-6">
                <span class="material-symbols-outlined text-primary text-3xl">mail</span>
                <h3 class="text-2xl font-bold text-primary">Newsletter</h3>
              </div>
              <p class="text-secondary mb-8">Get the latest technical insights, company updates, and exclusive offers delivered to your inbox. No spam, unsubscribe anytime.</p>
              <form class="space-y-4">
                <div>
                  <label class="block text-xs font-bold text-secondary uppercase tracking-widest mb-2">Email Address</label>
                  <input type="email" class="w-full px-4 py-3 rounded-lg border border-outline-variant bg-surface focus:outline-none focus:ring-2 focus:ring-primary text-primary" placeholder="your@email.com"/>
                </div>
                <div>
                  <label class="block text-xs font-bold text-secondary uppercase tracking-widest mb-2">Company Name (Optional)</label>
                  <input type="text" class="w-full px-4 py-3 rounded-lg border border-outline-variant bg-surface focus:outline-none focus:ring-2 focus:ring-primary text-primary" placeholder="Your Company"/>
                </div>
                <div class="flex items-center gap-3">
                  <input type="checkbox" id="agree" class="w-4 h-4 accent-primary"/>
                  <label for="agree" class="text-sm text-secondary">I agree to receive email updates from Solvia One LLC</label>
                </div>
                <button type="submit" class="w-full bg-primary text-on-primary font-bold py-4 rounded-lg flex items-center justify-center gap-2 hover:bg-primary/90 transition-colors">
                  Subscribe Now
                  <span class="material-symbols-outlined text-sm">arrow_forward</span>
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script setup>
</script>
