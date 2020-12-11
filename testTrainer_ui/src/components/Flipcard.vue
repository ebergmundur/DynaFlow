<template>
  <div class="q-pa-md row items-start q-gutter-md justify-center scroll">

    <q-slide-item
      @left="onLeft"
      @right="onRight"
      @top="onTop"
      @bottom="onBottom"
      left-color="transparent"
      right-color="transparent"
      top-color="transparent"
      bottom-color="transparent"
      class="flip-card"
    >
      <!--      @click="flippit"-->

      <template v-slot:top>
        <q-icon name="link"/>
      </template>
      <template v-slot:right>
        <q-icon name="forward"/>
      </template>
      <template v-slot:bottom>
        <q-icon name="link_off"/>
      </template>
      <template v-slot:left>
        <q-icon name="back"/>
      </template>

      <q-item class="q-pa-none flip-card" style="width: 300px; height: 500px;">
        <div class="flip-card-inner">

          <div class="col q-pa-none flip-card-front">
            <q-toolbar class="q-dark q-ma-none" style="background-color: #616161;">
              <q-toolbar-title>
                Flettikort
              </q-toolbar-title>
            </q-toolbar>
            <div class="row items-center no-wrap">

              <div class="col-12 q-pa-md scroll">
                <div class="">{{ currentQuestion.question }}</div>
                {{ currentQuestion.description }}
              </div>

            </div>
          </div>

          <div class="flip-card-back">
            <q-toolbar class="q-dark q-ma-none" style="background-color: #616161;">
              <q-toolbar-title>
                Flettikort
              </q-toolbar-title>
            </q-toolbar>
            <div class="col-12 q-pa-md ">
              <div class="">{{ currentQuestion.question }}</div>
            </div>
            <div class="col-12 text-left">
              <div
                v-for="opt in currentOptions"
                :key="opt.id"
                class="quest-options"
              >
                <q-radio
                  v-if="currentQuestion.single_selection"
                  :name="opt.question_ref.toString()"
                  :label="opt.answer"
                  value="false"
                  :val="opt.id"
                  v-model="currTestAnsw"
                  @input="setAnswerChecked"
                />
                <q-checkbox
                  v-if="!currentQuestion.single_selection"
                  :name="opt.question_ref.toString()"
                  :label="opt.answer"
                  value="false"
                  :val="opt.id"
                  v-model="currTestAnsw"
                  @input="setAnswerChecked"
                />
                {{ opt.correct }}
              </div>
            </div>
          </div>
        </div>

      </q-item>
    </q-slide-item>
    <q-separator></q-separator>

    <div class="col-2 col-lg-offset-5 align-center text-center redborder">
      <div class="row col">
        <div class="col-12">Merkja „kann vel“</div>
      </div>
      <div class="row col-12">
        <div class="col-3 redborder" style="float: left;">Fyrri</div>
        <div class="col-6 redborder" style="float: left;"></div>
        <div class="col-3 redborder" style="float: right;">Svar</div>
      </div>
      <div class="row col">
        <div class="col-12">Næsta spurning</div>
      </div>
    </div>
  </div>
</template>

<script>
import store from 'src/store'
import { date } from 'quasar'
import { axiosBase } from 'src/api/axios-base'

const access = store.getters.token // attempt to obtain new access token by running 'refreshToken' action
//       axios.request({
//   method: 'get',
//   headers: { Authorization: `Bearer ${access}` }, // the new access token is attached to the authorization header
//   url: 'https://127.0.0.1:8000/api/dashboard/'
// })

const SCHEMA = {
  type: 'object',
  properties: {
    question: '',
    memotext: '',
    difficulty: 50,
    date: '',
    user: 1
  }
}

export default {
  name: 'Question',
  computed: {
    currentQuestion () {
      return store.getters.currQest.payload
    },
    formDate () {
      return date.formatDate(this.date, 'YYYY-MM-DD')
    },
    currentOptions () {
      return store.getters.currQest.payload.options
    }
  },
  methods: {
    setQuestion (e) {
      var index = 0
      if (e > -1) {
        index = e - 1
      } else {
        index = 0
      }
      this.hinttext = ''
      this.editingIndex = index
      this.question = JSON.parse(JSON.stringify(this.myJson[index]))
      store.commit({ type: 'setQuestion', payload: this.question })
      // index.commit({ type: 'setTestQuestion', payload: [] })
      // Question.setAnswerChecked()
      this.currPoints = this.question.points
      this.questNum = index + 1
    },
    setAnswerChecked (e) {
      var i = 0
      for (i = 0; i < this.currentOptions.length; i++) {
        console.log(this.currentOptions[i].id)
        if (this.currentOptions[i].id === e) {
          if (this.currentOptions[i].correct === true) {
            alert('Húrra')
          } else {
            alert('Hálfviti')
          }
        }
      }
    },
    onMemoSubmit (e) {
      const formdata = {
        difficulty: this.difficulty,
        memo: this.memotext,
        known: this.known,
        curr_question: this.currentQuestion.id
      }
      axiosBase.post({
        headers: { Authorization: `Bearer ${access}` },
        url: '/api/memos/',
        data: formdata
      })
    },
    onAnswerSubmit (e) {
      const formdata = {
        time_allowed: this.time_allowed,
        time_taken: parseInt(this.time_taken),
        options_ids: this.currTestQuest.toString(),
        curr_question: this.currentQuestion.id
      }
      axiosBase.post({
        headers: { Authorization: `Bearer ${access}` },
        url: '/api/answer/',
        data: formdata
      })
    },
    onMemoReset () {
      this.memotext = ''
      this.difficulty = 50
      this.accept = false
      this.calendar = false
      this.showDate = false
    },
    hint () {
      this.hinttext = this.currentQuestion.hint
      this.hintloss = this.currentQuestion.points - this.currentQuestion.hint_cost
    },
    openMemos () {
      this.memolist = true
    },
    showCal () {
      this.calendar = true
      this.showDate = !this.showDate
    },
    formatDate (d) {
      return date.formatDate(d, 'YYYY-MM-DD')
    },
    formatOptions () {
      if (this.currentQuestion.single_selection) {
        return 'radio'
      } else {
        return 'checkbox'
      }
    },
    finalize (reset) {
      this.time = setTimeout(() => {
        reset()
      }, 1000)
    },
    onLeft ({ reset }) {
      this.$q.notify('Left action triggered. Resetting in 1 second.')
      this.finalize(reset)
    },
    onRight ({ reset }) {
      document.getElementsByClassName('flip-card-inner').className += ' flipp'
      this.$q.notify('Right action triggered. Resetting in 1 second.')
      // console.log(flippers)
      // flippers.childNodes[0]
      // document.getElementsByClassName('flip-card-inner').childNodes[1].className += ' flipp'
      this.finalize(reset)
    },
    onBottom ({ reset }) {
      this.$q.notify('Bottom action triggered. Resetting in 1 second.')
      this.finalize(reset)
    },
    onTop ({ reset }) {
      this.$q.notify('Top action triggered. Resetting in 1 second.')
      this.finalize(reset)
    },
    // rottto (i) {
    //   i.setAttribute('style', 'transform: rotateY(180deg)')
    // },
    flippit () {
      axiosBase.get({
        headers: { Authorization: `Bearer ${access}` },
        url: '/api/flipcard/?format=json'
      })
        .then(response => {
          this.myJson = JSON.parse(JSON.stringify(response.data))
          // console.log(this.myJson)
          this.setQuestion(1)
        })
        .catch(error => console.log('Error', error.message))
    }
  },
  mounted () {
    this.flippit()
  },
  beforeDestroy () {
    clearTimeout(this.timer)
  },
  data () {
    return {
      // currentOptions: this.currentQuestion.options,
      hinttext: '',
      cQ: 0,
      hintloss: '',
      currTestQuest: [],
      memo: SCHEMA,
      memolist: false,
      calendar: false,
      visible: false,
      currTestAnsw: [],
      memotext: '',
      difficulty: 50,
      accept: false,
      date: '2020/24/12',
      known: false,
      interval: 0,
      progress: 0.01,
      time_allowed: 0,
      time_taken: 0,
      time_step: 0,
      time: null,
      tesing_user: 1
    }
  }
}

// TODO Hreinsa currTestQuest á milli spurninga
</script>

<style scoped lang="css">
.quest-options {
  border: 1px solid #8d8c8c;
  padding: 5px;
  margin: 5px 0;
  background-color: #eaeaea;
}

/* The flip card container - set the width and height to whatever you want. We have added the border property to demonstrate that the flip itself goes out of the box on hover (remove perspective if you don't want the 3D effect */
.flip-card {
  background-color: transparent;
  /*width: 300px;*/
  /*height: 200px;*/
  border: 1px solid #f1f1f1;
  perspective: 1000px; /* Remove this if you don't want the 3D effect */
}

/* This container is needed to position the front and back side */
.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  text-align: center;
  transition: transform 0.8s;
  transform-style: preserve-3d;
}

/*Do an horizontal flip when you move the mouse over the flip box container*/
.flip-card:hover .flip-card-inner {
  transform: rotateY(180deg);
}

/*Do an horizontal flip when you move the mouse over the flip box container */
.flipp {
  transform: rotateY(180deg);
}

/* Position the front and back side */
.flip-card-front, .flip-card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  -webkit-backface-visibility: hidden; /* Safari */
  backface-visibility: hidden;
}

/* Style the front side (fallback if image is missing) */
.flip-card-front {
  /*background-color: #bbb;*/
  background-color: #FFFFFF;
  /*color: black;*/
}

/* Style the back side */
.flip-card-back {
  /*background-color: dodgerblue;*/
  background-color: #FFFFFF;
  /*color: white;*/
  transform: rotateY(180deg);
}

</style>
