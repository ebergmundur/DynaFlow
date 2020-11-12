<template>
  <div class="q-pa-md row items-start q-gutter-md">

    <q-dialog v-model="memo">
      <q-card>
        <q-toolbar>
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo/svg/quasar-logo.svg">
          </q-avatar>

          <q-toolbar-title><span class="text-weight-bold">E-nám</span> minnispunktar</q-toolbar-title>

          <q-btn flat round dense icon="close" v-close-popup/>
        </q-toolbar>

        <q-card-section>

          <h5>{{ currentQuestion.name }}</h5>
          <q-form
            @submit="onMemoSubmit"
            @reset="onMemoReset"
            class="q-gutter-md"
          >
            <div class="q-pa-md">
              <q-badge color="secondary ">
                Þyngd: {{ difficulty / 10 }}
              </q-badge>
              <q-slider
                v-model="difficulty"
                :step="10"
              />
            </div>

            <div class="q-pa-md">
              <q-input
                v-model="memotext"
                filled
                type="textarea"
              />
            </div>
             <q-toggle v-model="accept" label="I accept the license and terms" />
            <div>
              <q-btn label="Submit" type="submit" color="primary"/>
              <q-btn label="Reset" type="reset" color="primary" flat class="q-ml-sm"/>
            </div>
          </q-form>
        </q-card-section>
      </q-card>
    </q-dialog>

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

    <q-card flat bordered class="my-card bg-grey-1" v-model='currentQuestion' v-if="currentQuestion">
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
                  <q-item clickable>
                    <q-item-section>Endurskoða síðar</q-item-section>
                  </q-item>
                  <q-item clickable>
                    <q-item-section>Kann, má sleppa næst</q-item-section>
                  </q-item>
                  <q-item clickable>
                    <q-item-section @click="memo = true"> Minnispunktar</q-item-section>
                  </q-item>
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
        <div class="q-pa-lg">
          {{ currentQuestion.single_selection }}
          <q-option-group
            v-if="!currentQuestion.single_selection"
            v-model="currTestQuest"
            :options="currentOptions"
            type="checkbox"
            color="primary"
            @input="setAnswerChecked"
          />
          <q-option-group
            v-if="currentQuestion.single_selection"
            v-model="currTestQuest"
            :options="currentOptions"
            type="radio"
            color="primary"
            @input="setAnswerChecked"
          />
        </div>

      </q-card-section>
      <q-separator/>

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
          @click="openUrl"
          color="blue"
        >
          Breyta í Admin
        </q-btn>
        <q-btn
          @click="openUrl"
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
// import { mapMutations } from 'vuex'
export default {
  name: 'Question',
  computed: {
    currentQuestion () {
      return store.getters.currQest.payload
    },
    // currTestQuest () {
    //   return store.getters.currTestQest
    // },
    currentOptions () {
      return store.getters.currQest.payload.options
    }
    // message: {
    //   get () {
    //     return this.$store.state.obj.message
    //   },
    //   set (value) {
    //     this.$store.commit('updateMessage', value)
    //   }
    // }
  },
  // computed: mapState([
  //   'currQest'
  // ]),
  // methods: mapMutations([
  //   'setOptinsChecked'
  // ]),
  methods: {
    setAnswerChecked (e) {
      // // store.getters.setSelected(e)
      // console.log('hér erum við')
      // console.log(this.currentQuestion.id + ' ' + this.cQ)
      // if (this.currentQuestion.single_selection) {
      //   console.log('RADIO')
      //   if (this.currentQuestion.id === this.cQ) {
      //     console.log('R BREYTI EKKI')
      //   } else {
      //     console.log('R BREYTI')
      //     this.cQ = this.currentQuestion.id
      //   }
      // } else {
      //   console.log('CHECK')
      //   if (this.currentQuestion.id === this.cQ) {
      //     console.log('C BREYTI EKKI')
      //   } else {
      //     console.log('C BREYTI')
      //     // this.test = []
      //     this.cQ = this.currentQuestion.id
      //   }
      // }
      console.log(this.currTestQuest)
    },
    onMemoSubmit () {
      if (this.accept !== true) {
        this.$q.notify({
          color: 'red-5',
          textColor: 'white',
          icon: 'warning',
          message: 'You need to accept the license and terms first'
        })
      } else {
        this.$q.notify({
          color: 'green-4',
          textColor: 'white',
          icon: 'cloud_done',
          message: 'Submitted'
        })
      }
    },
    onMemoReset () {
      this.memotext = ''
      this.difficulty = 50
      this.accept = false
    },
    hint () {
      this.hinttext = this.currentQuestion.hint
      this.hintloss = this.currentQuestion.points - this.currentQuestion.hint_cost
    },
    openUrl () {
      window.open('https://testtrainer.benda.is/admin/questions/question/' + this.currentQuestion.id, '_blank')
    }
  },
  data () {
    return {
      // currentOptions: this.currentQuestion.options
      hinttext: '',
      cQ: 0,
      hintloss: '',
      currTestQuest: [],
      memo: false,
      memotext: '',
      difficulty: 50,
      accept: false

    }
  }
}
// TODO Hreinsa currTestQuest á milli spurninga
</script>

<style scoped>

</style>
