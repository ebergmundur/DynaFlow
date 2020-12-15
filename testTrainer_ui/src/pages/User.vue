<template>
    <q-page class="flex flex-center q-pa-xs ">
  <div class="q-pa-md row items-start q-gutter-md">

    <q-card
      class="my-card bg-grey-1 absolute-center col-xs-12 col-xs-12 col-md-6 col-xl-4 col-lg-4"
    >
      <q-toolbar class="q-dark" style="background-color: #616161;">
        <q-toolbar-title>
          {{ userInfo.firstName }} {{ userInfo.lastName }}
        </q-toolbar-title>

      </q-toolbar>
      <q-card-section>
        <div class="row items-center wrap q-gutter-md">
          <!--    <q-list bordered class="rounded-borders" style="max-width: 1600px">-->
          <q-list bordered class="rounded-borders col">
            <!--      <q-item-label header class="q-dark">Yfirlit um stöðu</q-item-label>-->

            <q-item>
              <q-item-section top class="col-2 gt-sm">
              <q-item-section avatar top>
                <q-icon class="" name="person" color="black" size="38px"/>
              </q-item-section>

                <q-item-label class="q-mt-sm">{{ user }}</q-item-label>
              </q-item-section>

              <q-item-section top>
                <q-item-label lines="1">
                  <span class="text-grey-8">Áskrift til {{ format_date(userInfo.until) }}
                  {{userInfo.open}}
                  </span>

                </q-item-label>
                <q-item-label caption lines="1">
                  Sjálfvirk endurnýjun í gangi
                </q-item-label>
<!--                <q-item-label lines="1" class="q-mt-xs text-body2 text-weight-bold text-primary text-uppercase">-->
<!--                              <span class="cursor-pointer">Open in GitHub</span>-->
<!--                </q-item-label>-->
              </q-item-section>

              <q-item-section top side>
                <div class="text-grey-8 q-gutter-xs">
                <q-btn class="bg-positive text-white" size="12px"  icon="payment" label="Breyta"/>
                  </div>
<!--                <div class="text-grey-8 q-gutter-xs">-->
<!--                  &lt;!&ndash;            <q-btn class="gt-xs" size="12px" flat dense round icon="delete" />&ndash;&gt;-->
<!--                  <q-btn class="gt-xs" size="12px" flat dense round icon="done"/>-->
<!--                  <q-btn size="12px" flat dense round icon="more_vert"/>-->
<!--                </div>-->
              </q-item-section>
            </q-item>

            <q-separator spaced/>

<!--            <q-item>-->
<!--              <q-item-section avatar top>-->
<!--                <q-icon name="account_tree" color="black" size="34px"/>-->
<!--              </q-item-section>-->

<!--              <q-item-section top class="col-2 gt-sm">-->
<!--                <q-item-label class="q-mt-sm">Árangur</q-item-label>-->
<!--              </q-item-section>-->

<!--              <q-item-section top>-->
<!--                <q-item-label lines="1">-->
<!--                  <span class="text-weight-medium">16% allra spurninga á 17 dögum</span>-->
<!--                  <span class="text-grey-8"> 634 ósvarað</span>-->
<!--                </q-item-label>-->
<!--                <q-item-label caption lines="1">-->
<!--                  Vel yfir meðaltali notenda-->
<!--                </q-item-label>-->
<!--                <q-item-label lines="1" class="q-mt-xs text-body2 text-weight-bold text-primary text-uppercase">-->
<!--                  &lt;!&ndash;            <span class="cursor-pointer">Open in GitHub</span>&ndash;&gt;-->
<!--                </q-item-label>-->
<!--              </q-item-section>-->

<!--              <q-item-section top side>-->
<!--                <div class="text-grey-8 q-gutter-xs">-->
<!--                  &lt;!&ndash;            <q-btn class="gt-xs" size="12px" flat dense round icon="delete" />&ndash;&gt;-->
<!--                  <q-btn class="gt-xs" size="12px" flat dense round icon="done"/>-->
<!--                  <q-btn size="12px" flat dense round icon="more_vert"/>-->
<!--                </div>-->
<!--              </q-item-section>-->
<!--            </q-item>-->
          </q-list>
        </div>
      </q-card-section>

    </q-card>
  </div>
    </q-page>

</template>

<script>
import store from 'src/store'
import { date } from 'quasar'
// import axios from 'axios'
// import { getAPI } from 'src/api/axios-base'

// const timeStamp = Date.now()

export default {
  name: 'User',
  // components: {
  //
  // },
  data () {
    return {
      // loggedIn: false,
      token: null,
      userId: 0,
      firstName: '',
      lastName: '',
      email: ''
    }
  },
  methods: {
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
