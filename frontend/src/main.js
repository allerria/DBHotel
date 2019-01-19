import Vue from 'vue'
import App from './App.vue'
import Datatable from 'vue2-datatable-component'

Vue.use(Datatable)
Vue.config.productionTip = false

new Vue({
    render: h => h(App),
}).$mount('#app')
