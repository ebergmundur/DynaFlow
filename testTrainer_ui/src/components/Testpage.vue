<template>
  <div class="tpage q-pa-md row items-start q-gutter-md scroll">

    <q-dialog v-model="testFinished">
      <q-card>
        <q-toolbar>
          <q-avatar>
            <img src="../assets/enam-logo.svg">
          </q-avatar>
          <q-toolbar-title><span class="text-weight-bold">E-nám</span> Ljúka prófi?</q-toolbar-title>
          <q-btn flat round dense icon="close" v-close-popup/>
        </q-toolbar>
        <q-card-section class="scroll">
          Viltu fara í gegnum svörin núna?

          <q-btn
            @click="reviewTest"
          >
            Já endilega hreint.
          </q-btn>

        </q-card-section>
      </q-card>
    </q-dialog>

    <q-dialog v-model="memo">
      <q-card>
        <q-toolbar>
          <q-avatar>
            <img src="../assets/enam-logo.svg">
          </q-avatar>

          <q-toolbar-title><span class="text-weight-bold">E-nám</span> minnismiðar</q-toolbar-title>

          <q-btn flat round dense icon="close" v-close-popup/>
        </q-toolbar>

        <!--        style="max-height: 70vh; width: 30vw;"-->
        <q-card-section class="scroll">

          <h6 class=" q-ma-sm">{{ currentQuestion.name }}</h6>
          <q-form
            @submit="onMemoSubmit"
            @reset="onMemoReset"
            class="q-gutter-md"
          >
            <div class="q-pa-md q-ma-sm">

              Þyngd: {{ difficulty / 10 }}
              <q-slider
                v-model="difficulty"
                :step="10"
              />
            </div>

            <div class="q-pa-md q-ma-xs">
              <q-input
                v-model="memotext"
                filled
                type="textarea"
              />
            </div>
            <q-toggle v-model="known" label="Kann vel " class=" q-ma-sm"/>
            <!--            <span v-if="showDate">{{ formDate }}</span><br>-->
            <!--            <q-date v-if="showDate" v-model="date" minimal/>-->
            <div>
              <q-btn label="Skrá" type="submit" color="primary"/>
              <q-btn label="Hreinsa" type="reset" color="primary" flat class="q-ml-sm"/>
            </div>
          </q-form>
        </q-card-section>
      </q-card>
    </q-dialog>

    <!--MEMOS-->
    <q-dialog v-model="memolist" position="right">
      <q-card>
        <q-card-section class="row items-center q-pb-none">
          <div class="text-h6">Minnismiðar</div>
          <q-space/>
          <q-btn icon="close" flat round dense v-close-popup/>
        </q-card-section>
        <q-card-section>
          <div class="q-pa-md row items-start q-gutter-md">

            <q-card
              flat bordered
              class="my-card bg-grey-1 scroll "
              v-for="(data) in currentQuestion.memos"
              :key="data.id"
            >
              <q-card-section>
                <div class="row items-center no-wrap">
                  <div class="col">

                    <div class="text-h6">
                      <!--                      {{ formatDate(data.created_date) }}-->

                      <q-toggle v-model="data.known" label="Kann vel " class=" q-ma-sm" disable/>
                    </div>
                    <!--                <div class="text-h6">{{formatDate(data.created_date)}}</div>-->
                    <div class="text-subtitle2">
                      Þyngd: {{ data.difficulty }}
                      <q-linear-progress size="25px" :value="data.difficulty/10" color="red" class="q-mt-sm"/>
                    </div>
                  </div>
                </div>
              </q-card-section>

              <q-card-section>
                {{ data.memo }}
              </q-card-section>

              <q-separator/>

              <q-card-actions>

                <q-btn>Í geymslu</q-btn>
                <!--            <q-btn>Minna á síðar</q-btn>-->
              </q-card-actions>
            </q-card>
          </div>
        </q-card-section>
      </q-card>
    </q-dialog>

    <q-card bordered
            class="my-card bg-grey-1 col-xs-12 col-sm-12 col-md-10 col-lg-6 q-my-xs-lg q-my-sm-lg q-mx-xs-none"
            v-model='currentQuestion'
            v-if="currentQuestion"
    >
      <!--            style="max-height: 80vh; width: 40%;"-->
      <q-toolbar class="q-dark" style="background-color: #616161;">
        <q-toolbar-title>
          {{ questNum }} / {{ totalQuestions }} | {{ myJson.name }}
        </q-toolbar-title>
        <div class="col-auto">
          <q-toggle v-model="known" value="false" label="Kann vel " class=" q-ma-sm"/>
          <!--          <q-toggle v-model="postpone" value="false" label="Sleppa " class=" q-ma-sm"/>-->

          <q-btn label="Minnismiðar" icon="">
            <q-menu cover auto-close>
              <q-list>
                <q-btn
                  v-if="currentQuestion.memos.length > 0"
                  @click="openMemos"
                  color="orange"
                  style="width: 100%"
                >
                  Minnismiðar {{ currentQuestion.memos.length }}
                </q-btn>
                <br>
                <q-btn
                  color="green"
                  @click="memo = true"
                  style="width: 100%"
                >
                  Nýr minnismiði
                </q-btn>
              </q-list>
            </q-menu>
          </q-btn>
          <q-btn
            color="blue"
            @click="openUrl"
            label="E"
          />
        </div>
      </q-toolbar>
      <q-card-section class="row col">
        <div class="col-md-6 q-pr-lg ">
          <div class="text-h6">{{ currentQuestion.question }}</div>
          <!--            <div class="text-subtitle2">{{ currentQuestion.name }}</div>-->
          <!--            <div class="text-subtitle2">{{ currentQuestion.owner.fullname }}</div>-->
          <div
            v-if="hinttext"
            class="text-white bg-orange q-pa-sm ">{{ hinttext }}
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
      <q-separator/>
      <q-card-actions>
        <div class="text-h5 ">
          {{ currPoints }} stig &nbsp;
          <!--          <span q-red>{{hintloss}}</span>&nbsp;-->
        </div>
        <q-btn
          v-if="currentQuestion.hint.length"
          @click="hint">„Tips“ {{ currentQuestion.hint_cost }} stig
        </q-btn>

        <q-btn
          @click="onAnswerSubmit"
          color="green"
        >
          Svara
        </q-btn>

      </q-card-actions>
    </q-card>

    <div class="questlist">
      <q-btn-toggle
        v-model="questNum"
        :options="questionsNumbersList"
        size="sm"
        @input="setQuestion"
      >
      </q-btn-toggle>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import store from '../router/store'
import { date } from 'quasar'
// import { clock } from './Clock'
// import Question from 'components/Question'
// import { date } from 'quasar'
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
      interval: 0,
      progress: 0.01,
      time_allowed: 0,
      time_taken: 0,
      time_step: 0,
      tesing_user: 1,
      btnmodel: 'one',
      currPoints: 0,
      known: false,
      postpone: false,
      maximizedToggle: true,
      totalQuestions: 0
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
      // store.commit({ type: 'setTestQuestion', payload: [] })
      // Question.setAnswerChecked()
      this.currPoints = this.question.points
      this.questNum = index + 1
    },
    setAnswerChecked (e) {
      if (this.currentQuestion.id !== this.cQ) {
        this.cQ = this.currentQuestion.id
        this.currTestAnsw = []
        // this.progress = 0.001
      }
    },
    onMemoSubmit (e) {
      const formdata = {
        difficulty: this.difficulty,
        memo: this.memotext,
        known: this.known,
        curr_question: this.currentQuestion.id
      }
      axios({
        method: 'post',
        url: 'http://einars-macbook-pro.local:8000/api/memos/',
        data: formdata
      }).catch(error => console.log('Error', error.message))
    },
    onAnswerSubmit (e) {
      if (this.currTestAnsw < 1) {
        if (confirm('Hey ætlar þú ekki að svara?\n OK merkir spurninguna til að hún gleymist ekki.')) {
          this.questionsNumbersList[this.questNum - 1].answered = true
          this.questionsNumbersList[this.questNum - 1].color = 'warning'
          this.questionsNumbersList[this.questNum - 1]['toggle-color'] = 'negative'
          // console.log(this.questionsNumbersList)
          // this.setQuestion(this.questNum + 1)
        }
      }

      var formdata = {
        // time_allowed: this.time_allowed,
        // time_taken: parseInt(this.time_taken),
        options_ids: this.currTestAnsw.toString(),
        curr_question: parseInt(this.currentQuestion.id),
        test_practice: parseInt(this.myJson.id),
        points: parseInt(this.currPoints),
        known: this.known,
        postpone: this.postpone
      }

      axios({
        method: 'post',
        url: 'http://einars-macbook-pro.local:8000/api/answer/',
        data: formdata
      })

      this.questionsNumbersList[this.questNum - 1].answer = this.currTestAnsw
      this.questionsNumbersList[this.questNum - 1].answered = true
      this.questionsNumbersList[this.questNum - 1].color = 'positive'
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
      window.open('http://einars-macbook-pro.local:8000/admin/questions/question/' + this.currentQuestion.id, '_blank')
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
      console.log(e)
    },
    formatOptions () {
      if (this.currentQuestion.single_selection) {
        return 'radio'
      } else {
        return 'checkbox'
      }
      // },
      // questionsNumbers (id) {
      //   var i
      //   var qs = []
      //   for (i = 0; i < this.myJson.question_collection.length; i++) {
      //     // console.log(this.myJson.question_collection[i].name)
      //     qs.push({
      //       label: i + 1,
      //       value: i,
      //       slot: this.myJson.question_collection[i].name,
      //       answered: false
      //     })
      //   }
      //   // console.log(qs)
      //   this.questionsNumbersList = qs
    },
    timerCount () {
      this.time_allowed = this.currentQuestion.time_allowed // 10 // til að stytta
      // this.time_step = 1 / this.time_allowed
      // this.time_taken = this.progress * this.time_allowed
      // if (this.progress > 1.0) {
      //   // alert('Tíminn búinn')
      //   this.progress = 0.001
      // } else {
      //   this.progress = this.progress + this.time_step
      // }
    },
    reviewTest () {
      this.testFinished = false
      this.$router.push({ path: '/review', params: { exam: 52 } }).catch(err => {
        console.log(err.message)
      })
    }
  },
  mounted () {
    if (exam > 0) {
      alert('MOUNTED REVIEW')
    }
    axios('http://einars-macbook-pro.local:8000/api/questionn/68/?format=json')
      .then(response => {
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
        // console.log(qs)
        this.questionsNumbersList = qs
        store.commit({ type: 'setTimeAllowed', payload: this.myJson.time_allowed + 0 })
        // console.log(this.myJson.time_allowed)

        // console.log(clock)
        // clock.limit = this.myJson.time_allowed * (60000)

        this.setQuestion(1)
      })
      .catch(error => console.log('Error', error.message))

    // this.myJson = JSON.parse(JSON.stringify(json))
    // this.interval = setInterval(() => {
    //   this.timerCount()
    // }, 1000)
  },
  updated () {
    this.setAnswerChecked()
  },
  created () {
    if (exam > 0) {
      alert('CREATED REVIEW')
    }
  }
}

</script>

<style scoped lang="sass">

.my-card
  margin: 5% auto
  @media screen and (max-width: $breakpoint-xs)
    margin-top: 10px
    margin-bottom: 30px
    margin-right: 5px
    margin-left: 8px

.tpage
  @media screen and (max-width: $breakpoint-xs)
    //padding-top: 130px
    //padding-bottom: 230px

.quest-options
  border: 1px solid #8d8c8c
  padding: 5px
  margin: 5px 0
  background-color: #eaeaea

.questlist
  padding: 10px 20px
  width: 100%
  position: fixed
  bottom: 0px
  margin: 60px 0 0 0
  background-color: #9ab2d0
  min-height: 40px
  overflow: scroll
  text-align: center

.qdeskr
  max-height: 250px
  overflow: scroll
//padding-right: 10px
</style>
