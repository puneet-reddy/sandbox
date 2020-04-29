import Vue from 'vue'
import App from './App.vue'
import {BootstrapVue, IconsPlugin} from 'bootstrap-vue';

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

Vue.config.productionTip = false

Vue.use(BootstrapVue);
Vue.use(IconsPlugin);


const NotFound = { template: '<p>Page not found</p>'}
const Home = {template: '<p>Home page goes here</p>'}

const routes = {
  '/': Home,
  '/about': App
}

new Vue({
  el: '#app',
  data: {
    currentRoute: window.location.pathname
  },
  computed: {
    ViewComponent() {
      return routes[this.currentRoute] || NotFound
    }
  },
  render (h) {return h(this.ViewComponent)}
})
