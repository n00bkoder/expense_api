import Vue from 'vue'
import App from './App.vue'
import VueFilterDateFormat from '@vuejs-community/vue-filter-date-format';

Vue.use(VueFilterDateFormat);

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
