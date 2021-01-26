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
              Dark mode
            </q-toolbar-title>
          </q-toolbar>
            <div>
              <!-- Setja inn preferenca í User Model í bakenda -->
              <q-toggle v-model="autodark" @input="setdarkauto" toggle-color="primary" label="Fylgja tölvu" />
              <q-toggle v-model="isdark" ref="mandark" @input="setdark" toggle-color="primary" label="Handvirkt" />
            </div>
            <!-- <q-separator spaced/> -->
          </q-card-section>
      </q-card>
    </div>
  </q-page>
</template>

<script>
import store from 'src/store'
import { date } from 'quasar'
import Heatmap from 'components/Heatmap'
// import axios from 'axios'
// import { getAPI } from 'src/api/axios-base'

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
      isdark: false,
      autodark: true
    }
  },
  methods: {
    setdark () {
      this.$q.dark.toggle()
    },
    setdarkauto () {
      this.$q.dark.set('auto')
      this.isdark = false
      // this.$ref.set(false)
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
    }
  },
  mounted () {
  //   this.token = store.getters.token
  //   var formdata = {
  //     username: 'eberg'
  //   }
  //   // console.log('response')
  //   axios({
  //     method: 'post',
  //     data: formdata,
  //     headers: { Authorization: `Bearer ${access}` }, // the new access token is attached to the authorization header
  //     url: 'https://einars-macbook-pro.local:8000/userdata/'
  //   })
  //     .then(response => {
  //       // console.log('response 2')
  //       console.log(response)
  //       this.user = response.data.username
  //       this.userId = response.data.id
  //       this.firstName = response.data.first_name
  //       this.lastName = response.data.last_name
  //       this.email = response.data.email
  //       // console.log('response OUT')
  //       localStorage.setItem('userFirstName')
  //       localStorage.setItem('userLastName')
  //       localStorage.setItem('userEmail')
  //     })
  //     .catch(error => console.log('Error', error.message))
  }
}

</script>

<style scoped>

</style>
