import Vue from 'vue'
import VueRouter from 'vue-router'
import IdleVue from 'idle-vue'
// import App from 'src/App.vue'
// import MainLayout from 'src/layouts/MainLayout'
import store from 'src/store'
import routes from './routes'

const eventsHub = new Vue()

Vue.use(VueRouter)

Vue.use(IdleVue, {
  eventEmitter: eventsHub,
  idleTime: 12 * 60000
}) // sets up the idle time,i.e. time left to logout the user on no activity
Vue.config.productionTip = true

var router

export default function (/* { store, ssrContext } */) {
  router = new VueRouter({
    mode: 'hash',
    base: process.env.VUE_ROUTER_BASE,
    routes: routes
  })
  router.beforeEach((to, from, next) => {
  // if any of the routes in ./router.js has a meta named 'requiresAuth: true'
  // then check if the user is logged in before routing to this path:
    if (to.matched.some(record => record.meta.requiresAuth)) {
      // console.log('login IS requried')
      if (!store.getters.loggedIn) {
        next({ name: 'login' })
      } else {
        next()
        // console.log('login NOT requried')
      }
    } else if (to.matched.some(record => record.meta.requiresLogged)) {
      // else if any of the routes in ./router.js has a meta named 'requiresLogged: true'
      // then check if the user is logged in; if true continue to home page else continue routing to the destination path
      // this comes to play if the user is logged in and tries to access the login/register page
      if (store.getters.loggedIn) {
        next({ name: 'home' })
      } else {
        next()
      }
    } else {
      next()
    }
  })
  return router
}

// router.beforeEach((to, from, next) => {
//   if (to.path === '/createtest') {
//     next(false)
//   } else {
//     next()
//   }
//   console.log('login IS requried')
// })

// window.app = new Vue({
//   router: this.router,
//   render: h => h('#q-app')
// })

// this.router.beforeEach((to, from, next) => {
//   // if any of the routes in ./router.js has a meta named 'requiresAuth: true'
//   // then check if the user is logged in before routing to this path:
// if (to.matched.some(record => record.meta.requiresAuth)) {
//   // console.log('login IS requried')
//   if (!store.getters.loggedIn) {
//     next({ name: 'login' })
//   } else {
//     next()
//     // console.log('login NOT requried')
//   }
// } else if (to.matched.some(record => record.meta.requiresLogged)) {
//   // else if any of the routes in ./router.js has a meta named 'requiresLogged: true'
//   // then check if the user is logged in; if true continue to home page else continue routing to the destination path
//   // this comes to play if the user is logged in and tries to access the login/register page
//   if (store.getters.loggedIn) {
//     next({ name: 'home' })
//   } else {
//     next()
//   }
// } else {
//   next()
// }
// })
