import Vue from 'vue'
import Vuex from 'vuex'
import { axiosBase } from 'src/api/axios-base'
// import axios from 'axios'

Vue.use(Vuex)
// const serv = 'https://einars-macbook-pro.local:8000'
const store = new Vuex.Store({
  state: {
    currentQuestion: 'CurrentQuestionInSession',
    testQuestion: [],
    timeAllowed: 150000,
    accessToken: localStorage.getItem('access_token') || null, // makes sure the user is logged in even after
    // refreshing the page
    refreshToken: localStorage.getItem('refresh_token') || null,
    userId: '',
    userName: '',
    userFullName: '',
    currentTest: '',
    APIData: '' // received data from the backend API is stored here.
  },
  mutations: {
    setTimeAllowed (state, payload) {
      state.timeAllowed = payload
    },
    setUserName (state, payload) {
      console.log(payload)
      state.userName = payload
    },
    setQuestion (state, payload) {
      state.currentQuestion = payload
    },
    setTestQuestion (state, payload) {
      state.testQuestion = payload
    },
    setOptinsChecked (state, payload) {
      state.currentQuestion.checked = payload
    },
    updateLocalStorage (state, { access, refresh }) {
      localStorage.setItem('access_token', access)
      localStorage.setItem('refresh_token', refresh)
      state.accessToken = access
      state.refreshToken = refresh
    },
    updateAccess (state, access) {
      state.accessToken = access
    },
    destroyToken (state) {
      state.accessToken = null
      state.refreshToken = null
      state.userName = ''
    }
  },
  actions: {
    setSelectedAnswer (state, payload) {
      console.log(payload)
    },
    refreshToken (context) {
      return new Promise((resolve, reject) => {
        axiosBase.post('/api/token/refresh/', {
          refresh: context.state.refreshToken
        }) // send the stored refresh token to the backend API
          .then(response => { // if API sends back new access and refresh token update the store
            console.log('New access successfully generated')
            context.commit('updateAccess', response.data.access)
            resolve(response.data.access)
          })
          .catch(err => {
            console.log('error in refreshToken Task')
            reject(err) // error generating new access and refresh token because refresh token has expired
          })
      })
    },
    registerUser (context, data) {
      return new Promise((resolve, reject) => {
        axiosBase.post('/register', {
          name: data.name,
          email: data.email,
          username: data.username,
          password: data.password,
          confirm: data.confirm
        })
          .then(response => {
            resolve(response)
          })
          .catch(error => {
            reject(error)
          })
      })
    },
    logoutUser (context) {
      if (context.getters.loggedIn) {
        return new Promise((resolve, reject) => {
          axiosBase.post('/api/token/logout/')
            .then(response => {
              localStorage.removeItem('access_token')
              localStorage.removeItem('refresh_token')
              context.commit('destroyToken')
            })
            .catch(err => {
              localStorage.removeItem('access_token')
              localStorage.removeItem('refresh_token')
              context.commit('destroyToken')
              resolve(err)
            })
        })
      }
    },
    loginUser (context, credentials) {
      console.log(context, credentials)
      // context.commit('setUserName', credentials.username)

      return new Promise((resolve, reject) => {
        // send the username and password to the backend API:
        axiosBase.post('/api/token/', {
          username: credentials.username,
          password: credentials.password
        })
          // if successful update local storage:
          .then(response => {
            context.commit('updateLocalStorage', { access: response.data.access, refresh: response.data.refresh }) // store the access and refresh token in localstorage
            context.commit('setUserName', credentials.username)
            resolve()
          })
          .catch(err => {
            reject(err)
          })
      })
    },
    userInfo (username) {
      const access = this.state.accessToken
      var formdata = {
        username: username
      }

      axiosBase.get({
        data: formdata,
        headers: { Authorization: `Bearer ${access}` }, // the new access token is attached to the authorization header
        url: '/api/userdata/'
      })
        .then(response => {
          this.state.userId = ''
          this.state.userName = ''
          this.state.userFullName = ''
        })
        .catch(error => console.log('Error', error.message))
    }
  },
  getters: {
    token (state) {
      return state.accessToken
    },
    loggedIn (state) {
      return state.accessToken != null
    },
    currQest: state => {
      return state.currentQuestion
    },
    currTestQest: state => {
      return state.testQuestion
    },
    getUserName (state) {
      return state.userName
    },
    currTimeAllowed: state => {
      if (state.timeAllowed > 0) {
        return state.timeAllowed
      } else {
        return 150000
      }
    }
    // ,
    // setSelected: state => {
    //   return actions.setSelectedAnswer()
    // }
  }
})

export default store
