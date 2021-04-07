<template>
  <q-page class="flex flex-center">
    <q-card flat
            class="pagecard"
    >
        <q-toolbar class="q-dark">
          <q-toolbar-title>
            {{ testname }}
<!--            {{ formatDate(testdate) }}-->

            <span class="" style="float: right">
          {{ totpoints }} af {{ optpoints }} = {{ Math.round((totpoints / optpoints) * 100) }}%
          </span>
          </q-toolbar-title>
        </q-toolbar>
      <q-card-section>
        <q-list bordered class="zrounded-borders questlist ">
          <q-expansion-item
            v-for="(item, index) in currTestAnsw"
            :key="index"
            :class="iscorrect( item.result, item.question.category.order )"
            expand-separator
            group="item.question.category.name"
            :label="item.question.question"
            :caption="item.question.category.name + ' –  minnismiðar: ' + item.question.memos.length"
          >
            <q-card-section style="background-color: white;" class="row quest-options">
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
              <strong>{{ formatDate(memo.created_date) }}:</strong> {{ memo.memo }}
              <strong>Þyngd:</strong> {{ memo.difficulty }} <span v-if="memo.known"> – Kann vel</span><br>
            </span>
              </div>

            </q-card-section>
          </q-expansion-item>
        </q-list>
        </q-card-section>
        <q-card-section>
        <q-card-actions>
        <q-btn @click="dashboard" color="positive" label="Mælaborð"/>
      </q-card-actions>
        </q-card-section>
    </q-card>
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
    dashboard () {
      this.$router.push({ path: '/dashboard/allt' }).catch(err => {
        console.log(err.message)
      })
    },
    onMemoReset () {
      this.memotext = ''
      this.difficulty = 50
      this.accept = false
      this.calendar = false
      this.showDate = false
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
    catColor (i) {
      return 'cat-' + 1
    },
    iscorrect (i, ii) {
      // console.log(p)
      // console.log('totpoints')
      // console.log(this.totpoints)
      // this.totpoints = this.totpoints + p

      if (i === 1) {
        return 'correct ccat-' + ii
      } else if (i === 0) {
        return 'postponed ccat-' + ii
      } else {
        return 'wrong ccat-' + ii
      }
    },
    reviewTest () {
      this.testFinished = false
      this.$router.push({ path: '/review' }).catch(err => {
        console.log(err.message)
      })
    }
  },
  computed: {
    reviewId () {
      return this.$route.params.id || 0
    }
  },
  mounted () {
    // if (exam > 0) {
    //   alert('MOUNTED REVIEW'
    // }

    // console.log(store.getters.getUserInfo)

    getAPI({
      url: '/api/review/',
      method: 'post',
      data: {
        id: this.reviewId,
        username: store.getters.getUserInfo.username
      },
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
          this.totpoints = this.totpoints + this.currTestAnsw[i].points_given
          this.optpoints = this.optpoints + this.currTestAnsw[i].points

          qs.push({
            label: i + 1,
            value: i + 1,
            slot: i + 1,
            color: 'info',
            answered: false,
            answer: 0
          })
        }
        this.questionsNumbersList = qs
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
      // alert('CREATED REVIEW')
    }
  }
}

</script>

<style scoped lang="sass">

.quest-options
  padding: 5px 25px

.questlist
  background-color: #fdfdfd
  .q-expansion-item
    border-bottom: 1px solid #bcbcbc

.mainlist
  text-align: left

.correct
  border-left: 6px solid #559f02

.postponed
  border-left: 6px solid #ece563

.wrong
  border-left: 6px solid #dd3333

.redborder
  border: 1px solid red

.ccat-1
  border-right: 12px solid $cat-1

.ccat-2
  border-right: 12px solid $cat-2

.ccat-3
  border-right: 12px solid $cat-3

.ccat-4
  border-right: 12px solid $cat-4

.ccat-5
  border-right: 12px solid $cat-5

</style>
