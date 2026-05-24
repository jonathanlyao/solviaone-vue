<template>
  <main>
    <section class="relative min-h-screen flex items-center pt-20 overflow-hidden bg-surface">
      <div class="absolute inset-0 z-0 opacity-10">
        <div class="absolute top-0 right-0 w-1/2 h-full bg-gradient-to-br from-primary to-primary-container transform skew-x-12 translate-x-1/4"></div>
      </div>
      <div class="max-w-7xl mx-auto px-8 w-full grid grid-cols-1 lg:grid-cols-12 gap-12 items-center relative z-10">
        <div class="lg:col-span-7">
          <span class="inline-block py-1 px-3 bg-secondary-container text-on-secondary-container text-xs font-bold uppercase tracking-widest mb-6">Established Local Expertise</span>
          <h1 class="text-5xl md:text-7xl font-extrabold text-editorial text-primary leading-[1.1] mb-8">
            Simple, Efficient, Reliable Local Tech Services
          </h1>
          <p class="text-lg text-secondary mb-10 max-w-xl leading-relaxed">
            We architect digital foundations for local businesses, ensuring your technical infrastructure is as solid as your reputation.
          </p>
          <div class="flex flex-wrap gap-4">
            <router-link to="/contact" class="bg-primary text-on-primary px-8 py-4 rounded-lg font-bold flex items-center gap-2 hover:bg-primary-container transition-all shadow-lg shadow-primary/10">
              Get Started
              <span class="material-symbols-outlined text-sm">arrow_forward</span>
            </router-link>
            <router-link to="/services" class="bg-surface-container-high text-primary px-8 py-4 rounded-lg font-bold hover:bg-surface-container-highest transition-all">
              View Services
            </router-link>
          </div>
        </div>
        <div class="lg:col-span-5 hidden lg:block">
          <div class="relative">
            <div class="absolute -inset-4 bg-primary-container/5 rounded-full blur-3xl"></div>
            <img alt="Professional tech team" class="rounded-xl shadow-2xl relative z-10 border-8 border-surface-container-lowest" src="/images/hero-team.jpg"/>
          </div>
        </div>
      </div>
    </section>

    <section class="py-24 bg-surface-container-low">
      <div class="max-w-7xl mx-auto px-8">
        <div class="flex flex-col md:flex-row justify-between items-end mb-16 gap-8">
          <div class="max-w-2xl">
            <h2 class="text-sm font-bold text-on-primary-container uppercase tracking-[0.2em] mb-4">Our Expertise</h2>
            <p class="text-4xl font-extrabold text-primary leading-tight">Tailored Technical Solutions for Every Business Stage</p>
          </div>
          <div class="h-px flex-grow bg-outline-variant/20 mx-8 hidden md:block"></div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-5 gap-4">
          <div class="group bg-surface-container-lowest p-8 flex flex-col justify-between h-80 hover:bg-primary transition-colors duration-300 cursor-pointer">
            <span class="material-symbols-outlined text-primary group-hover:text-on-primary text-4xl">hub</span>
            <div>
              <h3 class="font-bold text-primary group-hover:text-on-primary text-lg mb-2">Business Infrastructure</h3>
              <p class="text-sm text-secondary group-hover:text-on-primary/80">Scalable systems designed for stability.</p>
            </div>
          </div>
          <div class="group bg-surface-container-lowest p-8 flex flex-col justify-between h-80 hover:bg-primary transition-colors duration-300 cursor-pointer">
            <span class="material-symbols-outlined text-primary group-hover:text-on-primary text-4xl">web</span>
            <div>
              <h3 class="font-bold text-primary group-hover:text-on-primary text-lg mb-2">Web Development</h3>
              <p class="text-sm text-secondary group-hover:text-on-primary/80">Performance-first digital experiences.</p>
            </div>
          </div>
          <div class="group bg-surface-container-lowest p-8 flex flex-col justify-between h-80 hover:bg-primary transition-colors duration-300 cursor-pointer">
            <span class="material-symbols-outlined text-primary group-hover:text-on-primary text-4xl">shopping_cart</span>
            <div>
              <h3 class="font-bold text-primary group-hover:text-on-primary text-lg mb-2">E-commerce</h3>
              <p class="text-sm text-secondary group-hover:text-on-primary/80">Optimized sales flows and integrations.</p>
            </div>
          </div>
          <div class="group bg-surface-container-lowest p-8 flex flex-col justify-between h-80 hover:bg-primary transition-colors duration-300 cursor-pointer">
            <span class="material-symbols-outlined text-primary group-hover:text-on-primary text-4xl">build</span>
            <div>
              <h3 class="font-bold text-primary group-hover:text-on-primary text-lg mb-2">Maintenance</h3>
              <p class="text-sm text-secondary group-hover:text-on-primary/80">Proactive support and uptime security.</p>
            </div>
          </div>
          <div class="group bg-surface-container-lowest p-8 flex flex-col justify-between h-80 hover:bg-primary transition-colors duration-300 cursor-pointer">
            <span class="material-symbols-outlined text-primary group-hover:text-on-primary text-4xl">draw</span>
            <div>
              <h3 class="font-bold text-primary group-hover:text-on-primary text-lg mb-2">Illustration Platform</h3>
              <p class="text-sm text-secondary group-hover:text-on-primary/80">Creative toolsets for digital artists.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="py-32 bg-surface">
      <div class="max-w-7xl mx-auto px-8 grid grid-cols-1 lg:grid-cols-12 gap-16">
        <div class="lg:col-span-5">
          <h2 class="text-3xl font-extrabold text-primary mb-8 border-l-4 border-primary pl-6">Deeply Rooted, Exceptionally Focused.</h2>
        </div>
        <div class="lg:col-span-7">
          <p class="text-xl text-secondary leading-relaxed mb-6">
            Solvia One LLC was born from a commitment to the local business community. We believe that world-class technology shouldn't be reserved for global conglomerates.
          </p>
          <p class="text-xl text-secondary leading-relaxed">
            Our focus is singular: delivering high-precision digital architecture that empowers local entrepreneurs to compete, scale, and thrive in an increasingly digital economy.
          </p>
          <router-link to="/about" class="inline-flex items-center gap-2 text-primary font-bold hover:underline">
            Learn More About Us <span class="material-symbols-outlined text-sm">arrow_forward</span>
          </router-link>
        </div>
      </div>
    </section>

    <section class="py-24 bg-surface-container-highest">
      <div class="max-w-7xl mx-auto px-8">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-12">
          <div class="space-y-4">
            <div class="w-12 h-12 bg-primary flex items-center justify-center rounded-lg">
              <span class="material-symbols-outlined text-on-primary">speed</span>
            </div>
            <h3 class="text-xl font-bold text-primary">Efficiency</h3>
            <p class="text-on-surface-variant leading-relaxed">We eliminate technical bloat, focusing on streamlined workflows that deliver results faster without compromising quality.</p>
          </div>
          <div class="space-y-4">
            <div class="w-12 h-12 bg-primary flex items-center justify-center rounded-lg">
              <span class="material-symbols-outlined text-on-primary">verified</span>
            </div>
            <h3 class="text-xl font-bold text-primary">Professionalism</h3>
            <p class="text-on-surface-variant leading-relaxed">Clear communication, transparent timelines, and architectural precision are the pillars of every project we undertake.</p>
          </div>
          <div class="space-y-4">
            <div class="w-12 h-12 bg-primary flex items-center justify-center rounded-lg">
              <span class="material-symbols-outlined text-on-primary">payments</span>
            </div>
            <h3 class="text-xl font-bold text-primary">Cost-Effectiveness</h3>
            <p class="text-on-surface-variant leading-relaxed">High-end solutions designed for realistic budgets. We prioritize long-term ROI over short-term gimmicks.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="py-32 bg-surface">
      <div class="max-w-7xl mx-auto px-8">
        <div class="text-center mb-20">
          <h2 class="text-sm font-bold text-secondary uppercase tracking-[0.3em] mb-4">Local Success Stories</h2>
          <p class="text-4xl font-extrabold text-primary">Recent Impact Cases</p>
        </div>
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <div class="bg-surface-container-low overflow-hidden group">
            <div class="h-48 overflow-hidden">
              <img alt="Office workflow" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" src="/images/case-office-workflow.jpg"/>
            </div>
            <div class="p-8">
              <div class="text-xs font-bold text-on-primary-container mb-2">INFRASTRUCTURE</div>
              <h3 class="text-xl font-bold text-primary mb-3">Main Street Law Group</h3>
              <p class="text-secondary text-sm mb-6">Modernized legacy servers to cloud-hybrid infrastructure, increasing data retrieval speed by 40%.</p>
              <router-link to="/cases" class="text-primary font-bold text-sm flex items-center gap-2 hover:gap-3 transition-all">
                Read More <span class="material-symbols-outlined text-xs">arrow_forward</span>
              </router-link>
            </div>
          </div>
          <div class="bg-surface-container-low overflow-hidden group">
            <div class="h-48 overflow-hidden">
              <img alt="Retail shop" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" src="/images/case-retail-shop.jpg"/>
            </div>
            <div class="p-8">
              <div class="text-xs font-bold text-on-primary-container mb-2">E-COMMERCE</div>
              <h3 class="text-xl font-bold text-primary mb-3">The Local Boutique</h3>
              <p class="text-secondary text-sm mb-6">Launched a custom Shopify experience with local delivery integration, doubling monthly online revenue.</p>
              <router-link to="/cases" class="text-primary font-bold text-sm flex items-center gap-2 hover:gap-3 transition-all">
                Read More <span class="material-symbols-outlined text-xs">arrow_forward</span>
              </router-link>
            </div>
          </div>
          <div class="bg-surface-container-low overflow-hidden group">
            <div class="h-48 overflow-hidden">
              <img alt="Dashboard view" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" src="/images/case-dashboard.jpg"/>
            </div>
            <div class="p-8">
              <div class="text-xs font-bold text-on-primary-container mb-2">MAINTENANCE</div>
              <h3 class="text-xl font-bold text-primary mb-3">Heritage Construction</h3>
              <p class="text-secondary text-sm mb-6">Implemented 24/7 proactive security monitoring and automated backups for 15 remote site offices.</p>
              <router-link to="/cases" class="text-primary font-bold text-sm flex items-center gap-2 hover:gap-3 transition-all">
                Read More <span class="material-symbols-outlined text-xs">arrow_forward</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="py-24 bg-primary relative overflow-hidden">
      <div class="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/carbon-fibre.png')] opacity-10"></div>
      <div class="max-w-4xl mx-auto px-8 text-center relative z-10">
        <h2 class="text-3xl md:text-5xl font-extrabold text-on-primary mb-8 leading-tight">Ready to fortify your digital architecture?</h2>
        <div class="flex flex-col sm:flex-row justify-center gap-4">
          <router-link to="/contact" class="bg-on-primary text-primary px-10 py-4 rounded-lg font-bold hover:bg-secondary-container transition-all">
            Consult with an Architect
          </router-link>
          <router-link to="/cases" class="bg-primary-container text-on-primary-container border border-on-primary-container/30 px-10 py-4 rounded-lg font-bold hover:bg-primary/50 transition-all">
            View Our Portfolio
          </router-link>
        </div>
      </div>
    </section>
  </main>
</template>

<script setup>
</script>