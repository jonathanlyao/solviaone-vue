<template>
  <main class="bg-surface font-body text-on-surface antialiased pt-24 pb-20">
    <section class="px-8 py-20 max-w-7xl mx-auto">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
        <div class="lg:col-span-7">
          <span class="text-primary font-label font-bold uppercase tracking-[0.2em] text-xs mb-4 block">Architectural Excellence</span>
          <h1 class="text-primary font-headline font-extrabold text-5xl md:text-7xl leading-[1.1] tracking-tight mb-8">
            Precision Digital <br/><span class="text-on-primary-container">Infrastructure.</span>
          </h1>
          <p class="text-secondary text-lg max-w-xl leading-relaxed font-body">
            We design, deploy, and maintain the digital foundations that empower modern SMEs. Our approach balances technical rigor with practical operational efficiency.
          </p>
          <div class="flex flex-col sm:flex-row gap-4">
            <router-link to="/contact" class="bg-primary text-on-primary font-bold py-4 px-8 rounded-lg flex items-center justify-center gap-2 hover:bg-primary/90 transition-colors">
              <span class="material-symbols-outlined">mail</span>
              Contact Us
            </router-link>
            <router-link to="/about" class="bg-surface-container-high text-primary font-bold py-4 px-8 rounded-lg flex items-center justify-center gap-2 hover:bg-surface-container-highest transition-colors">
              <span class="material-symbols-outlined">business</span>
              About Us
            </router-link>
          </div>
        </div>
        <div class="lg:col-span-5 relative">
          <div class="aspect-square rounded-xl overflow-hidden shadow-2xl">
            <img class="w-full h-full object-cover" src="/images/tech-infrastructure.jpg" alt="Tech infrastructure"/>
          </div>
        </div>
      </div>
    </section>

    <section class="bg-surface-container-low py-24">
      <div class="max-w-7xl mx-auto px-8">
        <div class="mb-16">
          <h2 class="text-primary font-headline font-bold text-3xl mb-4">Core Service Areas</h2>
          <div class="h-1 w-20 bg-primary"></div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div class="bg-surface-container-lowest p-8 rounded-lg flex flex-col h-full group transition-all duration-200 hover:shadow-lg">
            <div class="text-primary mb-6">
              <span class="material-symbols-outlined text-4xl">storefront</span>
            </div>
            <h3 class="font-headline font-bold text-xl text-primary mb-4">Online Platforms</h3>
            <p class="text-secondary text-sm leading-relaxed mb-8 flex-grow">
              Specialized digital storefronts for Shoes & Illustration industries. We build platforms that respect the aesthetic demands of creative sectors.
            </p>
            <button class="flex items-center gap-2 text-primary font-bold text-sm hover:underline group-hover:gap-4 transition-all">
              Inquire Now <span class="material-symbols-outlined text-sm">arrow_forward</span>
            </button>
          </div>

          <div class="bg-surface-container-lowest p-8 rounded-lg flex flex-col h-full group transition-all duration-200 hover:shadow-lg">
            <div class="text-primary mb-6">
              <span class="material-symbols-outlined text-4xl">settings_input_component</span>
            </div>
            <h3 class="font-headline font-bold text-xl text-primary mb-4">SME Infrastructure</h3>
            <p class="text-secondary text-sm leading-relaxed mb-8 flex-grow">
              Complete Information Infrastructure including LAN setup and hardware procurement tailored for Small-to-Medium Enterprises.
            </p>
            <button class="flex items-center gap-2 text-primary font-bold text-sm hover:underline group-hover:gap-4 transition-all">
              Inquire Now <span class="material-symbols-outlined text-sm">arrow_forward</span>
            </button>
          </div>

          <div class="bg-surface-container-lowest p-8 rounded-lg flex flex-col h-full group transition-all duration-200 hover:shadow-lg">
            <div class="text-primary mb-6">
              <span class="material-symbols-outlined text-4xl">code</span>
            </div>
            <h3 class="font-headline font-bold text-xl text-primary mb-4">Basic Web Dev</h3>
            <p class="text-secondary text-sm leading-relaxed mb-8 flex-grow">
              Lean, high-performance web development. We focus on clean code and lightning-fast load times for professional corporate identities.
            </p>
            <button class="flex items-center gap-2 text-primary font-bold text-sm hover:underline group-hover:gap-4 transition-all">
              Inquire Now <span class="material-symbols-outlined text-sm">arrow_forward</span>
            </button>
          </div>

          <div class="bg-surface-container-lowest p-8 rounded-lg flex flex-col h-full group transition-all duration-200 hover:shadow-lg">
            <div class="text-primary mb-6">
              <span class="material-symbols-outlined text-4xl">shopping_bag</span>
            </div>
            <h3 class="font-headline font-bold text-xl text-primary mb-4">E-commerce Setup</h3>
            <p class="text-secondary text-sm leading-relaxed mb-8 flex-grow">
              Efficient, lightweight e-commerce solutions that minimize overhead while maximizing conversion and operational ease.
            </p>
            <button class="flex items-center gap-2 text-primary font-bold text-sm hover:underline group-hover:gap-4 transition-all">
              Inquire Now <span class="material-symbols-outlined text-sm">arrow_forward</span>
            </button>
          </div>

          <div class="bg-surface-container-lowest p-8 rounded-lg flex flex-col h-full group transition-all duration-200 hover:shadow-lg">
            <div class="text-primary mb-6">
              <span class="material-symbols-outlined text-4xl">build</span>
            </div>
            <h3 class="font-headline font-bold text-xl text-primary mb-4">Maintenance & Support</h3>
            <p class="text-secondary text-sm leading-relaxed mb-8 flex-grow">
              Ongoing technical maintenance and rapid-response support to ensure your business operations never face downtime.
            </p>
            <button class="flex items-center gap-2 text-primary font-bold text-sm hover:underline group-hover:gap-4 transition-all">
              Inquire Now <span class="material-symbols-outlined text-sm">arrow_forward</span>
            </button>
          </div>

          <div class="bg-surface-container-lowest p-8 rounded-lg flex flex-col h-full group transition-all duration-200 hover:shadow-lg">
            <div class="text-primary mb-6">
              <span class="material-symbols-outlined text-4xl">lightbulb</span>
            </div>
            <h3 class="font-headline font-bold text-xl text-primary mb-4">Digital Consulting</h3>
            <p class="text-secondary text-sm leading-relaxed mb-8 flex-grow">
              Strategic customization of digital assets. We audit your existing stack and provide a roadmap for technical maturity.
            </p>
            <button class="flex items-center gap-2 text-primary font-bold text-sm hover:underline group-hover:gap-4 transition-all">
              Inquire Now <span class="material-symbols-outlined text-sm">arrow_forward</span>
            </button>
          </div>

          <div class="bg-surface-container-lowest p-8 rounded-lg flex flex-col h-full group transition-all duration-200 hover:shadow-lg md:col-span-2 lg:col-span-1">
            <div class="text-primary mb-6">
              <span class="material-symbols-outlined text-4xl">cloud_upload</span>
            </div>
            <h3 class="font-headline font-bold text-xl text-primary mb-4">Software Deployment</h3>
            <p class="text-secondary text-sm leading-relaxed mb-8 flex-grow">
              End-to-end deployment services. We handle the complexities of server configuration and environment setup for your custom software.
            </p>
            <button class="flex items-center gap-2 text-primary font-bold text-sm hover:underline group-hover:gap-4 transition-all">
              Inquire Now <span class="material-symbols-outlined text-sm">arrow_forward</span>
            </button>
          </div>
        </div>
      </div>
    </section>

    <section class="py-24 max-w-7xl mx-auto px-8">
      <div class="grid grid-cols-12 gap-4 items-start">
        <div class="col-span-12 lg:col-span-4">
          <h2 class="text-4xl font-extrabold text-primary leading-tight">
            Built for <br/>Growth.
          </h2>
        </div>
        <div class="col-span-12 lg:col-span-8 lg:pl-12 border-l border-slate-200">
          <p class="text-xl text-secondary leading-relaxed">
            At Solvia One LLC, we don't just provide services; we engineer digital ecosystems. Every solution we deploy is designed to scale with your business, ensuring that your infrastructure investment grows alongside your ambitions.
          </p>
          <div class="mt-12 grid grid-cols-2 md:grid-cols-4 gap-8">
            <div>
              <div class="text-3xl font-bold text-primary">99.9%</div>
              <div class="text-xs uppercase text-secondary tracking-widest mt-2">Uptime Rate</div>
            </div>
            <div>
              <div class="text-3xl font-bold text-primary">24/7</div>
              <div class="text-xs uppercase text-secondary tracking-widest mt-2">Support</div>
            </div>
            <div>
              <div class="text-3xl font-bold text-primary">50+</div>
              <div class="text-xs uppercase text-secondary tracking-widest mt-2">Projects</div>
            </div>
            <div>
              <div class="text-3xl font-bold text-primary">100%</div>
              <div class="text-xs uppercase text-secondary tracking-widest mt-2">Commitment</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="py-24 px-8 bg-surface-container-lowest">
      <div class="max-w-7xl mx-auto">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-16 items-center">
          <div>
            <h2 class="text-4xl font-extrabold text-primary mb-8 tracking-tight">Our Process</h2>
            <div class="space-y-8">
              <div class="flex gap-6">
                <div class="flex-shrink-0 w-12 h-12 bg-primary text-on-primary flex items-center justify-center rounded-lg font-bold text-xl">1</div>
                <div>
                  <h4 class="font-bold text-primary uppercase text-xs tracking-widest mb-2">Discovery</h4>
                  <p class="text-secondary text-sm">We begin by understanding your business goals, challenges, and technical requirements through detailed consultation.</p>
                </div>
              </div>
              <div class="flex gap-6">
                <div class="flex-shrink-0 w-12 h-12 bg-primary text-on-primary flex items-center justify-center rounded-lg font-bold text-xl">2</div>
                <div>
                  <h4 class="font-bold text-primary uppercase text-xs tracking-widest mb-2">Design</h4>
                  <p class="text-secondary text-sm">Our architects design a customized solution blueprint that aligns with your objectives and budget.</p>
                </div>
              </div>
              <div class="flex gap-6">
                <div class="flex-shrink-0 w-12 h-12 bg-primary text-on-primary flex items-center justify-center rounded-lg font-bold text-xl">3</div>
                <div>
                  <h4 class="font-bold text-primary uppercase text-xs tracking-widest mb-2">Implementation</h4>
                  <p class="text-secondary text-sm">We deploy your solution with precision, ensuring minimal disruption to your daily operations.</p>
                </div>
              </div>
              <div class="flex gap-6">
                <div class="flex-shrink-0 w-12 h-12 bg-primary text-on-primary flex items-center justify-center rounded-lg font-bold text-xl">4</div>
                <div>
                  <h4 class="font-bold text-primary uppercase text-xs tracking-widest mb-2">Support</h4>
                  <p class="text-secondary text-sm">Ongoing monitoring and support ensure your systems remain secure, efficient, and up-to-date.</p>
                </div>
              </div>
            </div>
          </div>
          <div class="bg-surface-container-low rounded-xl p-12">
            <h3 class="text-2xl font-bold text-primary mb-6">Ready to Get Started?</h3>
            <p class="text-secondary mb-8">Schedule a consultation with our architecture team to discuss your specific needs and discover how we can help.</p>
            <div class="flex flex-col sm:flex-row gap-4">
              <router-link to="/contact" class="inline-flex items-center justify-center gap-2 bg-primary text-on-primary px-8 py-4 rounded-lg font-bold hover:bg-primary/90 transition-colors">
                <span class="material-symbols-outlined">mail</span>
                Contact Us
              </router-link>
              <router-link to="/about" class="inline-flex items-center justify-center gap-2 bg-surface-container-high text-primary px-8 py-4 rounded-lg font-bold hover:bg-surface-container-highest transition-colors">
                <span class="material-symbols-outlined">business</span>
                About Us
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script setup>
</script>