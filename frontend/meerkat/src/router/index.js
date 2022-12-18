import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import subdomainView from '../views/subdomainView.vue'
import wordlistView from '../views/wordlistView'
import LoginView from '../views/Login'
import RegisterView from '../views/Register'

Vue.use(VueRouter)

const routes = [{
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
    }, {
        path: '/login',
        name: 'Login',
        component: LoginView
    },
    {
        path: '/register',
        name: 'Register',
        component: RegisterView
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router