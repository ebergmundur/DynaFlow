<template>
  <q-page class="flex flex-center q-pa-xs ">
    <div class="q-pa-md row items-start q-gutter-md justify-center">
      <div class="mainlist col-lg-6 col-md-8 col-sm ">
        <q-toolbar>
          <q-toolbar-title>
            {{ testname }} -
            {{ formatDate(testdate) }}

            <span class="" style="float: right">
          {{ totpoints }} af {{ optpoints }} = {{ Math.round((totpoints / optpoints) * 100) }}%
          </span>
          </q-toolbar-title>
        </q-toolbar>
        <q-list bordered class="rounded-borders">
          <q-expansion-item
            v-for="(item, index) in currTestAnsw"
            :key="index"
            :class="iscorrect( item.result)"
            expand-separator
            :label="item.question.virtname"
            class=""
          >
            <q-card-section style="background-color: white;" class="row">
              <div class="col-6">
            <span v-for="(opt, idx) in item.question.options"
                  :key="idx"
            >
                <span
                  v-if="parseInt(item.options_ids * 1) == opt.id"
                  class="float-left"
                >
                  <strong>Þitt svar:</strong> {{ opt.answer }}<br>
                  <strong> {{ item.points_given }} stig </strong>
                </span>
            </span>
                <span v-if="item.result === 0">
                          <strong>Spurningu sleppt</strong><br>
                  <strong> {{ item.points_given }} stig </strong>
                        </span>
              </div>

              <div class="col-6 ">
            <span v-for="(memo, innx) in item.question.memos"
                  :key="innx"
            >
              <strong>{{ formatDate(memo.created_date) }}:</strong> {{ memo.memo }}<br>
            </span>
              </div>

            </q-card-section>
          </q-expansion-item>
        </q-list>

        <!--      <q-card-->
        <!--        v-for="(item, index) in myJson.answers"-->
        <!--        :key="index"-->
        <!--      >-->
        <!--        <q-toolbar class="q-dark">-->
        <!--          {{ item.question.name }}-->
        <!--        </q-toolbar>-->
        <!--        <q-card-section>-->
        <!--          &lt;!&ndash;          //{{ item.result }}&ndash;&gt;-->
        <!--          {{ item.options_ids }}-->
        <!--          <q-card-section-->
        <!--            v-for="(opt, idx) in item.question.options"-->
        <!--            :key="idx"-->
        <!--          >-->
        <!--            {{ opt.id }}: {{ opt.answer }}-->
        <!--          </q-card-section>-->
        <!--        </q-card-section>-->

        <!--      </q-card>-->
      </div>
      <!--    MAIN CARDS-->

      <!--    BOTTOM LIST OF QUESTIONS-->
      <!--    <div class="questlist ">-->
      <!--      &lt;!&ndash;      <q-page-sticky expand position="bottom" class="questlist ">&ndash;&gt;-->
      <!--      <q-btn-toggle-->
      <!--        v-model="questNum"-->
      <!--        :options="questionsNumbersList"-->
      <!--        size="sm"-->
      <!--      >-->
      <!--        &lt;!&ndash;        @input="setQuestion"&ndash;&gt;-->
      <!--      </q-btn-toggle>-->
      <!--      &lt;!&ndash;      </q-page-sticky>&ndash;&gt;-->
      <!--    </div>-->
    </div>
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
      name: 'Testpage',
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
      known: false,
      interval: 0,
      progress: 0.01,
      time_allowed: 0,
      time_taken: 0,
      time_step: 0,
      tesing_user: 1,
      btnmodel: 'one',
      currPoints: 0,
      postpone: false,
      myJson: null,
      optpoints: 0,
      totpoints: 0,
      totalQuestions: 0,
      testdate: '2020-01-01',
      testname: 'Próf'
    }
  },
  methods: {
    // setQuestion (e) {
    //   var index = 0
    //   if (e > -1) {
    //     index = e - 1
    //   } else {
    //     index = 0
    //   }
    //   this.hinttext = ''
    //   this.editingIndex = index
    //   this.question = JSON.parse(JSON.stringify(this.myJson.answers[index]))
    //   index.commit({ type: 'setQuestion', payload: this.question })
    //   // index.commit({ type: 'setTestQuestion', payload: [] })
    //   // Question.setAnswerChecked()
    //   this.currPoints = this.question.points
    //   this.questNum = index + 1
    // },
    // setAnswerChecked (e) {
    //   if (this.currentQuestion.id !== this.cQ) {
    //     this.cQ = this.currentQuestion.id
    //     this.currTestAnsw = []
    //     // this.progress = 0.001
    //   }
    // },
    // onMemoSubmit (e) {
    //   const formdata = {
    //     difficulty: this.difficulty,
    //     memo: this.memotext,
    //     known: this.known,
    //     curr_question: this.currentQuestion.id
    //   }
    //   axios({
    //     method: 'post',
    //     url: 'http://einars-macbook-pro.local:8000/api/memos/',
    //     data: formdata
    //   })
    // },
    onMemoReset () {
      this.memotext = ''
      this.difficulty = 50
      this.accept = false
      this.calendar = false
      this.showDate = false
    },
    openUrl () {
      window.open('https://127.0.0.1:8000/admin/questions/question/' + this.currentQuestion.id, '_blank')
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
    formatOptions () {
      if (this.currentQuestion.single_selection) {
        return 'radio'
      } else {
        return 'checkbox'
      }
    },
    iscorrect (i) {
      // console.log(p)
      // console.log('totpoints')
      // console.log(this.totpoints)
      // this.totpoints = this.totpoints + p

      if (i === 1) {
        return 'correct'
      } else if (i === 0) {
        return 'postponed'
      } else {
        return 'wrong'
      }
    },
    reviewTest () {
      this.testFinished = false
      this.$router.push({ path: '/review', params: { exam: 50 } }).catch(err => {
        console.log(err.message)
      })
    }
  },
  mounted () {
    if (exam > 0) {
      alert('MOUNTED REVIEW')
    }
    getAPI({
      url: '/api/review/76/?format=json',
      method: 'get',
      headers: { Authorization: `Bearer ${access}` }
    })
      .then(response => {
        this.myJson = JSON.parse(JSON.stringify(response.data))
        // console.log(this.myJson)
        this.totalQuestions = this.myJson.answers.length
        // console.log(this.totalQuestions)
        var i
        var qs = []
        this.testname = this.myJson.name
        this.testdate = this.myJson.created_date
        this.currTestAnsw = this.myJson.answers

        for (i = 0; i < this.totalQuestions; i++) {
          // console.log(this.myJson.answers[i])
          this.totpoints = this.totpoints + this.myJson.answers[i].points_given
          this.optpoints = this.optpoints + this.myJson.answers[i].points

          qs.push({
            label: i + 1,
            value: i + 1,
            slot: i + 1,
            color: 'info',
            answered: false,
            answer: 0
          })
        }
        // console.log(qs)
        this.questionsNumbersList = qs
        // index.commit({ type: 'setTimeAllowed', payload: this.myJson.time_allowed + 0 })
        // console.log(this.myJson.time_allowed)

        // console.log(clock)
        // clock.limit = this.myJson.time_allowed * (60000)

        // this.setQuestion(1)
      })
      .catch(error => console.log('Error', error.message))

    // this.myJson = JSON.parse(JSON.stringify(json))
    // this.interval = setInterval(() => {
    //   this.timerCount()
    // }, 1000)
  },
  updated () {
    // this.setAnswerChecked()
  },
  created () {
    if (exam > 0) {
      alert('CREATED REVIEW')
    }
  }
}

</script>

<style scoped lang="sass">
.quest-options
  border: 1px solid #8d8c8c
  padding: 5px
  margin: 5px 0
  background-color: #eaeaea

.questlist
  padding: 10px 20px
  width: 100%
  position: absolute
  bottom: 50px
  margin: 0 auto
  background-color: #9ab2d0
  min-height: 40px
  overflow: scroll
  text-align: center

.mainlist
  text-align: left

.correct
  background-color: #e7f3da

.postponed
  background-color: #faf5a8

.wrong
  background-color: #f3c7c7

.redborder
  border: 1px solid red

</style>
