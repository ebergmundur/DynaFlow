<template>
  <q-header elevated class="bg-primary text-white row" height-hint="198">
    <q-tabs align="left" class="col-lg">
      <q-route-tab to="/" label="">
        <q-avatar class="q-ma-md">
          <img src="../assets/enam-logo.svg">
        </q-avatar>
      </q-route-tab>

      <q-route-tab to="/createtest" label="Æfingar"/>
      <q-route-tab to="/testpractice" label="Æfing"/>
      <q-route-tab to="/testreal" label="Próf"/>
      <q-route-tab to="/review" label="Niðurstöður"/>
      <q-route-tab to="/flipcard" label="Flettikort"/>
      <q-route-tab to="/dashboard" label="Mælaborð"/>

      <q-route-tab v-if="!loggedIn" to="/login" label="Login"/>
      <q-route-tab v-if="!loggedIn" to="/register" label="Register"/>
      <q-route-tab v-if="loggedIn" to="/userinfo" :label="user"/>
      <q-route-tab v-if="loggedIn" to="/logout" label="Logout"/>

    </q-tabs>

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

// import { mapState } from 'vuex'

export default {
  name: 'Header',
  components: {
  //   Clock
  },
  data () {
    return {
      loggedIn: false,
      user: ''

    }
  },
  // computed: mapState(['accessToken', 'userName']),
  computed: {

    // this.loggedIn = index.getters.loggedIn
    // this.user = index.getters.getUserName
  },
  mounted () {
    this.loggedIn = store.getters.loggedIn
    this.user = store.getters.getUserName
  }
}

</script>

<style scoped>

</style>
