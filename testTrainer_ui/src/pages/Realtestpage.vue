<template>
  <q-page class="flex q-pa-none self-start">
    <div  class="q-pt-lg pagecard tpage">

    <!-- <q-dialog
      v-model="prolog"
      persistent
      transition-show="scale"
      transition-hide="scale"
      full-height
      full-width
    > -->
      <!-- <q-card class="column full-height full-width"> -->
        <q-toolbar class="bg-dark text-white">
          <!-- <q-avatar>
            <img src="../assets/enam-logo.svg" />
          </q-avatar> -->
          <q-toolbar-title>Próf:</q-toolbar-title>
        </q-toolbar>

        <q-card-section class="text-h4" >
          Prófið er 60 spurningar og 120 mínútur gefnar til að svara. Að þeim
          loknum lokast prófið og þá er hægt að fara yfir niðurstöður í
          framhaldi, eða síðar.
          Ekki er hægt að stöðva tímatalningu á meðan prófið stendur yfir.

          <q-banner inline-actions class="text-white bg-red q-mt-md ">
      <div class="text-h4 text-center">Prófið hefst þegar smellt er á grein</div>
    </q-banner>
        </q-card-section>
        <q-separator></q-separator>

        <!-- <div class="q-pa-md">
    <q-btn-group spread>
      <q-btn
        v-for="cat in categories"
        :key="cat.name"
        :ref="cat.id"
        :label="cat.name"
        :icon="cat.icon"
        stack
        size="xl"
      />
    </q-btn-group>
  </div> -->

        <q-card-section class="">
          <div class="row wrap q-gutter-md justify-evenly">
            <q-card
              v-for="cat in categories"
              :key="cat.category.name"
              :ref="cat.category.id"
              class="col-xs-12 col-sm-12 col-md-4 col-lg"
            >
              <q-toolbar class="q-dark text-center">
                <q-toolbar-title >
                  {{ cat.category.name }}
                </q-toolbar-title>
              </q-toolbar>
               <q-item clickable class="flex-center" :to="'/test/'+cat.category.id">
              <q-card-section class="text-center" >
               <!-- <q-item clickable class="flex-center" @click="catSelect(cat.id)"> -->
                <q-icon :name="cat.category.icon" size="12vh"  />
              </q-card-section>
                </q-item>
                <q-card-section class="text-center">
                <div  class="text-h5">
                 {{cat.answcount}} af {{cat.catcount}} lokið
                <q-linear-progress  rounded size="20px" :value="cat.answcount/cat.catcount" :class="cat.category.color_class" />
                </div>
                <div class="q-pt-none text-justify"  v-html="cat.category.description">
                </div>
              </q-card-section>

            </q-card>
          </div>
        </q-card-section>

        <!-- <q-separator></q-separator> -->
        <!-- <q-card-actions align="right" class="bg-white">
          <q-btn color="positive" size="lg"  label="Byrja próf" /> -->
          <!-- @click="setupExam" -->
        <!-- </q-card-actions> -->

      </div>
    <!-- </q-dialog> -->
  </q-page>
</template>

<script>
import { getAPI } from 'src/api/axios-base'
import store from 'src/store'
import { date } from 'quasar'

const access = store.getters.token

export default {
  data () {
    return {
      // currentOptions: this.currentQuestion.options,
      name: 'Realtestpage',
      categories: [],
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
      prolog: true
    }
  },
  computed: {
    // currentQuestion () {
    //   return store.getters.currQest.payload
    // },
    // formDate () {
    //   return date.formatDate(this.date, 'YYYY-MM-DD')
    // },
    // currentOptions () {
    //   return store.getters.currQest.payload.options
    // }
  },
  methods: {
    catSelect (catid) {
      console.log(this.$refs[catid])
      // this.$refs[catid].$el.lastElementChild
    },
    timers () {
      // this.totaltime = date
      //   .formatDate(this.timeTotal - Date.now(), 'HH:mm:ss')
      //   .toString()
      // this.questTime = date
      //   .formatDate(Date.now() - this.questStartTime, 'mm:ss')
      //   .toString()
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
      this.question = JSON.parse(
        JSON.stringify(this.myJson.question_collection[index])
      )
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
        if (
          confirm(
            'Hey ætlar þú ekki að svara?\n OK merkir spurninguna til að hún gleymist ekki.'
          )
        ) {
          this.questionsNumbersList[this.questNum - 1].answered = true
          this.questionsNumbersList[this.questNum - 1].color = 'warning'
          this.questionsNumbersList[this.questNum - 1]['toggle-color'] =
            'negative'
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
      this.currPoints =
        this.currentQuestion.points - this.currentQuestion.hint_cost
    },
    openUrl () {
      window.open(
        'https://api.enam.is/admin/questions/question/' +
          this.currentQuestion.id,
        '_blank'
      )
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
          this.$store.dispatch(
            'setTestTimeTotal',
            date.addToDate(Date.now(), { minutes: 120 })
          )
          this.questionsNumbersList = qs
          this.setQuestion(1)
          this.spinnegal = false
        })
        .catch(error => console.log('Error', error.message))
    }
  },
  // beforeMount () {
  //   getAPI({
  //     url: '/api/category/',
  //     method: 'get',
  //     headers: { Authorization: `Bearer ${access}` }
  //   })
  //     .then(response => {
  //       const rdata = JSON.parse(JSON.stringify(response.data))
  //       var i
  //       for (i = 0; i < rdata.length; i++) {
  //         // console.log(this.myJson.question_collection[i].name)
  //         this.categories.push(rdata[i])
  //       }
  //     })
  //     .catch(error => console.log('Error', error.message))
  // },
  mounted () {
    const username = store.getters.getUserName
    getAPI({
      url: '/api/catstat/',
      method: 'post',
      data: {
        user: username,
        timed: true,
        time_allowed: 0
      },
      headers: { Authorization: `Bearer ${access}` }
    })
      .then(response => {
        this.categories = JSON.parse(JSON.stringify(response.data))
        console.log(this.categories)
        // var i
        // for (i = 0; i < rdata.length; i++) {
        //   // console.log(this.myJson.question_collection[i].name)
        //   this.categories.push(rdata[i])
        // }
      })
      .catch(error => console.log('Error', error.message))
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
