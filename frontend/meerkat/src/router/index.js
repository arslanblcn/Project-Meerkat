import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import subdomainView from '../views/subdomainView.vue'
import wordlistView from '../views/wordlistView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/subdomain',
    name: 'subdomain',
    component: subdomainView
  },
  {
    path: '/createWordlist',
    name: 'createWordlist',
    component: wordlistView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
