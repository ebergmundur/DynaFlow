import Vue from 'vue'
import store from './store'
// import Router from './router'
import VueRouter from 'vue-router'
// import App from '../App.vue'

Vue.use(VueRouter)

import routes from './routes'

// import { mapGetters } from 'vuex'

export default function (/* { store, ssrContext } */) {
  const Router = new VueRouter({
    scrollBehavior: () => ({ x: 0, y: 0 }),
    routes,
    store,
    // Leave these as they are and change in quasar.conf.js instead!
    // quasar.conf.js -> build -> vueRouterMode
    // quasar.conf.js -> build -> publicPath
    mode: process.env.VUE_ROUTER_MODE,
    base: process.env.VUE_ROUTER_BASE
  })

  return Router
}

// new Vue({
//   routes,
//   store,
//   // Router,
//   // computed: mapState([
//   //   'currentQestion'
//   // ]),
//   // computed: mapState({
//   //   // currQest: state => state.currentQuestion,
//   //   // currQuestAlias: 'currentQuestion'
//   //   currQestAlias () {
//   //     return this.$store.getters.currQest
//   //   }
//   // computed: mapGetters([
//   //   'currQest'
//   // ]),
//   render: h => h(App)
// }).$mount('#q-app')

// export default {
//   store,
//   Router
// }
