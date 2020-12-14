<template>
  <q-page class="flex flex-center q-pa-xs ">
    <div class="q-pa-md row items-start q-gutter-md">
      <q-card
        class="my-card bg-grey-1 absolute-center col-xs-12 col-xs-12 col-md-6 col-xl-4 col-lg-4"
      >
        <q-toolbar class="q-dark" style="background-color: #616161;">
          <q-toolbar-title>
            Nýr notandi
          </q-toolbar-title>
        </q-toolbar>
        <q-card-section>
          <div class="row items-center wrap q-gutter-md">

            <div class="row col-12">

              <div class="form-group col-11" :class="{ 'form-group--error': $v.name.$error }">
                <q-input type="text" class="" label="Nafn" v-model.trim="$v.name.$model">
                  <template v-slot:before>
                    <q-icon class="fa fa-user-alt"/>
                  </template>
                </q-input>
              </div>
              <div class="error col-11" v-if="!$v.name.required">Verður að fylla út</div>
              <div class="error col-11" v-if="!$v.name.minLength">Nafn verður að vera minnst {{ $v.name.$params.minLength.min }}
                stafir.
              </div>
              <div class="form-group  col-11" :class="{ 'form-group--error': $v.username.$error }">
                <q-input type="text" class="col-11" label="Notendanafn" v-model.trim="$v.username.$model">
                  <template v-slot:before>
                    <q-icon class="fa  fa-id-card"/>
                  </template>
                </q-input>
              </div>
              <div class="error col-11" v-if="!$v.username.required">Verður að fylla út</div>
              <div class="error col-11" v-if="!$v.username.minLength">Name must have at least
                {{ $v.username.$params.minLength.min }}
                letters.
              </div>
              <div class="form-group  col-11" :class="{ 'form-group--error': $v.email.$error }">
                <q-input type="email" class="col-11" label="Netfang" v-model.trim="$v.email.$model">
                  <template v-slot:before>
                    <q-icon class="fa fa-at"/>
                  </template>
                </q-input>
              </div>
              <div class="error col-11" v-if="!$v.email.required">Verður að fylla út</div>
              <div class="error col-11" v-if="!$v.email.email">Verður að vera netfang</div>
              <div class="form-group  col-11" :class="{ 'form-group--error': $v.password.$error }">
                <q-input type="password" class="col-11" label="Lykilorð" v-model.trim="$v.password.$model">
                  <template v-slot:before>
                    <q-icon class="fa fa-key"/>
                  </template>
                </q-input>
              </div>
              <div class="error col-11" v-if="!$v.password.required">Verður að fylla út</div>
              <div class="error col-11" v-if="!$v.password.minLength">Name must have at least
                {{ $v.password.$params.minLength.min }}
                letters.
              </div>
              <div class="form-group  col-11" :class="{ 'form-group--error': $v.passworconfirmed.$error }">
                <q-input type="password" class="col-11" label="Staðfesta lykilorð"
                         v-model.trim="$v.passworconfirmed.$model">
                  <template v-slot:before>
                    <q-icon class="fa fa-check-circle" color=""/>
                  </template>
                </q-input>
              </div>
              <div class="error col-11" v-if="!$v.passworconfirmed.required">Verður að fylla út</div>
              <div class="error col-11" v-if="!$v.passworconfirmed.sameAsPassword">Stenst ekki prófun við efra lykilorð
              </div>
            </div>

            <!--          </form>-->
          </div>
        </q-card-section>
        <q-card-actions>
          <div class="q-gutter-md col">
            <!--          <button type="submit">Skrá inn</button>-->

            <q-btn
              color="positive"
              label="Staðfesta"
              style="float: right;"
              class="q-mr-none q-mb-md"
              @click="registerUser"

            />
          </div>
        </q-card-actions>
      </q-card>
    </div>

    <!--  <div class="register-form">-->
    <!--&lt;!&ndash;    <NavBar></NavBar>&ndash;&gt;-->
    <!--    <form @submit.prevent="registerUser">-->
    <!--      <label for="Name">Name</label>-->
    <!--      <input type="text" name="Name" id="Name" v-model="name">-->
    <!--      <label for="el">Email</label>-->
    <!--      <input type="email" name="el" id="el" v-model="email">-->
    <!--      <label for="ur">Username</label>-->
    <!--      <input type="text" name="ur" id="ur" v-model="username">-->
    <!--      <label for="pwr">Password</label>-->
    <!--      <input type="password" name="pwr" id="pwr" v-model="password">-->
    <!--      <label for="pass">Password Confirmation</label>-->
    <!--      <input type="password" name="pass" id="pass" v-model="confirm">-->
    <!--      <button type="submit">Register</button>-->
    <!--    </form>-->
    <!--  </div>-->
  </q-page>
</template>

<script>
// import NavBar from '../components/Navbar'

import Vue from 'vue'
import Vuelidate from 'vuelidate'
Vue.use(Vuelidate)

import { required, minLength, sameAs, email } from 'vuelidate/lib/validators'

export default {
  name: 'register',
  components: {},
  data () {
    return {
      name: '',
      email: '',
      username: '',
      password: '',
      passworconfirmed: ''
    }
  },
  validations: {
    name: {
      required,
      minLength: minLength(10)
    },
    username: {
      required,
      minLength: minLength(5)
    },
    email: {
      required,
      email
    },
    password: {
      required,
      minLength: minLength(6)
    },
    passworconfirmed: {
      required,
      sameAsPassword: sameAs('password')
    }
  },
  methods: {
    setName (value) {
      this.name = value
      this.$v.name.$touch()
    },
    registerUser () {
      this.$store.dispatch('registerUser', {
        name: this.name,
        email: this.email,
        username: this.username,
        password: this.password,
        confirm: this.passworconfirmed
      }).then(() => {
        this.$router.push({ name: 'login' })
      })
    }
  }
}
</script>

<style scoped>
@import url(https://fonts.googleapis.com/css?family=Quicksand);

.error {
  font-size: small;
  color: crimson;
  text-align: right;
}

.register-form {
  /*background-color: #606366;*/
  width: 100%;
  margin: 78px auto;
  padding: 0;
  text-align: center;
}

/*h5%449aZ32*/
</style>
