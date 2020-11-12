import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    currentQuestion: 'CurrentQuestionInSession',
    testQuestion: []
  },
  mutations: {
    setQuestion (state, payload) {
      state.currentQuestion = payload
    },
    setTestQuestion (state, payload) {
      state.testQuestion = payload
    },
    setOptinsChecked (state, payload) {
      state.currentQuestion.checked = payload
    }
  },
  actions: {
    setSelectedAnswer (state, payload) {
      console.log(payload)
    }
  },
  getters: {
    currQest: state => {
      return state.currentQuestion
    },
    currTestQest: state => {
      return state.testQuestion
    }
    // ,
    // setSelected: state => {
    //   return actions.setSelectedAnswer()
    // }
  }
})

export default store
