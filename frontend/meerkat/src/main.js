import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import VueApexCharts from 'vue-apexcharts'
import mdiVue from 'mdi-vue/v2'
import * as mdijs from '@mdi/js'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(mdiVue, {
    icons: mdijs
})

Vue.use(VueApexCharts)
Vue.use(VueAxios, axios)


Vue.component('apex-chart', VueApexCharts)
Vue.config.productionTip = false

new Vue({
    router,
    store,
    vuetify,
    render: h => h(App)
}).$mount('#app')