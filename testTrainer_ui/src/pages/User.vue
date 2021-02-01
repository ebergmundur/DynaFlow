<template>
  <q-page class="flex q-pa-xs ">
    <div class="row">
      <q-card class="my-card absolute-center col-12">
        <q-toolbar class="q-dark">
          <q-toolbar-title>
            {{ userInfo.firstName }} {{ userInfo.lastName }}
          </q-toolbar-title>
        </q-toolbar>
        <q-card-section>
          <!-- <div class="row items-center wrap q-gutter-md"> -->
          <!--    <q-list bordered class="rounded-borders" style="max-width: 1600px">-->
            <q-item>
              <q-item-section avatar top>
                <q-icon class="" name="person" size="38px"/>
              </q-item-section>
              <q-item-section top>
                <q-item-label class="q-mt-sm">{{ user }} - {{ userInfo.firstName }} {{ userInfo.lastName }}</q-item-label>
              </q-item-section>
            </q-item>
        </q-card-section>

        <q-card-section>
          <q-toolbar>
            <q-toolbar-title>
              Yfirlit um stöðu
            </q-toolbar-title>
          </q-toolbar>
          <q-item>
              <q-item-section top>
                <q-item-label lines="1">
                  <span class="">Áskrift til {{ format_date(userInfo.until) }}
                    {{userInfo.open}}
                  </span>
                </q-item-label>
                <q-item-label caption lines="1">
                  Sjálfvirk endurnýjun í gangi
                </q-item-label>
              </q-item-section>
                </q-item>
          </q-card-section>

          <q-card-section>
            <q-toolbar>
              <q-toolbar-title>
                Ástundun
              </q-toolbar-title>
            </q-toolbar>
            <div class="" style="height: 300px;">
              <Heatmap></Heatmap>
            </div>
          </q-card-section>

          <q-card-section>
                      <q-toolbar>
            <q-toolbar-title>
              Dark mode stilling
            </q-toolbar-title>
          </q-toolbar>
            <div>
              <q-toggle v-model="systemDark" toggle-color="primary" @input="setdarkauto" label="Fylgja tölvu" />
              <q-toggle v-model="dark" ref="mandark" toggle-color="primary" @input="setdark" label="Handvirkt" />
            </div>
            <!-- <q-separator spaced/> -->
          </q-card-section>
      </q-card>
    </div>
  </q-page>
</template>
input
<script>
import store from 'src/store'
import { date } from 'quasar'
import Heatmap from 'components/Heatmap'
// import axios from 'axios'
import { getAPI } from 'src/api/axios-base'

// const timeStamp = Date.now()

export default {
  name: 'User',
  components: {
    Heatmap
  },
  data () {
    return {
      // loggedIn: false,
      token: null,
      Heatmap: Heatmap,
      userId: 0,
      firstName: '',
      lastName: '',
      email: '',
      dark: null,
      systemDark: null
    }
  },
  methods: {
    setdark () {
      console.log('setdark')
      // this.$q.dark.set(false)
      if (this.dark === false) {
        this.dark = false
        store.commit('setDarkMode', false)
        this.$q.dark.set(false)
      } else if (this.dark === true) {
        this.$q.dark.set(true)
        this.dark = true
        this.systemDark = false
        store.commit('setDarkMode', true)
        store.commit('setSystemDarkMode', false)
      }
      this.update_prefs()
    },
    setdarkauto () {
      console.log('setdarkauto')
      if (this.systemDark === false) {
        this.$q.dark.set(false)
        this.systemDark = false
        this.dark = false
        store.commit('setDarkMode', false)
        store.commit('setSystemDarkMode', true)
      } else if (this.systemDark === true) {
        this.$q.dark.set('auto')
        this.systemDark = true
        this.dark = false
        store.commit('setDarkMode', false)
        store.commit('setSystemDarkMode', true)
      }
      this.update_prefs()
    },
    format_date (d) {
      return date.formatDate(d, 'DD. MMMM YYYY', {
        months: ['janúar', 'febrúar', 'mars', 'apríl', 'maí', 'júní', 'júlí', 'ágúst', 'september', 'október', 'nóvember', 'desember']
      })
    },
    count_days (d) {
      const date = new Date()
      const restofdays = date.subtractFromDate(date, d)
      return restofdays
    },
    update_prefs () {
      if (this.loggedIn) {
        const access = store.getters.token
        getAPI({
          data: {
            system_dark_mode: this.systemDark,
            dark_mode: this.dark,
            username: this.user
          },
          method: 'post',
          headers: { Authorization: `Bearer ${access}` }, // the new access token is attached to the authorization header
          url: '/api/prefs/'
        })
          .then(response => {
            console.log('set prefs')
            console.log(response)
          })
      }
    }
  },
  // computed: mapState(['accessToken', 'userName']),
  computed: {
    loggedIn () {
      return store.getters.loggedIn
    },
    user () {
      return store.getters.getUserName
    },
    userInfo () {
      return store.getters.getUserInfo
    },
    userDark () {
      return store.getters.getDarkMode
    },
    userSystemDark () {
      return store.getters.getSystemDarkMode
    }
  },
  mounted () {
    if (this.loggedIn) {
      const access = store.getters.token
      getAPI({
        data: { username: this.user },
        method: 'post',
        headers: { Authorization: `Bearer ${access}` }, // the new access token is attached to the authorization header
        url: '/api/userinfo/'
      })
        .then(response => {
          console.log('response')
          console.log(response)
          this.systemDark = response.data.prefs_system_dark_mode
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

          store.commit('setUserId', response.data.id)
          store.commit('setUserFirstName', response.data.first_name)
          store.commit('setUserLastName', response.data.last_name)
          store.commit('setUserEmail', response.data.email)
          store.commit('setUserEndDay', response.data.until)
          store.commit('setUserOpen', response.data.open)
          store.commit('setUserIsadmin', response.data.isadmin)
          store.commit('setDarkMode', response.data.prefs_dark_mode)
          store.commit('setSystemDarkMode', response.data.prefs_system_dark_mode)
        })
    }
  }
}

</script>

<style scoped>

</style>
