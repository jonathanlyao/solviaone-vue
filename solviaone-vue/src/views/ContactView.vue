<template>
  <main class="bg-background text-on-background font-body pt-32 pb-24">
    <section class="max-w-7xl mx-auto px-8 mb-20">
      <div class="grid grid-cols-1 md:grid-cols-12 gap-8 items-end">
        <div class="md:col-span-8">
          <span class="text-primary font-headline font-bold tracking-[0.2em] text-xs uppercase mb-4 block">Get In Touch</span>
          <h1 class="text-primary font-headline font-extrabold text-5xl md:text-7xl tracking-tighter leading-tight">
            Architecture of <br/><span class="text-on-primary-container">Reliability.</span>
          </h1>
        </div>
        <div class="md:col-span-4 pb-2">
          <p class="text-secondary font-body text-lg leading-relaxed border-l-2 border-primary-container pl-6">
            Expert consultation for digital infrastructure. Reach out to our team of architects today.
          </p>
        </div>
      </div>
    </section>

    <section class="max-w-7xl mx-auto px-8 mb-24">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div class="lg:col-span-2 bg-surface-container-lowest p-8 md:p-12 rounded-xl shadow-sm">
          <h2 class="font-headline font-bold text-2xl text-primary mb-8">Send a Message</h2>
          <form @submit.prevent="handleSubmit" class="space-y-6">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div class="space-y-2">
                <label class="text-xs font-bold uppercase tracking-wider text-secondary">Full Name</label>
                <input v-model="formData.name" class="w-full bg-surface-container-low border-none rounded-lg p-4 focus:ring-2 focus:ring-primary/20 text-on-surface" placeholder="John Doe" type="text" required/>
              </div>
              <div class="space-y-2">
                <label class="text-xs font-bold uppercase tracking-wider text-secondary">Phone Number</label>
                <input v-model="formData.phone" class="w-full bg-surface-container-low border-none rounded-lg p-4 focus:ring-2 focus:ring-primary/20 text-on-surface" placeholder="+1 (555) 000-0000" type="tel"/>
              </div>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div class="space-y-2">
                <label class="text-xs font-bold uppercase tracking-wider text-secondary">Company</label>
                <input v-model="formData.company" class="w-full bg-surface-container-low border-none rounded-lg p-4 focus:ring-2 focus:ring-primary/20 text-on-surface" placeholder="Organization Name" type="text"/>
              </div>
              <div class="space-y-2">
                <label class="text-xs font-bold uppercase tracking-wider text-secondary">Service Type</label>
                <select v-model="formData.serviceType" class="w-full bg-surface-container-low border-none rounded-lg p-4 focus:ring-2 focus:ring-primary/20 text-on-surface appearance-none">
                  <option>Infrastructure Design</option>
                  <option>Security Audit</option>
                  <option>Cloud Migration</option>
                  <option>Managed Services</option>
                </select>
              </div>
            </div>
            <div class="space-y-2">
              <label class="text-xs font-bold uppercase tracking-wider text-secondary">Your Message</label>
              <textarea v-model="formData.message" class="w-full bg-surface-container-low border-none rounded-lg p-4 focus:ring-2 focus:ring-primary/20 text-on-surface" placeholder="Tell us about your project requirements..." rows="5" required></textarea>
            </div>
            <div class="pt-4">
              <button class="bg-primary text-on-primary px-10 py-4 rounded-lg font-headline font-bold text-sm tracking-wide transition-all hover:shadow-lg active:scale-95 w-full md:w-auto" type="submit">
                SEND MESSAGE
              </button>
            </div>
          </form>
        </div>

        <div class="space-y-8">
          <div class="bg-primary-container p-8 rounded-xl text-on-primary">
            <h3 class="font-headline font-bold text-xl mb-6 text-on-primary-container">Contact Details</h3>
            <div class="space-y-6">
              <div class="flex items-start gap-4">
                <span class="material-symbols-outlined text-on-primary-container">call</span>
                <div>
                  <p class="text-xs uppercase font-bold tracking-widest opacity-60 mb-1">Call Us</p>
                  <p class="font-headline font-bold">+1(929)608-6298</p>
                </div>
              </div>
              <div class="flex items-start gap-4">
                <span class="material-symbols-outlined text-on-primary-container">mail</span>
                <div>
                  <p class="text-xs uppercase font-bold tracking-widest opacity-60 mb-1">Email Us</p>
                  <p class="font-headline font-bold">vicky@solvia-one.com</p>
                </div>
              </div>
              <div class="flex items-start gap-4">
                <span class="material-symbols-outlined text-on-primary-container">location_on</span>
                <div>
                  <p class="text-xs uppercase font-bold tracking-widest opacity-60 mb-1">Visit Us</p>
                  <p class="font-headline font-bold">24850 Van Zandt Ave.Little Neck NY 11362</p>
                </div>
              </div>
            </div>
          </div>

          <div class="bg-surface-container p-8 rounded-xl">
            <div class="flex items-center gap-3 mb-4 text-primary">
              <span class="material-symbols-outlined">schedule</span>
              <h3 class="font-headline font-bold text-lg">Working Hours</h3>
            </div>
            <div class="flex justify-between items-center py-3 border-b border-outline-variant/30">
              <span class="text-secondary font-medium">Mon - Fri</span>
              <span class="text-primary font-bold">9:00 AM - 6:00 PM</span>
            </div>
            <div class="flex justify-between items-center py-3">
              <span class="text-secondary font-medium">Sat - Sun</span>
              <span class="text-on-surface-variant italic">Closed</span>
            </div>
          </div>

          <button class="w-full bg-surface-container-high text-primary font-bold py-5 rounded-xl flex items-center justify-center gap-3 transition-colors hover:bg-primary hover:text-on-primary group">
            <span class="material-symbols-outlined">event_available</span>
            Book an On-site Appointment
            <span class="material-symbols-outlined text-sm transition-transform group-hover:translate-x-1">arrow_forward</span>
          </button>
        </div>
      </div>
    </section>

    <section class="w-full bg-surface-container-low py-24 overflow-hidden">
      <div class="max-w-7xl mx-auto px-8">
        <div class="grid grid-cols-1 md:grid-cols-12 gap-12 items-center">
          <div class="md:col-span-4">
            <h2 class="font-bold text-4xl text-primary mb-6 leading-tight">Our Global <br/>Hub.</h2>
            <p class="text-secondary mb-8 leading-relaxed">Located in Little Neck, NY, our headquarters serve as the central node for our global infrastructure operations.</p>
            <a href="https://www.google.com/maps/dir/?api=1&destination=24850+Van+Zandt+Ave+Little+Neck+NY+11362" target="_blank" rel="noopener noreferrer" class="flex items-center gap-2 text-primary font-bold hover:underline">
              <span class="material-symbols-outlined">directions</span>
              <span>Get Directions</span>
            </a>
          </div>
          <div class="md:col-span-8 relative">
            <div class="aspect-video bg-surface-container-highest rounded-xl overflow-hidden shadow-xl ring-8 ring-surface-container-lowest/50">
              <iframe 
                src="https://www.google.com/maps?q=24850+Van+Zandt+Ave+Little+Neck+NY+11362&output=embed&z=15"
                width="100%" 
                height="100%" 
                style="border:0;" 
                allowfullscreen="" 
                loading="lazy" 
                referrerpolicy="no-referrer-when-downgrade"
                class="w-full h-full"
              ></iframe>
              <div class="absolute bottom-6 left-6 bg-white/90 backdrop-blur p-4 rounded-lg shadow-lg border-l-4 border-primary">
                <p class="text-xs font-bold text-secondary uppercase tracking-widest mb-1">Little Neck, NY</p>
                <p class="text-primary font-bold">24850 Van Zandt Ave, NY 11362</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script setup>
import { reactive } from 'vue'

const formData = reactive({
  name: '',
  phone: '',
  company: '',
  serviceType: 'Infrastructure Design',
  message: ''
})

const handleSubmit = () => {
  alert('Thank you for your message! We will get back to you soon.')
  formData.name = ''
  formData.phone = ''
  formData.company = ''
  formData.serviceType = 'Infrastructure Design'
  formData.message = ''
}
</script>