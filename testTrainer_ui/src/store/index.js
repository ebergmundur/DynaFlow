import Vue from 'vue'
import Vuex from 'vuex'
import { axiosBase } from 'src/api/axios-base'
// import axios from 'axios'
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
    userId: localStorage.getItem('user_id') || null,
    userName: localStorage.getItem('username') || null,
    userFirstName: localStorage.getItem('user_first_name') || null,
    userLastName: localStorage.getItem('user_last_name') || null,
    userEmail: localStorage.getItem('user_email') || null,
    currentTest: '',
    APIData: '' // received data from the backend API is stored here.
  },
  mutations: {
    setTimeAllowed (state, payload) {
      state.timeAllowed = payload
    },
    setUserId (state, payload) {
      localStorage.setItem('user_id', payload)
      state.userId = payload
    },
    setUserFirstName (state, payload) {
      localStorage.setItem('user_first_name', payload)
      state.userFirstName = payload
    },
    setUserLastName (state, payload) {
      localStorage.setItem('user_last_name', payload)
      state.userLastName = payload
    },
    setUserEmail (state, payload) {
      localStorage.setItem('user_email', payload)
      state.userEmail = payload
    },
    setUserName (state, payload) {
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
    updateLocalStorage (state, { access, refresh, username }) {
      localStorage.setItem('access_token', access)
      localStorage.setItem('refresh_token', refresh)
      localStorage.setItem('username', username)
      state.accessToken = access
      state.refreshToken = refresh
      state.userName = username
    },
    updateLocalUserStorage (state, { firstname, lastname, email, id }) {
      localStorage.setItem('user_first_name', firstname)
      localStorage.setItem('user_last_name', lastname)
      localStorage.setItem('user_email', email)
      localStorage.setItem('user_id', id)
      state.userFirstName = firstname
      state.userLastName = lastname
      state.userEmail = email
      state.userId = id
    },
    updateAccess (state, access) {
      state.accessToken = access
    },
    destroyToken (state) {
      state.accessToken = null
      state.refreshToken = null
      state.userName = null
    }
  },
  actions: {
    setSelectedAnswer (state, payload) {
      // console.log(payload)
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
        axiosBase.post('/api/registeruser/', {
          first_name: data.name,
          email: data.email,
          username: data.username,
          password: data.password
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
          axiosBase.get('/api/token/logout/')
            .then(response => {
              localStorage.removeItem('access_token')
              localStorage.removeItem('refresh_token')
              localStorage.removeItem('username')
              localStorage.removeItem('user_first_name')
              localStorage.removeItem('user_last_name')
              localStorage.removeItem('user_email')
              localStorage.removeItem('user_id')
              context.commit('destroyToken')
            })
            .catch(err => {
              localStorage.removeItem('access_token')
              localStorage.removeItem('refresh_token')
              localStorage.removeItem('username')
              localStorage.removeItem('user_first_name')
              localStorage.removeItem('user_last_name')
              localStorage.removeItem('user_email')
              localStorage.removeItem('user_id')
              context.commit('destroyToken')
              resolve(err)
            })
        })
      }
    },
    loginUser (context, credentials) {
      return new Promise((resolve, reject) => {
        // send the username and password to the backend API:
        axiosBase.post('/api/token/', {
          username: credentials.username,
          password: credentials.password
        })
          // if successful update local storage:
          .then(response => {
            context.commit('updateLocalStorage', {
              access: response.data.access,
              refresh: response.data.refresh,
              username: credentials.username
            }) // store the access and refresh token in localstorage

            resolve()
          })
          .catch(err => {
            reject(err)
          })
      })
    },
    userInfo (context) {
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
    currTestQest:
  state => {
    return state.testQuestion
  },
    getUserName (state) {
      return state.userName
    },
    getUserFirstName (state) {
      return state.userFirstName
    },
    getUserLastName (state) {
      return state.userLastName
    },
    getUserEmail (state) {
      return state.userEmail
    },
    getUserInfo (state) {
      return {
        firstName: state.userFirstName,
        lastName: state.userLastName,
        userid: state.userId,
        username: state.userName,
        email: state.userEmail
      }
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
