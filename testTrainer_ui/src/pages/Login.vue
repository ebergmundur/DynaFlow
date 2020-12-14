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
          <h2 v-if="wrongCred">Wrong credentials entered!. Please enter your correct details.</h2>
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
export default {
  name: 'login',
  components: {
    // NavBar
  },
  data () {
    return {
      username: '',
      password: '',
      isPwd: true,
      wrongCred: false // activates appropriate message if set to true
    }
  },
  methods: {
    loginUser () { // call loginUSer action
      this.$store.dispatch('loginUser', {
        username: this.username,
        password: this.password
      })
        .then(() => {
          this.wrongCred = false
          this.$router.push({ name: 'userinfo' })
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
