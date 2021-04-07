<template>
  <q-page class="flex q-pa-none self-start column">
    <q-dialog
      v-model="testFinished"
      persistent
      transition-show="scale"
      transition-hide="scale"
    >
      <q-card>
        <q-toolbar class="bg-dark text-white">
          <!-- <q-avatar>
            <img src="../assets/enam-logo.svg" />
          </q-avatar> -->
          <q-toolbar-title>
            <span class="text-weight-bold">E-nám</span>
            Ljúka prófi?
          </q-toolbar-title>
          <q-btn flat round dense icon="close" v-close-popup />
        </q-toolbar>
        <q-card-section class="scroll">
          Viltu fara í gegnum niðurstöður núna?
        </q-card-section>
        <q-card-action class="q-ma-md">
          <q-btn @click="reviewTest" color="positive" class="q-ma-md">
            Já, takk.
          </q-btn>
          <q-btn @click="testFinished = false" color="negative" class="q-ma-md">
            Nei, takk. Skoða prófið aftur.
          </q-btn>
        </q-card-action>
      </q-card>
    </q-dialog>

    <q-dialog v-model="memo">
      <q-card>
        <q-toolbar>
          <!-- <q-avatar>
            <img src="../assets/enam-logo.svg" />
          </q-avatar> -->

          <q-toolbar-title>
            <span class="text-weight-bold">E-nám</span>
            minnismiðar
          </q-toolbar-title>

          <q-btn flat round dense icon="close" v-close-popup />
        </q-toolbar>

        <!--        style="max-height: 70vh; width: 30vw;"-->
        <q-card-section class="scroll">
          <h6 class="q-ma-sm">{{ currentQuestion.virtname }}</h6>
          <q-form
            @submit="onMemoSubmit"
            @reset="onMemoReset"
            class="q-gutter-md"
          >
            <div class="q-pa-md q-ma-sm">
              Þyngd: {{ difficulty / 10 }}
              <q-slider v-model="difficulty" :step="10" />
            </div>

            <div class="q-pa-md q-ma-xs">
              <q-input v-model="memotext" filled label="Minnisatriði" autogrow type="textarea" />
            </div>
            <div style="float: left">
              <q-toggle v-model="known" label="Kann vel " class="q-ma-sm" />
            </div>
            <div align="right" >
              <q-btn
                label="Hreinsa"
                type="reset"
                color="primary"
                class="q-ma-md"
              />
              <q-btn label="Skrá" type="submit" color="positive" class="q-ma-md" />
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
          <q-space />
          <q-btn icon="close" flat round dense v-close-popup />
        </q-card-section>
        <q-card-section>
          <div class="q-pa-md items-start q-gutter-md col">
            <q-card
              flat
              bordered
              class="my-card bg-grey-1 scroll col"
              v-for="data in currentQuestion.memos"
              :key="data.id"
            >
              <q-card-section>
                <div class="row items-center no-wrap">
                  <div class="col">
                    <div class="text-h6">
                      {{ formatDate(data.created_date) }}
                    </div>
                    <div>
                      <q-toggle
                        v-model="data.known"
                        label="Kann vel "
                        class="q-ma-sm"
                        disable
                      />
                      <!-- <q-toggle v-model="data.postpone" label="Geymd" class=" q-ma-sm" disable/> -->
                    </div>
                    <div class="text-subtitle2">
                      Þyngd: {{ data.difficulty }}
                      <q-linear-progress
                        size="14px"
                        :value="data.difficulty / 100"
                        color="red"
                        track-color="orange"
                        class="q-mt-sm"
                      />
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

    <!--OPTIONS-->
    <!-- <q-dialog v-model="memolist" >
      <q-card class="memowing">
        <q-card-section class="row items-center q-pb-none col-lg-8">
          <div class="text-h6">Veldu grein</div>
          <q-space />
          <q-btn icon="close" flat round dense v-close-popup />
        </q-card-section>
        <q-card-section>
        </q-card-section>
      </q-card>
    </q-dialog> -->

    <!--    <div class="row col redborder">-->

    <q-card
      flat
      class="q-pt-lg pagecard tpage fit"
      v-model="currentQuestion"
      v-if="currentQuestion"
    >
      <q-toolbar class="q-dark ">
        <q-toolbar-title>
          {{ totaltime }} | {{ currentQuestion.category.name }}

          {{ currPoints }} stig &nbsp;
          <!--          <span q-red>{{hintloss}}</span>&nbsp;-->

          <q-btn v-if="currentQuestion.hint.length" @click="hint">
            „Tips“ {{ currentQuestion.hint_cost }} stig
          </q-btn>

          <!--          <q-btn-->
          <!--            color="blue"-->
          <!--            @click="openUrl"-->
          <!--            label="E"-->
          <!--          />-->

          <div style="float: right;">
            spurning {{ questNum }} af {{ totalQuestions }} | {{ questTime }} |
            <q-btn @click="testFinished = true" color="negative" style="">
              Ljúka
            </q-btn>
          </div>
        </q-toolbar-title>
        <div class="col-auto">
          <!--          <q-toggle v-model="postpone" value="false" label="Sleppa " class=" q-ma-sm"/>-->
        </div>
      </q-toolbar>
      <q-card-section class="row col" style="min-height: 50vh;">
        <div class="col-md-6 q-pr-lg">
          <div class="text-h6">{{ currentQuestion.question }}</div>
          <!-- <div class="text-subtitle2">{{ currentQuestion.name }}</div>
                      <div class="text-subtitle2">{{ currentQuestion.owner.fullname }}</div> -->
          <div v-if="hinttext" class="text-white bg-orange q-pa-sm">
            {{ hinttext }}
          </div>
          <div class="qdeskr scroll q-mb-md">
            {{ currentQuestion.description }}
          </div>
        </div>
        <div class="col-md-6 col-sm-12 col-xs-12">
          <div
            v-for="opt in currentQuestion.options"
            :key="opt.id"
            class="quest-options"
          >
            <q-tooltip v-if="username === 'eberg'">
              {{ opt.correct }}
            </q-tooltip>
            <q-radio
              v-if="currentQuestion.single_selection"
              :name="opt.question_ref.toString()"
              :label="opt.answer"
              value="false"
              :val="opt.id"
              v-model="currentQuestion.answer"
              style="width: 100%; height: 100%;"
            />
            <q-checkbox
              v-if="!currentQuestion.single_selection"
              :name="opt.question_ref.toString()"
              :label="opt.answer"
              value="false"
              :val="opt.id"
              v-model="currentQuestion.answer"
            />
          </div>
        </div>
        <!--        <q-linear-progress rounded size="20px" :value="progress" color="red" class="q-mt-sm"/>-->
      </q-card-section>
      <q-separator />

      <q-card-actions class="">
        <q-checkbox
          v-model="currentQuestion.known"
          value="false"
          label="Kann vel "
          class="q-ma-sm"
          @click="currentQuestion.known = !currentQuestion.known"
        />
        <q-checkbox
          :v-model="currentQuestion.postpone"
          :value="currentQuestion.postpone"
          label="Geyma"
          class="q-ma-sm"
          @input="postPoneQuestion"
        />

        <q-btn color="orange" class="">
          Minnismiðar: {{ currentQuestion.memos.length }}
          <q-menu cover auto-close>
            <!-- v-if="currentQuestion.memos.length > 0" -->
            <q-list>
              <q-btn @click="openMemos" color="orange" style="width: 100%;">
                Minnismiðar: {{ currentQuestion.memos.length }}
              </q-btn>
              <br />
              <q-btn color="green" @click="memo = true" style="width: 100%;">
                Nýr minnismiði
              </q-btn>
            </q-list>
          </q-menu>
        </q-btn>

<!-- TODO clean submitted answer as well or just postpone  -->
        <q-btn
          @click="currentQuestion.answer = []"
          color="info"
          style="position: absolute; left: 50%;"
        >
          Hreinsa
        </q-btn>

        <q-btn
          ref="answerbutton"
          @click="onAnswerSubmit"
          color="positive"
          style="position: absolute; right: 15px;"
          size="lg"
        >
          Svara
        </q-btn>
        <q-separator />
      </q-card-actions>

      <q-card-section class="flex flex-center window-width">
        <div class="scroll">
          <q-btn-group>
            <q-btn
              v-for="quest in questions"
              :key="quest.id"
              :color="quest.color"
              :toggle-color="quest.toggle_color"
              unelevated
              :label="quest.label"
              size="lg"
              @click="setQuestion(quest.label - 1 )"
            >
              <q-tooltip
                :v-model="quest.label"
                self="bottom middle"
                anchor="top middle"
              >
                {{ quest.virtname.substring(0, 60) }}
              </q-tooltip>
            </q-btn>
          </q-btn-group>
        </div>
      </q-card-section>
    </q-card>
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
      testFinishedReadAgain: false,
      hinttext: '',
      cQ: 0,
      hintloss: '',
      currTestAnsw: [],
      questions: [],
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
      questCumulatedTime: null,
      questTime: null,
      spinnegal: true,
      username: '',
      currentQuestion: null
    }
  },
  computed: {
    isTest () {
      return this.$route.params.test || false
    }
    // currentQuestion () {
    //   return store.getters.currQest.payload
    // },
    // currentOptions () {
    //   return store.getters.currQest.payload.options
    // }
  },
  methods: {
    timers () {
      this.totaltime = date
        .formatDate(Date.now() - this.timeTotal, 'HH:mm:ss')
        .toString()
      var cqt = Date.now() - this.questStartTime
      this.questTime = date.formatDate(cqt, 'mm:ss').toString()
    },
    answerButtonState (b) {
      if (b.answered) {
        this.$refs.answerbutton.label = 'Breyta svari'
      } else {
        this.$refs.answerbutton.label = 'Svara'
      }
    },
    setQuestion (q) {
      var index = 0
      if (q > -1) {
        index = q
      } else {
        index = 0
      }

      // console.log(this.currentQuestion)

      if (this.currentQuestion) {
        console.log('T', this.clock)
        console.log('A', this.currentQuestion.time)
        console.log('TT', this.questTime)
        if (this.currentQuestion.postpone) {
          this.currentQuestion.color = 'warning'
        } else if (this.currentQuestion.answered) {
          this.currentQuestion.color = 'positive'
        } else {
          this.currentQuestion.color = 'info'
        }
        // this.answerButtonState(this.currentQuestion)
        // this.rowButtonState(this.currentQuestion)
      }

      // console.log('B', this.currentQuestion)

      this.hinttext = ''
      this.editingIndex = index
      // this.question = JSON.parse(JSON.stringify(this.questions[index]))
      // store.commit({ type: 'setQuestion', payload: this.question })
      this.currentQuestion = this.questions[index]
      this.currPoints = this.currentQuestion.points
      this.questNum = index + 1
      // console.log('C', this.currentQuestion)

      this.currentQuestion.color = 'blue-grey-4'
      // this.rowButtonState(this.currentQuestion)
      // console.log('D', this.currentQuestion)

      this.timeTotal = store.getters.getTimeTotal
    },
    // setAnswerChecked (e) {
    //   // e.preventDefault()
    //   if (this.currentQuestion.id !== this.cQ) {
    //     this.cQ = this.currentQuestion.id
    //     this.currTestAnsw = []
    //   }
    // },
    postPoneQuestion (e, go) {
      if (!this.currentQuestion.postpone) {
        this.currentQuestion.color = 'warning'
        this.currentQuestion.answered = true
        this.currentQuestion.postpone = true
      } else {
        this.currentQuestion.color = 'info'
        this.currentQuestion.answered = false
        this.currentQuestion.postpone = false
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
      this.memo = false
      this.currentQuestion.memos.push(formdata)
    },
    onAnswerSubmit (e) {
      if (this.currentQuestion.answer < 1) {
        if (
          confirm(
            'Hey ætlar þú ekki að svara?\n OK merkir spurninguna til að hún gleymist ekki.'
          )
        ) {
          this.currentQuestion.color = 'warning'
          this.currentQuestion.answered = true
          this.currentQuestion.postpone = true
        }
      } else {
        this.currentQuestion.answered = true
        this.currentQuestion.postpone = false
        this.currentQuestion.color = 'positive'
      }

      const formdata = {
        options_ids: this.currentQuestion.answer.toString(),
        curr_question: parseInt(this.currentQuestion.id),
        test_practice: parseInt(this.myJson.id),
        points: parseInt(this.currPoints),
        known: this.currentQuestion.known,
        postpone: this.currentQuestion.postpone
      }
      // console.log(formdata)

      getAPI({
        url: '/api/answer/',
        method: 'post',
        data: formdata,
        headers: { Authorization: `Bearer ${access}` }
      }) // .catch((error) => console.log('Error', error.message))

      // this.questions[this.questNum - 1].answer = this.currTestAnsw

      // this.questions[this.questNum - 1]['toggle-color'] = 'info'
      this.known = false

      var answers = 0
      var i
      for (i = 0; i < this.totalQuestions; i++) {
        if (this.questions[i].answered) {
          answers++
        }
      }

      if (answers === this.totalQuestions) {
        this.testFinished = true
      } else {
        var ii
        for (ii = 0; ii < this.totalQuestions; ii++) {
          console.log(ii, this.questions[ii].id, this.currentQuestion.id, this.questions[ii].id === this.currentQuestion.id)
          if (this.questions[ii].id === this.currentQuestion.id) {
            this.setQuestion(ii + 1)
            ii = this.totalQuestions
          }
        }
      }

      // var ii
      // for (ii = 0; ii < this.totalQuestions; ii++) {
      //   if (!this.questions[ii].answered) {
      //     this.setQuestion(ii + 1)
      //     ii = this.totalQuestions
      //   }
      // }
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
      this.$router
        .push({ path: '/review/' + this.myJson.id + '/' })
        .catch(err => {
          console.log(err.message)
        })
    },
    keyprocess (e) {
      console.log(e)
      if (e.key === 'Enter') {
        this.onAnswerSubmit()
      }
    },
    userok () {
      return this.username === 'eberg'
    }
  },
  beforeMount () {
    this.username = store.getters.getUserName
    getAPI({
      url: '/api/questionnaiere/?user=' + this.username,
      headers: { Authorization: `Bearer ${access}` }
    })
      .then(response => {
        this.myJson = JSON.parse(JSON.stringify(response.data[0]))
        this.questions = JSON.parse(
          JSON.stringify(response.data[0].question_collection)
        )
        this.totalQuestions = this.questions.length
        var i
        for (i = 0; i < this.totalQuestions; i++) {
          // console.log(this.questions[i].name)
          this.questions[i].label = i + 1
        }

        this.startTime = Date.now()
        this.$store.dispatch('setTotalTime', Date.now())
        this.setQuestion(0)
      })
      .catch(error => console.log('Error', error.message))
  },
  updated () {},
  created () {
    this.clock = setInterval(this.timers, 1000)
    window.addEventListener('keyup', this.keyprocess)
  },
  beforeDestroy () {
    window.removeEventListener('keyup', this.keyprocess)
  }
}
</script>

<style scoped lang="sass">

.memowing
  width: 400px

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
  bottom: 50px
  margin: 0px
  background-color: $primary
  //min-height: 40px
  overflow: scroll
  text-align: center

.qdeskr
  max-height: 250px
  overflow: scroll
</style>
