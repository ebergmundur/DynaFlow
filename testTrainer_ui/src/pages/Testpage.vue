<template>
  <q-page class="flex flex-center">

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

          <h6 class=" q-ma-sm">{{ currentQuestion.virtname }}</h6>
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
      <q-card class="memowing">
        <q-card-section class="row items-center q-pb-none col-lg-8">
          <div class="text-h6">Minnismiðar</div>
          <q-space/>
          <q-btn icon="close" flat round dense v-close-popup/>
        </q-card-section>
        <q-card-section>
          <div class="q-pa-md items-start q-gutter-md col">

            <q-card
              flat bordered
              class="my-card bg-grey-1 scroll col"
              v-for="(data) in currentQuestion.memos"
              :key="data.id"
            >
              <q-card-section>
                <div class="row items-center no-wrap">
                  <div class="col">
                    <div class="text-h6">{{ formatDate(data.created_date) }}</div>
                    <div>
                      <q-toggle v-model="data.known" label="Kann vel " class=" q-ma-sm" disable/>
                      <q-toggle v-model="data.postpone" label="Geymd" class=" q-ma-sm" disable/>
                    </div>
                    <div class="text-subtitle2">
                      Þyngd: {{ data.difficulty }}
                      <q-linear-progress size="14px" :value="data.difficulty/15" color="red" track-color="orange"
                                         class="q-mt-sm"/>
                    </div>
                  </div>
                </div>
                <div class="text-subtitle2 q-mt-sm">Minnistatriði</div>
                {{ data.memo }}
              </q-card-section>
            </q-card>
          </div>
        </q-card-section>
      </q-card>
    </q-dialog>

    <!--    <div class="row col redborder">-->
    <q-card flat
            class="pagecard"
            v-model='currentQuestion'
            v-if="currentQuestion"
    >
      <q-toolbar class="q-dark">
        <q-toolbar-title>

          {{ totaltime }} | {{ currentQuestion.category.name }}

          <!--          <q-btn-->
          <!--            color="blue"-->
          <!--            @click="openUrl"-->
          <!--            label="E"-->
          <!--          />-->

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
      <q-card-actions class="">
        <q-checkbox v-model="known" value="false" label="Kann vel " class=" q-ma-sm"/>
        <q-checkbox v-model="postpone" value="false" label="Geyma" class=" q-ma-sm"/>

        <div class="text-h5 ">
          {{ currPoints }} stig &nbsp;
          <!--          <span q-red>{{hintloss}}</span>&nbsp;-->
        </div>

        <q-btn
          v-if="currentQuestion.hint.length"
          @click="hint">„Tips“ {{ currentQuestion.hint_cost }} stig
        </q-btn>
        &nbsp;
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

        <div style="position: absolute; right: 15px;" class="">

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
      totalQuestions: 0,
      totaltime: 0,
      timeTotal: 0,
      questStartTime: null,
      questTime: null,
      spinnegal: true
    }
  },
  computed: {
    currentQuestion () {
      return store.getters.currQest.payload
    },
    currentOptions () {
      return store.getters.currQest.payload.options
    }
  },
  methods: {
    timers () {
      this.totaltime = date.formatDate(Date.now() - this.timeTotal, 'HH:mm:ss').toString()
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
      this.timeTotal = store.getters.getTimeTotal
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
    }
  },
  mounted () {
    const username = store.getters.getUserName

    getAPI({
      url: '/api/questionnaiere/?user=' + username,
      headers: { Authorization: `Bearer ${access}` }
    })
      .then(response => {
        // console.log(response.data)
        this.myJson = JSON.parse(JSON.stringify(response.data[0]))
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
        this.startTime = Date.now()
        this.$store.dispatch('setTotalTime', Date.now())
        this.questionsNumbersList = qs
        this.setQuestion(1)
      })
      .catch(error => console.log('Error', error.message))
  },
  updated () {
    this.setAnswerChecked()
  },
  created () {
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
