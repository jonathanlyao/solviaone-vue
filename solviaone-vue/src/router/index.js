import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import ContactView from '../views/ContactView.vue'
import ServicesView from '../views/ServicesView.vue'
import NewsView from '../views/NewsView.vue'
import AdvantagesView from '../views/AdvantagesView.vue'
import CasesView from '../views/CasesView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView
    },
    {
      path: '/contact',
      name: 'contact',
      component: ContactView
    },
    {
      path: '/services',
      name: 'services',
      component: ServicesView
    },
    {
      path: '/news',
      name: 'news',
      component: NewsView
    },
    {
      path: '/advantages',
      name: 'advantages',
      component: AdvantagesView
    },
    {
      path: '/cases',
      name: 'cases',
      component: CasesView
    }
  ],
  scrollBehavior() {
    return { top: 0 }
  }
})

export default router