<template>
  <main class="bg-surface font-body text-on-surface pt-24 pb-20">
    <section class="px-8 pt-16 pb-24 max-w-7xl mx-auto">
      <div class="grid grid-cols-1 md:grid-cols-12 gap-8 items-end">
        <div class="md:col-span-8">
          <span class="text-primary font-label uppercase tracking-widest text-xs font-bold mb-4 block">Our Portfolio</span>
          <h1 class="text-5xl md:text-7xl font-headline font-extrabold text-primary tracking-tight leading-none">
            Precision in <br/> Digital Success.
          </h1>
        </div>
        <div class="md:col-span-4">
          <p class="text-secondary text-lg leading-relaxed mb-4">
            We transform technical complexity into streamlined business performance. Explore how our digital architecture empowers modern enterprises.
          </p>
        </div>
      </div>
    </section>

    <section class="bg-surface-container-low py-12">
      <div class="max-w-7xl mx-auto px-8 flex flex-wrap gap-4 overflow-x-auto">
        <button class="bg-primary text-on-primary px-6 py-3 rounded-sm font-label text-xs uppercase tracking-widest font-bold">All Projects</button>
        <button class="bg-surface-container-high text-secondary px-6 py-3 rounded-sm font-label text-xs uppercase tracking-widest font-bold hover:bg-secondary-container transition-colors">Enterprise Digitization</button>
        <button class="bg-surface-container-high text-secondary px-6 py-3 rounded-sm font-label text-xs uppercase tracking-widest font-bold hover:bg-secondary-container transition-colors">E-commerce</button>
        <button class="bg-surface-container-high text-secondary px-6 py-3 rounded-sm font-label text-xs uppercase tracking-widest font-bold hover:bg-secondary-container transition-colors">Tech Maintenance</button>
        <button class="bg-surface-container-high text-secondary px-6 py-3 rounded-sm font-label text-xs uppercase tracking-widest font-bold hover:bg-secondary-container transition-colors">Creative Illustration</button>
      </div>
    </section>

    <section class="px-8 py-20 max-w-7xl mx-auto space-y-32">
      <div class="space-y-12">
        <div class="flex items-center gap-4">
          <div class="h-px bg-outline-variant flex-grow opacity-30"></div>
          <h2 class="text-primary font-headline font-bold text-2xl">Enterprise Office Digitization</h2>
          <div class="h-px bg-outline-variant flex-grow opacity-30"></div>
        </div>
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">
          <div class="lg:col-span-7 bg-surface-container-lowest overflow-hidden">
            <img class="w-full aspect-video object-cover grayscale hover:grayscale-0 transition-all duration-500" src="/images/modern-office.jpg" alt="Modern office"/>
          </div>
          <div class="lg:col-span-5 space-y-8">
            <div>
              <span class="text-primary-container font-label text-[10px] uppercase tracking-widest font-bold">Featured Case: Logistics Giant</span>
              <h3 class="text-3xl font-headline font-bold text-primary mt-2">Zero-Paper Transition</h3>
            </div>
            <div class="grid grid-cols-1 gap-6">
              <div class="p-6 bg-surface-container-low">
                <h4 class="font-label text-xs uppercase tracking-widest text-primary font-bold mb-2">Client Goal</h4>
                <p class="text-secondary text-sm">To eliminate manual document processing for 500+ daily shipments and reduce reporting lag from 48 hours to real-time.</p>
              </div>
              <div class="p-6 bg-primary-container text-on-primary">
                <h4 class="font-label text-xs uppercase tracking-widest text-on-primary-container font-bold mb-2">Solvia Solution</h4>
                <p class="text-sm">Engineered a custom cloud-based ERP with automated OCR scanning and secure digital signatures, unifying three regional databases.</p>
              </div>
              <div class="flex justify-between items-center px-4">
                <div class="text-center">
                  <span class="block text-2xl font-headline font-bold text-primary">94%</span>
                  <span class="text-[10px] uppercase font-label text-secondary">Efficiency Gain</span>
                </div>
                <div class="text-center">
                  <span class="block text-2xl font-headline font-bold text-primary">0%</span>
                  <span class="text-[10px] uppercase font-label text-secondary">Data Loss</span>
                </div>
                <div class="text-center">
                  <span class="block text-2xl font-headline font-bold text-primary">Real-time</span>
                  <span class="text-[10px] uppercase font-label text-secondary">Reporting</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="space-y-12">
        <div class="flex items-center gap-4">
          <div class="h-px bg-outline-variant flex-grow opacity-30"></div>
          <h2 class="text-primary font-headline font-bold text-2xl">Local E-commerce Sites</h2>
          <div class="h-px bg-outline-variant flex-grow opacity-30"></div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
          <div class="group">
            <div class="relative overflow-hidden bg-surface-container-high aspect-[4/3] mb-6">
              <img class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-500 scale-105 group-hover:scale-100" src="/images/case-retail-shop.jpg" alt="Bakery storefront"/>
              <div class="absolute bottom-4 left-4 right-4 bg-white/90 backdrop-blur p-6 shadow-sm">
                <h3 class="font-headline font-bold text-xl text-primary">Artisan Bakery Storefront</h3>
                <p class="text-secondary text-xs font-label uppercase tracking-widest mt-1">From Local Stall to Global Shipping</p>
              </div>
            </div>
            <div class="grid grid-cols-2 gap-4">
              <div class="p-4 border-l-2 border-primary-container">
                <span class="text-[10px] uppercase font-label text-secondary block">Before</span>
                <p class="text-sm font-medium">Phone-only orders, inconsistent stock tracking.</p>
              </div>
              <div class="p-4 border-l-2 border-primary">
                <span class="text-[10px] uppercase font-label text-primary block">After</span>
                <p class="text-sm font-medium">300% increase in weekly sales via automated web-shop.</p>
              </div>
            </div>
          </div>
          <div class="group">
            <div class="relative overflow-hidden bg-surface-container-high aspect-[4/3] mb-6">
              <img class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-500 scale-105 group-hover:scale-100" src="/images/case-dashboard.jpg" alt="Fresh market"/>
              <div class="absolute bottom-4 left-4 right-4 bg-white/90 backdrop-blur p-6 shadow-sm">
                <h3 class="font-headline font-bold text-xl text-primary">FreshMarket Express</h3>
                <p class="text-secondary text-xs font-label uppercase tracking-widest mt-1">Next-Day Delivery Logistics</p>
              </div>
            </div>
            <div class="grid grid-cols-2 gap-4">
              <div class="p-4 border-l-2 border-primary-container">
                <span class="text-[10px] uppercase font-label text-secondary block">Before</span>
                <p class="text-sm font-medium">Manual route planning, high delivery error rates.</p>
              </div>
              <div class="p-4 border-l-2 border-primary">
                <span class="text-[10px] uppercase font-label text-primary block">After</span>
                <p class="text-sm font-medium">AI-routed delivery app reducing fuel costs by 22%.</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="space-y-12">
        <div class="flex items-center gap-4">
          <div class="h-px bg-outline-variant flex-grow opacity-30"></div>
          <h2 class="text-primary font-headline font-bold text-2xl">Tech Support &amp; Maintenance</h2>
          <div class="h-px bg-outline-variant flex-grow opacity-30"></div>
        </div>
        <div class="bg-primary text-on-primary p-12 relative overflow-hidden">
          <div class="relative z-10 max-w-3xl">
            <span class="bg-primary-container text-on-primary-container px-3 py-1 text-[10px] font-bold uppercase tracking-widest rounded-full">Managed Reliability</span>
            <h3 class="text-4xl font-headline font-bold mt-6 mb-4 tracking-tight">24/7 Stability for Financial Firm "Alpha &amp; Co"</h3>
            <p class="text-lg text-on-primary-container mb-8">Providing end-to-end server maintenance and proactive security monitoring for a high-volume trading firm.</p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
              <div>
                <h4 class="font-label text-xs uppercase tracking-widest text-on-primary font-bold mb-2">The Challenge</h4>
                <p class="text-sm opacity-80 leading-relaxed">Frequent downtime during peak market hours and outdated firewall protocols risking sensitive client data.</p>
              </div>
              <div>
                <h4 class="font-label text-xs uppercase tracking-widest text-on-primary font-bold mb-2">The Solvia Standard</h4>
                <p class="text-sm opacity-80 leading-relaxed">Implemented redundant server clusters and a military-grade encryption layer with 15-minute response SLA.</p>
              </div>
            </div>
            <div class="mt-12 flex gap-8 border-t border-primary-container pt-8">
              <div>
                <span class="block text-3xl font-headline font-bold">99.99%</span>
                <span class="text-[10px] uppercase font-label opacity-60">Uptime Record</span>
              </div>
              <div>
                <span class="block text-3xl font-headline font-bold">0</span>
                <span class="text-[10px] uppercase font-label opacity-60">Security Breaches</span>
              </div>
            </div>
          </div>
          <div class="absolute right-[-10%] top-[-20%] opacity-10">
            <span class="material-symbols-outlined text-[400px]">security</span>
          </div>
        </div>
      </div>

      <div class="space-y-12">
        <div class="flex items-center gap-4">
          <div class="h-px bg-outline-variant flex-grow opacity-30"></div>
          <h2 class="text-primary font-headline font-bold text-2xl">Original Creative Illustration</h2>
          <div class="h-px bg-outline-variant flex-grow opacity-30"></div>
        </div>
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <div class="bg-surface-container-low p-8 group hover:bg-white transition-colors">
            <img class="w-full aspect-square object-cover mb-6" src="/images/case-office-workflow.jpg" alt="Cyber identity"/>
            <h4 class="font-headline font-bold text-xl text-primary">Cyber-Identity Package</h4>
            <p class="text-sm text-secondary mt-2">Custom iconography and visual language for a cybersecurity startup needing an 'approachable' tech look.</p>
          </div>
          <div class="bg-surface-container-low p-8 group hover:bg-white transition-colors">
            <img class="w-full aspect-square object-cover mb-6" src="/images/office-meeting.jpg" alt="Educational storyboards"/>
            <h4 class="font-headline font-bold text-xl text-primary">Educational Storyboards</h4>
            <p class="text-sm text-secondary mt-2">A series of 50+ hand-drawn digital illustrations for a medical training application, simplifying complex anatomy.</p>
          </div>
          <div class="bg-surface-container-low p-8 group hover:bg-white transition-colors">
            <img class="w-full aspect-square object-cover mb-6" src="/images/hero-team.jpg" alt="Data visual narrative"/>
            <h4 class="font-headline font-bold text-xl text-primary">Data-Visual Narrative</h4>
            <p class="text-sm text-secondary mt-2">Converting dry annual reports into a compelling visual journey using bespoke vector illustrations.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="max-w-7xl mx-auto px-8 mb-24">
      <div class="bg-surface-container-low p-16 md:p-24 text-center">
        <h2 class="text-4xl md:text-5xl font-headline font-extrabold text-primary mb-6">Ready to Architect Your Success?</h2>
        <p class="text-secondary text-lg max-w-2xl mx-auto mb-10">Every project starts with a conversation. Let's discuss how Solvia One can bring technical precision to your next big move.</p>
        <div class="flex flex-col sm:flex-row justify-center gap-4">
          <router-link to="/contact" class="bg-primary text-on-primary px-10 py-4 font-bold rounded-sm hover:opacity-90 transition-opacity uppercase tracking-widest text-sm">Schedule a Consultation</router-link>
          <router-link to="/services" class="bg-surface-container-high text-primary px-10 py-4 font-bold rounded-sm hover:bg-secondary-container transition-colors uppercase tracking-widest text-sm">View All Services</router-link>
        </div>
      </div>
    </section>
  </main>
</template>

<script setup>
</script>
