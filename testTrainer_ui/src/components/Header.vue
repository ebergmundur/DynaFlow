<template>
  <q-header elevated class="bg-primary text-white row" height-hint="198">
    <div class="q-gutter-y-sm q-gutter-x-sm">
      <q-tabs
        align="left"
        inline-label
        dense
      >
        <q-route-tab to="/" label="">
          <q-avatar class="q-ma-md">
            <img src="../assets/enam-logo.svg">
          </q-avatar>
        </q-route-tab>

        <q-route-tab v-if="loggedIn" to="/createtest" label="Æfing"/>
        <q-route-tab v-if="loggedIn" to="/testpractice" label="Æ"/>
        <q-route-tab v-if="loggedIn" to="/testreal" label="Próf"/>
        <q-route-tab v-if="loggedIn" to="/review" label="Niðurstöður"/>
        <q-route-tab v-if="loggedIn" to="/flipcard" label="Flettikort"/>
        <q-route-tab v-if="loggedIn" to="/dashboard" label="Mælaborð"/>

        <q-route-tab v-if="!loggedIn" to="/login" label="Login" class="no-wrap">
          <q-icon v-if="!loggedIn" class="fa fa-user-alt nowrap q-ml-sm"/>
        </q-route-tab>
        <q-route-tab v-if="!loggedIn" to="/register" icon="user" label="Register"/>
        <q-route-tab v-if="loggedIn" to="/userinfo" :label=user.firstName>
          <q-icon v-if="loggedIn" class="fa fa-user-alt nowrap q-ml-sm"/>
        </q-route-tab>
        <q-route-tab v-if="loggedIn" to="/logout" label="Logout"/>
      </q-tabs>
    </div>

    <!--        <div class="nav-bar">-->
    <!--          <ul>-->
    <!--            <li v-if="accessToken==null">-->
    <!--              <routerJs-link :to="{ name:'register' }">REGISTER</routerJs-link>-->
    <!--            </li>-->
    <!--            <li v-if="accessToken==null">-->
    <!--              <routerJs-link :to="{ name:'login' }">LOGIN</routerJs-link>-->
    <!--            </li>-->
    <!--            <li v-if="accessToken!=null">-->
    <!--              <routerJs-link :to="{ name:'logout' }">LOGOUT</routerJs-link>-->
    <!--            </li>-->
    <!--          </ul>-->
    <!--        </div>-->
    <!--    <clock></clock>-->
  </q-header>
</template>

<script>
// import Clock from 'components/Clock'
import store from 'src/store'
// import axios from 'axios'
import { getAPI } from 'src/api/axios-base'

// import { mapState } from 'vuex'

export default {
  name: 'Header',
  components: {
    //   Clock
  },
  data () {
    return {
      // loggedIn: false,
      // user: ''

    }
  },
  // computed: mapState(['accessToken', 'userName']),
  computed: {
    loggedIn () {
      return store.getters.loggedIn
    },
    user () {
      return store.getters.getUserInfo
    }

    // firstName () {
    //   return store.getters.getUserFirstName
    // },
    // lastName () {
    //   return store.getters.getUserLastName
    // },
    // email () {
    //   return store.getters.getUserEmail
    // }

    // this.loggedIn = index.getters.loggedIn
    // this.user = index.getters.getUserName
  },
  mounted () {
    // if (!store.getters.getUserName) {
    const access = store.getters.token
    // axios({
    //   data: { username: this.user },
    //   method: 'post',
    //   headers: { Authorization: `Bearer ${access}` }, // the new access token is attached to the authorization header
    //   url: 'https://einars-macbook-pro.local:8000/userdata/'
    // })
    getAPI({
      data: { username: this.user },
      method: 'post',
      headers: { Authorization: `Bearer ${access}` }, // the new access token is attached to the authorization header
      url: '/api/userinfo/'
    })
      .then(response => {
        // console.log(response)
        store.commit('setUserId', response.data.id)
        store.commit('setUserFirstName', response.data.first_name)
        store.commit('setUserLastName', response.data.last_name)
        store.commit('setUserEmail', response.data.email)
        store.commit('setUserEndDay', response.data.until)
        store.commit('setUserOpen', response.data.open)
        store.commit('setUserIsadmin', response.data.isadmin)
      })
  }
  // this.loggedIn = store.getters.loggedIn
  // this.user = store.getters.getUserName
  // }
}

</script>

<style scoped>

</style>
