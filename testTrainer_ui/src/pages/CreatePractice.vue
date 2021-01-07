<template>
  <q-page class="flex flex-center">
    <q-card flat
            class="pagecard"
    >

      <q-toolbar class="q-dark">
        <q-toolbar-title>
          Búa til æfingapróf
        </q-toolbar-title>
      </q-toolbar>
      <q-card-section>

        <div class="text-h6 q-mt-md">Flokkar</div>
        <q-field
          v-for="(data, index) in myJson"
          :key="index"
          :label="data.name + ' ' + cats_count[data.id] + ' af ' + data.q_count"
          stack-label
          v-model="cats"
        >
          <q-slider
            v-if="data.q_count"
            v-model="cats_count[data.id]"
            :min="0"
            color="green"
            :max="data.q_count"
            @change="calc_question_count"
          />
        </q-field>

        <div class="text-h6">Fjöldi spurninga í æfingu {{ question_count }}</div>

        <div>
          Nota tímamörk spurninga {{ time_limit }} mín.
          eða setja eigin tíma: {{ manualTime }} mín.
          <q-slider
            v-model="manualTime"
            :min="0"
            :max="180"
            :step="5"
            label
          />
        </div>
        <div>
          <q-checkbox
            label="Sleppa „kann vel“"
            value="false"
            v-model="omit_known"
          />
          <q-checkbox
            label="Aðeins spurningar sem ég hef svarað rangt"
            value="false"
            v-model="only_failed"
          />
        </div>
      </q-card-section>
      <!--      {{groups}} // {{cats}}-->
      <q-separator/>
      <q-card-actions>
        <q-btn
          @click="onPracticeSubmit"
          color="green"
        >
          Vista
        </q-btn>
      </q-card-actions>
    </q-card>
  </q-page>
</template>

<script>
// import axios from 'axios'
import store from 'src/store'
import { getAPI } from 'src/api/axios-base'
// import { date } from 'quasar'
const access = store.getters.token
export default {

  data () {
    return {
      myJson: null,
      name: 'CreatePractice',
      groups: [],
      cats_count: [],
      cats: [],
      question_count: 0,
      given_time_limit: true,
      time_limit: 0,
      manualTime: 0,
      omit_known: false,
      only_failed: false,
      examname: '',
      access: store.getters.token
    }
  },
  computed: {
    // question_count () {
    //   var i = 0
    //   var t = 0
    //   for (i = 0; i < this.cats_count.length; i++) {
    //     if (this.cats_count[i] > 0) { t = t + (this.cats_count[i] * 1) }
    //   }
    //   return t
    // }
  },
  methods: {
    onPracticeSubmit () {
      const formdata = {
        question_collection_str: this.cats_count.toString(),
        question_collection: this.cats_count,
        // time_taken: parseInt(this.time_taken),
        // options_ids: this.currTestQuest.toString(),
        time_allowed: this.manualTime,
        timed: this.given_time_limit,
        only_failed: this.only_failed,
        omit_known: this.omit_known,
        examname: this.examname,
        user: store.getters.getUserName
      }
      // console.log(formdata)
      getAPI({
        url: '/api/questionnaiere/',
        method: 'post',
        headers: { Authorization: `Bearer ${access}` },
        data: formdata
      })
        .then(() => {
          this.wrongCred = false
          this.$router.push({ name: 'testpractice' })
        })
        .catch(err => {
          console.log(err)
          this.wrongCred = true // if the credentials were wrong set wrongCred to true
        })
    },
    manualSet () {
      this.given_time_limit = false
    },
    calc_question_count () {
      var i = 0
      var t = 0
      for (i = 0; i < this.cats_count.length; i++) {
        if (this.cats_count[i] > 0) {
          t = t + (this.cats_count[i] * 1)
        }
      }
      this.question_count = t
      this.count_time_limit()
    },
    setGroupChecked () {
      return 0
    },
    setCategoryChecked () {
      return 0
    },
    set_slider () {
      var i = 0
      var qc = 0
      for (i = 0; i < this.myJson.length; i++) {
        var cid = this.myJson[i]
        qc = qc + Math.round(cid.q_count / 2)
        // this.cats_count[cid.id] = Math.round(cid.q_count / 2)
        this.cats_count[cid.id] = 0
      }
      // this.question_count = qc
    },
    count_time_limit () {
      this.time_limit = Math.round(this.question_count)
      this.manualTime = this.time_limit
    }
  },
  beforeMount () {
    getAPI({
      url: '/api/category/',
      method: 'get',
      headers: { Authorization: `Bearer ${access}` }
    })
      .then(response => {
        // console.log(response)
        this.myJson = JSON.parse(JSON.stringify(response.data))
        console.log(this.myJson)
        this.set_slider()
        this.count_time_limit()
      })
      .catch(error => console.log('Error', error.message))
    // this.myJson = JSON.parse(JSON.stringify(json))
  }
}
</script>

<style scoped>

</style>
