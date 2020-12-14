<template>
  <q-page class="flex flex-center q-pa-xs ">
  <div class="q-pa-md row items-start q-gutter-md">
    <q-card bordered
            class="my-card bg-grey-1 absolute-center col-xs-10 col-sm-10 col-md-10 col-xl-6 col-lg-6">
      <q-card-section>
        <div class="text-h4">Búa til æfingapróf</div>
        <q-separator/>
        <q-input
          v-model="examname"
          placeholder="Heiti prófs, ef ekkert er slegið inn fær prófið dagsetningu sem heiti"
        label="Nefna próf"
        >

        </q-input>
        <div class="text-h6 q-mt-md">Flokkar</div>
<!--        cats_count: {{ cats_count }},<br>-->
<!--{{question_count}}-->
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

        <!--        <q-checkbox-->
        <!--          v-for="(data, index) in myJson"-->
        <!--          :key="index"-->
        <!--          :label="data.name + ' ' + data.q_count"-->
        <!--          value="false"-->
        <!--          :val="data.id"-->
        <!--          v-model="cats"-->
        <!--          @input="setCategoryChecked"-->
        <!--          style="border: 1px solid red; width: 100%; float: none;"-->
        <!--        />-->
        <!--            {{ data.questions }}-->

        <div class="text-h6" >Fjöldi spurninga í æfingu {{ question_count }}</div>
<!--        <q-slider-->
<!--          v-model="question_count"-->
<!--          :min="0"-->
<!--          :max="150"-->
<!--          label-->
<!--        />-->
        <div >
<!--        <q-checkbox-->
<!--            label=" Nota tímamörk spurninga"-->
<!--            v-model="given_time_limit"-->
<!--          /> <span>: {{time_limit}} mínútur</span>-->
          Nota tímamörk spurninga  {{time_limit}} mín.
          eða setja eigin tíma: {{manualTime}} mín.
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
  </div>
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
        examname: this.examname
      }
      // console.log(formdata)
      getAPI({
        url: '/api/questionnaiere/',
        method: 'post',
        headers: { Authorization: `Bearer ${access}` },
        data: formdata
      })
    },
    manualSet () {
      this.given_time_limit = false
    },
    calc_question_count () {
      var i = 0
      var t = 0
      for (i = 0; i < this.cats_count.length; i++) {
        if (this.cats_count[i] > 0) { t = t + (this.cats_count[i] * 1) }
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
