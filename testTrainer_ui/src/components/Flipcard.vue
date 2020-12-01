<template>
  <div class="q-pa-md row items-start q-gutter-md">
    <q-card bordered
            class="my-card bg-grey-1 absolute-center col-xs-12 col-xs-12 col-md-6 col-xl-4 col-lg-4"
            v-model='currentQuestion'
            v-if="currentQuestion"
    >
      <!--            style="max-height: 80vh; width: 40%;"-->
      <q-toolbar class="q-dark" style="background-color: #616161;">
        <q-toolbar-title>
          Flettikort
        </q-toolbar-title>
      </q-toolbar>
      <q-card-section>
        <div class="row items-center no-wrap">
          <div class="col">
            <div class="text-h6">{{ currentQuestion.question }}</div>
            <div
              v-if="hinttext"
              class="text-white bg-orange q-pa-xs ">{{ hinttext }}
            </div>
          </div>

        </div>
      </q-card-section>

      <q-card-section class="">
        <div class="col-12 q-px-xs scroll">
          {{ currentQuestion.description }}
        </div>
        <q-slide-transition>
          <div class="col-12" v-show="visible">
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
        </q-slide-transition>
      </q-card-section>
      <q-separator/>
      <q-card-actions>
        <!--        <div class="text-h5">-->
        <!--          {{ currPoints }} stig &nbsp;-->
        <!--        </div>-->
        <!--        <q-btn-->
        <!--          v-if="currentQuestion.hint.length"-->
        <!--          @click="hint">„Tips“ {{ currentQuestion.hint_cost }} stig-->
        <!--        </q-btn>-->

        <q-toggle v-model="visible" label="Sjá spurningar" class="q-mb-md"/>
        <!--        <q-btn-->
        <!--          @click="onAnswerSubmit"-->
        <!--          color="green"-->
        <!--        >-->
        <!--          Svara-->
        <!--        </q-btn>-->

      </q-card-actions>
    </q-card>
  </div>
</template>

<script>
import store from '../router/store'
import { date } from 'quasar'
import axios from 'axios'

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
      this.question = JSON.parse(JSON.stringify(this.myJson.question_collection[index]))
      store.commit({ type: 'setQuestion', payload: this.question })
      // store.commit({ type: 'setTestQuestion', payload: [] })
      // Question.setAnswerChecked()
      this.currPoints = this.question.points
      this.questNum = index + 1
    },
    setAnswerChecked (e) {
      console.log(e)
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
      axios({
        method: 'post',
        url: 'http://einars-macbook-pro.local:8000/api/memos/',
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
      console.log(formdata)
      axios({
        method: 'post',
        url: 'http://einars-macbook-pro.local:8000/api/answer/',
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
    }
  },
  mounted () {
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

</style>
