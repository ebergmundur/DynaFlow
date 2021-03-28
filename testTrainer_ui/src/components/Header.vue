<template>
  <q-header
    dark
    reveal
    elevated
    class="text-white row"
  >
    <div
      class="q-gutter-y-sm q-gutter-x-sm col"
      v-if="$q.platform.is.desktop"
    >
      <q-tabs
        dark
        align="left"
        inline-label
        class="float-left tabbar"
      >
        <q-route-tab
          to="/"
          label=""
          name="root"
        >
          <!--          E nám-->
          <q-avatar class="">
            <img
              src="../assets/enam-logo.svg"
              style="height: 40px; margin: 0;"
            >
          </q-avatar>
        </q-route-tab>

        <q-route-tab
          dark
          v-if="loggedIn"
          to="/createtest"
          label="Æfing"
        />
        <q-route-tab
          dark
          v-if="loggedIn"
          to="/testreal"
          label="Próf"
        />
        <q-route-tab
          dark
          v-if="loggedIn"
          to="/flipcard"
          label="Flettikort"
        />
        <q-route-tab
          dark
          v-if="!loggedIn"
          to="/about"
          label="Um vefinn"
        />
      </q-tabs>
      <!--        <q-icon v-if="loggedIn" class="fa fa-user-alt nowrap q-ml-sm"/>-->
      <q-tabs
        align="right"
        inline-label
        class="float-right tabbar"
        stretch
      >

        <q-route-tab
          v-if="!loggedIn"
          name="login"
          to="/login"
          label="Innskrá"
          @click="tab = 'login'"
        />
        <q-route-tab
          v-if="!loggedIn"
          name="register"
          to="/register"
          label="Nýskrá"
          @click="tab = 'register'"
        />
        <q-btn-dropdown
          auto-close
          stretch
          flat
          name="more"
          label="Mín gögn"
          style="float: right;"
          v-if="loggedIn"
        >
          <q-list>
            <q-item
              clickable
              @click="tab = 'more'"
            >
              <q-route-tab
                v-if="loggedIn"
                to="/userinfo"
                label="Áskrift"
              />
            </q-item>

            <!-- <q-item clickable @click="tab = 'more'">
              <q-route-tab v-if="loggedIn" to="/userinfo" label="Ástundun"/>
            </q-item> -->

            <q-item
              clickable
              @click="tab = 'more'"
            >
              <q-route-tab
                v-if="loggedIn"
                @click="tab = 'more'"
                to="/dashboard/allt"
                label="Mælaborð"
              />
            </q-item>

            <q-item
              clickable
              @click="tab = 'more'"
            >
              <q-route-tab
                v-if="loggedIn"
                @click="tab = 'review'"
                to="/review/0/"
                label="Úrlausnir"
              />
            </q-item>

            <q-item
              clickable
              @click="tab = 'more'"
            >
              <q-route-tab
                v-if="loggedIn"
                to="/about"
                label="Um vefinn"
              />
            </q-item>

            <q-item
              clickable
              @click="tab = 'more'"
            >
              <q-route-tab
                v-if="loggedIn"
                to="/logout"
                label="Logout"
              />
            </q-item>
          </q-list>
        </q-btn-dropdown>
      </q-tabs>
    </div>
    <div
      class="absolute-full flex"
      v-if="$q.platform.is.mobile"
    >
      <q-toolbar class="text-white bg-primary flex">
        <a href="/#">
        <img
          src="../assets/enam-logo.svg"
          style="height: 40px; margin: 0; width: auto;"
        >
        </a>
        <q-tabs
          align="right"
          inline-label
          style="float: right; margin-right: 1px; margin-left: auto;"
          class="items-end"
          stretch
        >
          <q-btn-dropdown
            auto-close
            stretch
            flat
            name="more"
            icon="menu"
          >
            <q-list>
              <q-item
              v-if="!loggedIn"
                clickable
                @click="tab = 'more'"
              >
                <q-route-tab
                  name="login"
                  to="/login"
                  label="Innskrá"
                  @click="tab = 'login'"
                />
              </q-item>

              <q-item
              v-if="!loggedIn"
                clickable
                @click="tab = 'more'"
              >
                <q-route-tab
                  name="register"
                  to="/register"
                  label="Nýskrá"
                  @click="tab = 'register'"
                />
              </q-item>

              <q-item
              v-if="loggedIn"
                clickable
                @click="tab = 'more'"
              >
                <q-route-tab
                  dark
                  to="/createtest"
                  label="Æfing"
                />
              </q-item>

              <q-item
                  v-if="loggedIn"
                clickable
                @click="tab = 'more'"
              >
                <q-route-tab
                  dark
                  to="/testreal"
                  label="Próf"
                />
              </q-item>

              <q-item
                  v-if="loggedIn"
                clickable
                @click="tab = 'more'"
              >
                <q-route-tab
                  dark
                  to="/flipcard"
                  label="Flettikort"
                />
              </q-item>

              <q-item
                  v-if="loggedIn"
                clickable
                @click="tab = 'more'"
              >
                <q-route-tab
                  to="/dashboard/allt"
                  label="Mælaborð"
                />
              </q-item>
              <q-item
                  v-if="loggedIn"
                clickable
                @click="tab = 'more'"
              >
                <q-route-tab
                  @click="tab = 'review'"
                  to="/review"
                  label="Úrlausnir"
                />
              </q-item>

              <q-item
                  v-if="loggedIn"
                clickable
                @click="tab = 'more'"
              >
                <q-route-tab
                  to="/about"
                  label="Um vefinn"
                />
              </q-item>

              <q-item
                  v-if="loggedIn"
                clickable
                @click="tab = 'more'"
              >
                <q-route-tab
                  to="/logout"
                  label="Logout"
                />
              </q-item>

            </q-list>
          </q-btn-dropdown>
        </q-tabs>
      </q-toolbar>
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
// import { getAPI } from 'src/api/axios-base'
// import Vue from 'vue'
// Vue.forceUpdate()

// import { mapState } from 'vuex'

export default {
  name: 'Header',
  components: {
    // Clock
  },
  data () {
    return {
      tab: 'root',
      dark: false,
      systemDark: false,
      data: []
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
      if (this.loggedIn) {
        return store.getters.getUserInfo
      } else {
        return null
      }
      // },
      // userDark () {
      //   return store.getters.getDarkMode
      // },
      // userSystemDark () {
      //   return store.getters.getSystemDarkMode
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
  beforeMount () {
    // console.log('beforeMount')
    // var loggg = true
    // console.log(loggg)
    // // if (this.loggedIn) {
    // if (loggg === true) {
    //   const access = store.getters.token
    //   getAPI({
    //     data: { username: this.user },
    //     method: 'post',
    //     headers: { Authorization: `Bearer ${access}` }, // the new access token is attached to the authorization header
    //     url: '/api/userinfo/'
    //   })
    //     .then(response => {
    //       // console.log('response')
    //       // console.log(response)
    //       this.data = response.data

    //       console.log('mounted')
    //       console.log(this.data)
    //       if (this.data.prefs_system_dark_mode) {
    //         console.log('system-true')
    //         this.$q.dark.set('auto')
    //         this.dark = false
    //         this.systemDark = true
    //       } else if (this.data.prefs_dark_mode) {
    //         console.log('user-true')
    //         this.$q.dark.set(true)
    //         this.dark = true
    //         this.systemDark = false
    //       } else {
    //         console.log('user-false')
    //         this.$q.dark.set(false)
    //         this.dark = false
    //         this.systemDark = false
    //       }

    //       store.commit('setUserId', this.data.id)
    //       store.commit('setUserFirstName', this.data.first_name)
    //       store.commit('setUserLastName', this.data.last_name)
    //       store.commit('setUserEmail', this.data.email)
    //       store.commit('setUserEndDay', this.data.until)
    //       store.commit('setUserOpen', this.data.open)
    //       store.commit('setUserIsadmin', this.data.isadmin)
    //       store.commit('setDarkMode', this.data.prefs_dark_mode)
    //       store.commit('setSystemDarkMode', this.data.prefs_system_dark_mode)
    //     })
    // }
  },
  mounted () {
    // this.loggedIn = store.getters.loggedIn
    // this.user = store.getters.getUserName
    // }
  }
}
</script>

<style scoped lang="sass">
.tabbar
  height: 60px

.ebbg-primary
  background: linear-gradient(to right, $primary, $secondary)
</style>
