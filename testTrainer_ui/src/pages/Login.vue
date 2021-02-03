<template>
  <q-page class="flex flex-center q-pa-xs ">
  <div class="q-pa-md row items-start q-gutter-md">
    <q-card
      class="my-card bg-grey-1 absolute-center col-xs-12 col-xs-12 col-md-6 col-xl-4 col-lg-4"
    >
      <q-toolbar class="q-dark" style="background-color: #616161;">
        <q-toolbar-title>
          Innskráning
        </q-toolbar-title>
      </q-toolbar>
      <q-card-section>
        <div class="row items-center wrap q-gutter-md">
          <h4 v-if="wrongCred">Notendanafn, lykilorð eða hvorttveggja stenst ekki skoðun.

            <a href="/#/logout" >Logout</a>

          </h4>

          <!--          <form v-on:submit.prevent="loginUser">-->

            <q-input v-model="username" type="text" class="col-11" label="Notendanafn">
                                <template v-slot:before>
                    <q-icon class="fa fa-user-alt"/>
                  </template>
                </q-input>

            <q-input class="col-11" id="pass" type="password" v-model="password" label="Lykilorð">
                                <template v-slot:before>
                    <q-icon class="fa fa-key"/>
                  </template>
                </q-input>

          <!--          </form>-->
        </div>
      </q-card-section>
      <q-card-actions>
        <div class="q-gutter-md col">
          <!--          <button type="submit">Skrá inn</button>-->

          <q-btn
            color="positive"
            label="Skrá inn"
            style="float: right;"
            class="q-mr-none q-mb-md"
            @click="loginUser"

          />
        </div>
      </q-card-actions>
    </q-card>
  </div>
  </q-page>
</template>

<script>

import store from 'src/store'
import { getAPI } from 'src/api/axios-base'

export default {
  name: 'login',
  components: {
    // NavBar
  },
  data () {
    return {
      wdata: [],
      username: '',
      password: '',
      isPwd: true,
      wrongCred: false // activates appropriate message if set to true
    }
  },
  methods: {
    update () {
      const access = store.getters.token
      getAPI({
        data: { username: this.user },
        method: 'post',
        headers: { Authorization: `Bearer ${access}` }, // the new access token is attached to the authorization header
        url: '/api/userinfo/'
      })
        .then(response => {
          console.log('update')
          // console.log(response)
          this.wdata = response.data
          console.log(this.wdata)
          store.commit('setUserId', this.wdata.id)
          store.commit('setUserFirstName', this.wdata.first_name)
          store.commit('setUserLastName', this.wdata.last_name)
          store.commit('setUserEmail', this.wdata.email)
          store.commit('setUserEndDay', this.wdata.until)
          store.commit('setUserOpen', this.wdata.open)
          store.commit('setUserIsadmin', this.wdata.isadmin)
          store.commit('setDarkMode', this.wdata.prefs_dark_mode)
          store.commit('setSystemDarkMode', this.wdata.prefs_system_dark_mode)
          if (response.data.prefs_system_dark_mode) {
            console.log('system-true')
            this.$q.dark.set('auto')
            this.dark = false
            this.systemDark = true
          } else if (response.data.prefs_dark_mode) {
            console.log('user-true')
            this.$q.dark.set(true)
            this.dark = true
            this.systemDark = false
          } else {
            console.log('user-false')
            this.$q.dark.set(false)
            this.dark = false
            this.systemDark = false
          }
        })
        .then(() => {
          this.$router.push({ path: '/' })
        })
        .catch(err => {
          console.log(err)
          this.wrongCred = true // if the credentials were wrong set wrongCred to true
        })
    },
    loginUser () { // call loginUSer action
      this.$store.dispatch('loginUser', {
        username: this.username,
        password: this.password
      })
        .then(() => {
          this.wrongCred = false
        })
        .then(() => {
          this.update()
        })
        .catch(err => {
          console.log(err)
          this.wrongCred = true // if the credentials were wrong set wrongCred to true
        })
    }
  }
}
</script>

<style scoped>
</style>
