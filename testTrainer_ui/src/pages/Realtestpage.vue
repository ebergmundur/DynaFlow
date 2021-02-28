<template>
  <q-page class="flex flex-center">

    <div v-if="spinnegal">
      <q-spinner-bars
        color="primary"
        size="8em"
      />
      <q-tooltip :offset="[0, 8]">QSpinnerBars</q-tooltip>
    </div>

    <q-dialog v-model="testFinished">
      <q-card>
        <q-toolbar>
          <q-avatar>
            <img src="../assets/enam-logo.svg">
          </q-avatar>
          <q-toolbar-title><span class="text-weight-bold">E-nám</span> Ljúka prófi?</q-toolbar-title>
          <q-btn
            flat
            round
            dense
            icon="close"
            v-close-popup
          />
        </q-toolbar>
        <q-card-section class="scroll">
          Viltu fara í gegnum svörin núna?
          <q-btn @click="reviewTest">
            Já endilega hreint.
          </q-btn>

        </q-card-section>
      </q-card>
    </q-dialog>

    <!--    <div class="row col redborder">-->
    <q-card
      flat
      class="pagecard"
      v-model='currentQuestion'
      v-if="currentQuestion"
    >
      <q-toolbar class="q-dark">
        <q-toolbar-title>
          Próf |{{ totaltime }} | {{currentQuestion.category.name }}
          <div style="float: right;"> spurning {{ questNum }} af
            {{ totalQuestions }} | {{ questTime }}
          </div>
        </q-toolbar-title>
        <div class="col-auto">

          <!--          <q-toggle v-model="postpone" value="false" label="Sleppa " class=" q-ma-sm"/>-->

        </div>
      </q-toolbar>
      <q-card-section class="row col">
        <div class="col-md-6 q-pr-lg ">
          <div class="text-h6">{{ currentQuestion.question }}</div>
          <!--            <div class="text-subtitle2">{{ currentQuestion.name }}</div>-->
          <!--            <div class="text-subtitle2">{{ currentQuestion.owner.fullname }}</div>-->
          <div
            v-if="hinttext"
            class="text-white bg-orange q-pa-sm "
          >{{ hinttext }}
          </div>
          <div class="qdeskr scroll q-mb-md">
            {{ currentQuestion.description }}
          </div>

        </div>
        <div class="col-md-6 col-sm-12 col-xs-12">
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
        <!--        <q-linear-progress rounded size="20px" :value="progress" color="red" class="q-mt-sm"/>-->
      </q-card-section>
      <q-separator />
      <q-card-actions class="">
        <div style="position: absolute; right: 15px; bottom: -35px;">
          <q-btn
            @click="onAnswerSubmit"
            color="positive"
          >
            Svara
          </q-btn>
        </div>
      </q-card-actions>
    </q-card>
    <!--      </div>-->

    <div class="row questlist content-center ">

      <div class="content-center col ">
        <q-btn-toggle
          v-model="questNum"
          :options="questionsNumbersList"
          size="sm"
          @input="setQuestion"
        >
        </q-btn-toggle>
      </div>
    </div>

    <q-dialog
      v-model="persistent"
      persistent
      transition-show="scale"
      transition-hide="scale"
    >
      <q-card
        class=""
        style="width: 500px"
      >
        <q-toolbar class="bg-dark text-white">
          <q-avatar>
            <img src="../assets/enam-logo.svg">
          </q-avatar>
          <q-toolbar-title>Próf:</q-toolbar-title>
        </q-toolbar>

        <q-card-section class="">
         Prófið er 60 spurningar og 120 mínútur gefnar til að svara.
         Að þeim loknum lokast prófið og þá er hægt að fara yfir niðurstöður í framhaldi, eða síðar.<br>
         Ekki er hægt að stöðva tímatalningu á meðan prófið stendur yfir.
        </q-card-section>
        <q-separator></q-separator>
        <q-card-actions
          align="right"
          class="bg-white"
        >
          <q-btn
            color="positive"
            label="OK"
            @click="setupExam"
          />
        </q-card-actions>
      </q-card>
    </q-dialog>

  </q-page>
</template>

<script>
import { getAPI } from 'src/api/axios-base'
import store from 'src/store'
import { date } from 'quasar'

const access = store.getters.token

var exam = 0
export default {
  data () {
    return {
      // currentOptions: this.currentQuestion.options,
      name: 'Realtestpage',
      testFinished: false,
      hinttext: '',
      cQ: 0,
      hintloss: '',
      currTestAnsw: [],
      questionsNumbersList: [],
      questNum: 1,
      memo: false,
      memolist: false,
      calendar: false,
      memotext: '',
      difficulty: 50,
      accept: false,
      date: '2020/24/12',
      interval: 0,
      progress: 0.01,
      time_taken: 0,
      time_step: 0,
      tesing_user: 1,
      btnmodel: 'one',
      currPoints: 0,
      known: false,
      postpone: false,
      maximizedToggle: true,
      totalQuestions: 0,
      time_allowed: 0,
      totaltime: 0,
      timeTotal: 0,
      questStartTime: null,
      questTime: null,
      spinnegal: true,
      persistent: true
    }
  },
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
    timers () {
      this.totaltime = date.formatDate(this.timeTotal - Date.now(), 'HH:mm:ss').toString()
      this.questTime = date.formatDate(Date.now() - this.questStartTime, 'mm:ss').toString()
    },
    setQuestion (e) {
      var index = 0
      if (e > -1) {
        index = e - 1
      } else {
        index = 0
      }
      this.hinttext = ''
      this.editingIndex = index
      this.question = JSON.parse(JSON.stringify(this.myJson.question_collection[index]))
      store.commit({ type: 'setQuestion', payload: this.question })
      this.currPoints = this.question.points
      this.questNum = index + 1

      this.questStartTime = Date.now()
      this.timeTotal = store.getters.getTestTimeTotal
    },
    setAnswerChecked (e) {
      if (this.currentQuestion.id !== this.cQ) {
        this.cQ = this.currentQuestion.id
        this.currTestAnsw = []
      }
    },
    onMemoSubmit (e) {
      const formdata = {
        difficulty: this.difficulty,
        memo: this.memotext,
        known: this.known,
        curr_question: this.currentQuestion.id
      }
      getAPI({
        url: '/api/memos/',
        method: 'post',
        headers: { Authorization: `Bearer ${access}` },
        data: formdata
      }).catch(error => console.log('Error', error.message))
    },
    onAnswerSubmit (e) {
      if (this.currTestAnsw < 1) {
        if (confirm('Hey ætlar þú ekki að svara?\n OK merkir spurninguna til að hún gleymist ekki.')) {
          this.questionsNumbersList[this.questNum - 1].answered = true
          this.questionsNumbersList[this.questNum - 1].color = 'warning'
          this.questionsNumbersList[this.questNum - 1]['toggle-color'] = 'negative'
        }
      }

      var formdata = {
        options_ids: this.currTestAnsw.toString(),
        curr_question: parseInt(this.currentQuestion.id),
        test_practice: parseInt(this.myJson.id),
        points: parseInt(this.currPoints),
        known: this.known,
        postpone: this.postpone
      }

      getAPI({
        url: '/api/answer/',
        method: 'post',
        data: formdata,
        headers: { Authorization: `Bearer ${access}` }
      })

      this.questionsNumbersList[this.questNum - 1].answer = this.currTestAnsw
      this.questionsNumbersList[this.questNum - 1].answered = true
      this.questionsNumbersList[this.questNum - 1].color = '$primary'
      this.known = false

      var answers = 0
      var i
      for (i = 0; i < this.totalQuestions; i++) {
        if (this.questionsNumbersList[i].answered) {
          answers++
        }
      }

      if (answers === this.totalQuestions) {
        this.testFinished = true
      }

      var ii
      for (ii = 0; ii < this.totalQuestions; ii++) {
        if (!this.questionsNumbersList[ii].answered) {
          this.setQuestion(ii + 1)
          ii = this.totalQuestions
        }
      }
      // console.log(this.questionsNumbersList)
    },
    onMemoReset () {
      this.memotext = ''
      this.difficulty = 50
      this.accept = false
      this.calendar = false
      this.showDate = false
    },
    hint (e) {
      e.target.offsetParent.disabled = true
      this.hinttext = this.currentQuestion.hint
      this.currPoints = this.currentQuestion.points - this.currentQuestion.hint_cost
    },
    openUrl () {
      window.open('https://api.enam.is/admin/questions/question/' + this.currentQuestion.id, '_blank')
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
    showTooltip (e) {
      // console.log(e)
    },
    timerCount () {
      this.time_allowed = this.currentQuestion.time_allowed // 10 // til að stytta
    },
    reviewTest () {
      this.testFinished = false
      this.$router.push({ path: '/review', params: { exam: 52 } }).catch(err => {
        console.log(err.message)
      })
    },
    setupExam () {
      const username = store.getters.getUserName
      this.persistent = false
      getAPI({
        url: '/api/realtest/',
        method: 'post',
        data: {
          user: username,
          timed: true,
          time_allowed: 0
        },
        headers: { Authorization: `Bearer ${access}` }
      })
        .then(response => {
          // console.log(response.data)
          this.myJson = JSON.parse(JSON.stringify(response.data))
          this.totalQuestions = this.myJson.question_collection.length
          var i
          var qs = []
          for (i = 0; i < this.totalQuestions; i++) {
            // console.log(this.myJson.question_collection[i].name)
            qs.push({
              label: i + 1,
              value: i + 1,
              slot: i + 1,
              title: this.myJson.question_collection[i].name,
              color: 'info',
              answered: false,
              answer: 0
            })
          }
          this.$store.dispatch('setTestTimeTotal', date.addToDate(Date.now(), { minutes: 120 }))
          this.questionsNumbersList = qs
          this.setQuestion(1)
          this.spinnegal = false
        })
        .catch(error => console.log('Error', error.message))
    }
  },
  updated () {
    this.setAnswerChecked()
  },
  created () {
    if (exam > 0) {
      alert('CREATED REVIEW')
    }
    this.clock = setInterval(this.timers, 1000)
  }
}

</script>

<style scoped lang="sass">
.memowing
  width: 400px

//.my-card
//  margin: 5% auto
//  @media screen and (max-width: $breakpoint-xs)
//    margin-top: 10px
//    margin-bottom: 30px
//    margin-right: 5px
//    margin-left: 8px

.tpage
  @media screen and (max-width: $breakpoint-xs)
//padding-top: 130px
//padding-bottom: 230px

.quest-options
  border: 1px solid #d0d0d0
  padding: 5px
  margin: 5px 0
  background-color: #eaeaea

.questlist
  padding: 10px 20px
  width: 100%
  position: fixed
  bottom: 0px
  margin: 0px
  background-color: $primary
  //min-height: 40px
  overflow: scroll
  text-align: center

.qdeskr
  max-height: 250px
  overflow: scroll
//padding-right: 10px
</style>
