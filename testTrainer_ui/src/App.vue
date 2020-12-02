<template>
  <div id="q-app">
    <router-view />
      <div style="margin-right: 200px; margin-top: 20px;">

                    <h5>//{{authenticated}}//</h5>
      <button
        class="btn btn-primary btn-margin"
        v-if="!authenticated"
        @click="login()">
        Log In
      </button>

      <button
        class="btn btn-primary btn-margin"
      v-if="authenticated"
        @click="privateMessage()">
        Call Private
      </button>

      <button
        class="btn btn-primary btn-margin"
        v-if="authenticated"
        @click="logout()">
        Log Out
      </button>
      {{ message }}
      <br>
        </div>
  </div>
</template>

<script>
import AuthService from './auth/AuthService'
import axios from 'axios'

const API_URL = 'https://api.enam.is'
const auth = new AuthService()

export default {
  name: 'App',
  data () {
    this.handleAuthentication()
    this.authenticated = false

    auth.authNotifier.on('authChange', authState => {
      this.authenticated = authState.authenticated
    })

    return {
      authenticated: false,
      message: ''
    }
  },
  methods: {
    // this method calls the AuthService login() method
    login () {
      auth.login()
    },
    handleAuthentication () {
      auth.handleAuthentication()
    },
    logout () {
      auth.logout()
    },
    privateMessage () {
      const url = `${API_URL}/api/questionn/68/?format=json`
      return axios.get(url, { headers: { Authorization: `Bearer ${auth.getAuthToken()}` } }).then((response) => {
        console.log(response.data)
        this.message = response.data || ''
      })
    }
  }
}

</script>
