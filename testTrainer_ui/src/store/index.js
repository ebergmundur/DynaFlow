import Vue from 'vue'
import Vuex from 'vuex'
import { axiosBase } from 'src/api/axios-base'

Vue.use(Vuex)

// const serv = 'https://einars-macbook-pro.local:8000'
const store = new Vuex.Store({
  state: {
    currentQuestion: 'CurrentQuestionInSession',
    testQuestion: [],
    accessToken: localStorage.getItem('access_token') || null, // makes sure the user is logged in even after
    // refreshing the page
    refreshToken: localStorage.getItem('refresh_token') || null,
    userId: localStorage.getItem('user_id') || null,
    userName: localStorage.getItem('username') || null,
    userFirstName: localStorage.getItem('user_first_name') || null,
    userLastName: localStorage.getItem('user_last_name') || null,
    userEmail: localStorage.getItem('user_email') || null,
    userOpen: localStorage.getItem('open') || null,
    userIsadmin: localStorage.getItem('isadmin') || null,
    userEndDay: localStorage.getItem('endday') || null,
    ueserPrefsDarkMode: localStorage.getItem('dark_mode') || null,
    userPrefsSystemDarkMode: localStorage.getItem('system_dark_mode') || null,
    timeTotal: localStorage.getItem('timetotal') || 0,
    testTimeTotal: localStorage.getItem('testtimetotal') || 0,
    timeAllowed: localStorage.getItem('timeallowed') || 0,
    testTimeAllowed: localStorage.getItem('testtimeallowed') || 0,
    currentTest: '',
    APIData: '' // received data from the backend API is stored here.
  },
  mutations: {
    setTestTimeAllowed (state, payload) {
      state.testTimeAllowed = payload
    },
    setTimeAllowed (state, payload) {
      state.timeAllowed = payload
    },
    setDarkMode (state, payload) {
      localStorage.setItem('dark_mode', payload)
      state.userPrefsDarkMode = payload
    },
    setSystemDarkMode (state, payload) {
      localStorage.setItem('system_dark_mode', payload)
      state.userPrefsSysemDarkMode = payload
    },
    setTimeTotal (state, payload) {
      localStorage.setItem('timetotal', payload)
      state.timeTotal = payload
    },
    setTestTimeTotal (state, payload) {
      console.log('testtimetotal')
      localStorage.setItem('testtimetotal', payload)
      state.testTimeTotal = payload
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
    setUserOpen (state, payload) {
      state.userOpen = payload
    },
    setUserIsadmin (state, payload) {
      state.userIsadmin = payload
    },
    setUserEndDay (state, payload) {
      state.userEndDay = payload
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
    updateLocalUserStorage (state, { firstname, lastname, email, id, open, until, isadmin, darkMode, systemDarkMode }) {
      console.log('updateLocalUserStorage')
      localStorage.setItem('user_first_name', firstname)
      localStorage.setItem('user_last_name', lastname)
      localStorage.setItem('user_email', email)
      localStorage.setItem('user_id', id)
      localStorage.setItem('open', open)
      localStorage.setItem('endday', until)
      localStorage.setItem('isadmin', isadmin)
      localStorage.setItem('dark_mode', darkMode)
      localStorage.setItem('system_dark_mode', systemDarkMode)
      state.userFirstName = firstname
      state.userLastName = lastname
      state.userEmail = email
      state.userOpen = open.open
      state.userEndDay = open.until
      state.userIsadmin = isadmin
      state.userPrefsSysemDarkMode = systemDarkMode
      state.userPrefsDarkMode = darkMode
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
    logoutUser (context, payload) {
      console.log('LOGGING OUT')
      if (context.getters.loggedIn) {
        return new Promise((resolve, reject) => {
          axiosBase.get('/api/token/logout/')
            // axiosBase.get('/api-auth/logout/')
            .then(response => {
              localStorage.removeItem('access_token')
              localStorage.removeItem('refresh_token')
              localStorage.removeItem('username')
              localStorage.removeItem('testtimetotal')
              localStorage.removeItem('testtimeallowed')
              localStorage.removeItem('timetotal')
              localStorage.removeItem('timeallowed')
              localStorage.removeItem('user_first_name')
              localStorage.removeItem('user_last_name')
              localStorage.removeItem('user_email')
              localStorage.removeItem('open')
              localStorage.removeItem('isadmin')
              localStorage.removeItem('user_id')
              localStorage.removeItem('open')
              localStorage.removeItem('endday')
              localStorage.removeItem('dark_mode')
              localStorage.removeItem('system_dark_mode')
              context.commit('destroyToken')
              console.log('LOGGED OUT A')
            })
            .catch(err => {
              localStorage.removeItem('access_token')
              localStorage.removeItem('refresh_token')
              localStorage.removeItem('username')
              localStorage.removeItem('testtimetotal')
              localStorage.removeItem('testtimeallowed')
              localStorage.removeItem('timetotal')
              localStorage.removeItem('timeallowed')
              localStorage.removeItem('user_first_name')
              localStorage.removeItem('user_last_name')
              localStorage.removeItem('user_email')
              localStorage.removeItem('open')
              localStorage.removeItem('isadmin')
              localStorage.removeItem('user_id')
              localStorage.removeItem('open')
              localStorage.removeItem('endday')
              localStorage.removeItem('dark_mode')
              localStorage.removeItem('system_dark_mode')
              context.commit('destroyToken')
              resolve(err)
              console.log('LOGGED OUT B')
            })
        })
      } else {
        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
        localStorage.removeItem('username')
        localStorage.removeItem('testtimetotal')
        localStorage.removeItem('testtimeallowed')
        localStorage.removeItem('timetotal')
        localStorage.removeItem('timeallowed')
        localStorage.removeItem('user_first_name')
        localStorage.removeItem('user_last_name')
        localStorage.removeItem('user_email')
        localStorage.removeItem('open')
        localStorage.removeItem('isadmin')
        localStorage.removeItem('user_id')
        localStorage.removeItem('open')
        localStorage.removeItem('endday')
        localStorage.removeItem('dark_mode')
        localStorage.removeItem('system_dark_mode')
        context.commit('destroyToken')
        console.log('LOGGED OUT D')
      }
    },
    setTotalTime (context, time) {
      context.commit('setTimeTotal', time)
    },
    setTestTimeTotal (context, time) {
      context.commit('setTestTimeTotal', time)
    },
    setTestTimeAllowed (context, time) {
      context.commit('setTestTimeAllowed', time)
    },
    loginUser (context, credentials) {
      console.log('LOGGING IN')
      return new Promise((resolve, reject) => {
        // send the username and password to the backend API:
        axiosBase.post('/api/token/', {
          // axiosBase.post('/api-auth/login/', {
          username: credentials.username,
          password: credentials.password
        })
          // if successful update local storage:
          .then(response => {
            // console.log(response)
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
    getTimeAllowed (state) {
      return state.timeAllowed
    },
    getTestTimeAllowed (state) {
      return state.testTimeAllowed
    },
    getTestTimeTotal (state) {
      return state.testTimeTotal
    },
    getTimeTotal (state) {
      return state.timeTotal
    },
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
    getDarkMode (state) {
      if (state.ueserPrefsDarkMode === 'false') {
        return false
      } else {
        return true
      }
    },
    getSystemDarkMode (state) {
      if (state.userPrefsSystemDarkMode === 'false') {
        return false
      } else {
        return true
      }
      // return state.userPrefsSystemDarkMode
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
        email: state.userEmail,
        isadmin: state.userIsadmin,
        open: state.userOpen,
        until: state.userEndDay,
        darkMode: state.userPrefsDarkMode,
        systemDarkMode: state.userPrefsSystemDarkMode
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
