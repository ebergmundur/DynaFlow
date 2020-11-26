<template>
  <div class="q-pa-md row items-start q-gutter-md">

    <q-dialog v-model="memo">
      <q-card>
        <q-toolbar>
          <q-avatar>
            <img src="../assets/enam-logo.svg">
          </q-avatar>

          <q-toolbar-title><span class="text-weight-bold">E-nám</span> minnispunktar</q-toolbar-title>

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
          <div class="text-h6">Minnispunktar</div>
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
                      {{ formatDate(data.created_date) }}

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

    <!--    <q-dialog v-model="calendar" >-->
    <!--      <q-card>-->
    <!--        <q-card-section>-->
    <!--            -->
    <!--        </q-card-section>-->
    <!--      </q-card>-->
    <!--    </q-dialog>-->

    <!--    <q-card class="my-card bg-secondary text-white">-->
    <!--      <q-card-section>-->
    <!--        <div class="text-h6">Our Changing Planet</div>-->
    <!--        <div class="text-subtitle2">by John Doe</div>-->
    <!--      </q-card-section>-->

    <!--      <q-card-section>-->
    <!--        {{ lorem }}-->
    <!--      </q-card-section>-->

    <!--      <q-separator dark/>-->

    <!--      <q-card-actions>-->
    <!--        <q-btn flat>Action 1</q-btn>-->
    <!--        <q-btn flat>Action 2</q-btn>-->
    <!--      </q-card-actions>-->
    <!--    </q-card>-->

    <!--    <q-card class="my-card">-->
    <!--      <q-card-section>-->
    <!--        <div class="text-h6">Our Changing Planet</div>-->
    <!--        <div class="text-subtitle2">by John Doe</div>-->
    <!--      </q-card-section>-->

    <!--      <q-separator/>-->

    <!--      <q-card-actions vertical>-->
    <!--        <q-btn flat>Action 1</q-btn>-->
    <!--        <q-btn flat>Action 2</q-btn>-->
    <!--      </q-card-actions>-->
    <!--    </q-card>-->

    <!--    <q-card class="my-card bg-purple text-white">-->
    <!--      <q-card-section>-->
    <!--        <div class="text-h6">Our Changing Planet</div>-->
    <!--        <div class="text-subtitle2">by John Doe</div>-->
    <!--      </q-card-section>-->

    <!--      <q-card-actions>-->
    <!--        <q-btn flat>Action 1</q-btn>-->
    <!--        <q-btn flat>Action 2</q-btn>-->
    <!--      </q-card-actions>-->
    <!--    </q-card>-->

    <q-card bordered

            class="my-card bg-grey-1 absolute-center col-xs-10 col-sm-10 col-md-10 col-xl-6 col-lg-6"
            v-model='currentQuestion'
            v-if="currentQuestion"
    >
      <!--            style="max-height: 80vh; width: 40%;"-->
      <q-card-section>
        <div class="row items-center no-wrap">
          <div class="col">
            <div class="text-h6">{{ currentQuestion.question }}</div>
            <div class="text-subtitle2">{{ currentQuestion.name }}</div>
            <div class="text-subtitle2">{{ currentQuestion.owner.fullname }}</div>
            <div class="text-h6">{{ hinttext }}</div>
          </div>

          <div class="col-auto">
            <q-btn color="grey-7" round flat icon="more_vert">
              <q-menu cover auto-close>
                <q-list>
                  <!--                  <q-item clickable>-->
                  <!--                    <q-item-section>Endurskoða síðar</q-item-section>-->
                  <!--                  </q-item>-->
                  <q-btn
                    v-if="currentQuestion.memos.length > 0"
                    @click="openMemos"
                    color="orange"
                    style="width: 100%"
                  >
                    Minnispunktar {{ currentQuestion.memos.length }}
                  </q-btn>
                  <br>
                  <q-btn
                    color="green"
                    @click="memo = true"
                    style="width: 100%"
                  >
                    Nýir minnispunktar
                  </q-btn>
                </q-list>
              </q-menu>
            </q-btn>
          </div>
        </div>
      </q-card-section>
      <q-card-section>

        <!--        <q-option-group-->
        <!--      v-model="currentOptions"-->
        <!--      :options="currentOptions"-->
        <!--      color="primary"-->
        <!--    />-->
        <!--        v-for="(data, index) in currentOptions" :key="index"-->
        <!--                  @input="setAnswerChecked"-->
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
            v-model="currTestQuest"
            @input="setAnswerChecked"
          />
          <q-checkbox
            v-if="!currentQuestion.single_selection"
            :name="opt.question_ref.toString()"
            :label="opt.answer"
            value="false"
            :val="opt.id"
            v-model="currTestQuest"
            @input="setAnswerChecked"
          />
        </div>

        <!--        <div class="q-pa-lg">-->
        <!--          <q-option-group-->
        <!--            v-if="!currentQuestion.single_selection"-->
        <!--            v-model="currTestQuest"-->
        <!--            :options="currentOptions"-->
        <!--            type="checkbox"-->
        <!--            color="primary"-->
        <!--            @input="setAnswerChecked"-->
        <!--          />-->
        <!--          <q-option-group-->
        <!--            v-if="currentQuestion.single_selection"-->
        <!--            v-model="currTestQuest"-->
        <!--            :options="currentOptions"-->
        <!--            type="radio"-->
        <!--            color="primary"-->
        <!--            @input="setAnswerChecked"-->
        <!--          />-->
        <!--        </div>-->
        <!--        {{ this.progress }} - {{ this.time_step }}  {{ currentQuestion.time_allowed }} -->

        <q-linear-progress rounded size="20px" :value="progress" color="red" class="q-mt-sm"/>
      </q-card-section>
      <q-separator/>
      <q-card-section>
        <!--        <p>{{ currentQuestion.memos.created_date }}</p>-->
        <!--        <p>{{ currentQuestion.memos.memo }}</p>-->
        <!--        <q-toggle v-model="currentQuestion.memos.known" label="Kann þetta"/>-->
        <!--        <p>{{ currentQuestion.memos.review_date }}</p>-->

        <!--      {{ currentQuestion.memos }}-->
      </q-card-section>
      <q-card-actions>
        <div class="text-h5">
          {{ currentQuestion.points }} stig &nbsp;
          <!--          <span q-red>{{hintloss}}</span>&nbsp;-->
        </div>
        <q-btn
          v-if="currentQuestion.hint.length"
          @click="hint">„Tips“ kostar {{ currentQuestion.hint_cost }} stig
        </q-btn>

        <q-btn
          color="blue"
          @click="openUrl"
        >
          Breyta í Admin
        </q-btn>
        <q-btn
          @click="onAnswerSubmit"
          color="green"
        >
          Svara
        </q-btn>
      </q-card-actions>
    </q-card>
  </div>
</template>

<script>
import store from '../router/store'
import { date } from 'quasar'
import axios from 'axios'
// import { mapMutations } from 'vuex'

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
    setAnswerChecked (e) {
      if (this.currentQuestion.id !== this.cQ) {
        this.cQ = this.currentQuestion.id
        this.currTestQuest = []
        this.progress = 0.001
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
    openUrl () {
      window.open('https://testtrainer.benda.is/admin/questions/question/' + this.currentQuestion.id, '_blank')
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
    timerCount () {
      this.time_allowed = this.currentQuestion.time_allowed // 10 // til að stytta
      this.time_step = 1 / this.time_allowed
      this.time_taken = this.progress * this.time_allowed
      if (this.progress > 1.0) {
        // alert('Tíminn búinn')
        this.progress = 0.001
      } else {
        this.progress = this.progress + this.time_step
      }
    }
  },
  mounted () {
    this.interval = setInterval(() => {
      this.timerCount()
    }, 1000)
  },
  updated () {
    this.setAnswerChecked()
    // console.log('At this point, Virtual DOM has re-rendered and patched.')
    // Fired every second, should always be true
    // console.log(+this.$refs['example-element'].textContent === this.counter)
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
