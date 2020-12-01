<template>
  <div id="q-app">
    <router-view />
  </div>
</template>

<script>
import AuthService from './auth/AuthService'
import axios from 'axios'

const API_URL = 'http://api.enam.is'
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
      const url = `${API_URL}/api/private/`
      return axios.get(url, { headers: { Authorization: `Bearer ${auth.getAuthToken()}` } }).then((response) => {
        console.log(response.data)
        this.message = response.data || ''
      })
    }
  }
}

</script>
