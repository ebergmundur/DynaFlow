<template>
  <q-page class="flex q-pa-none self-start column">
    <q-card class="q-pt-lg">
<!-- TODO: Fylla upp í svæðpi -->
      <!-- <q-toolbar class="q-dark q-mt-md">
        <q-toolbar-title>
          Búa til æfingapróf
        </q-toolbar-title>
      </q-toolbar> -->
      <q-card-section>

        <div class="text-h4 q-mt-md">Veldu fjölda spurninga</div>
        <div class="q-ma-lg">
        <q-input v-model="tot_count" type="number" label="" @input="calc_total_count" class="text-h4" style="height: 80px; margin-top: -40px;"/>
         <!-- <q-field
          :label="tot_count.toString()"
          v-model="cats"
        > -->
          <q-slider
            v-model="tot_count"
            :min='0'
            color="blue"
            label
            :max='100'
            :step='5'
            markers
            @change="calc_total_count"
          />
          <!-- </q-field> -->
          <q-checkbox
            v-for="(data, index) in myJson"
            :key="index"
            :value="data.id"
            :label="data.name"
            v-model="cats_count[data.id].use"
            @input="calc_total_count"
        />
        </div>
        <div class="q-ma-lg">
        <q-field
          v-for="(data, index) in myJson"
          :key="index"
          :label="data.name + ' ' + cats_count[data.id].num + ' af ' + data.q_count"
          v-model="cats"
        >
          <q-slider
            v-if="data.q_count"
            v-model="cats_count[data.id].num"
            :min="0"
            color="green"
            label
            markers
            :max="data.q_count"
            @change="calc_question_count"
          />
        </q-field>
        </div>

        <div class="text-h6 q-mt-md">Fjöldi spurninga í æfingu {{ question_count }}</div>
        <!-- <div>
          Nota tímamörk spurninga {{ time_limit }} mín.
          eða setja eigin tíma: {{ manualTime }} mín.
          <q-slider
            v-model="manualTime"
            :min="0"
            :max="180"
            :step="5"
            label
          />
        </div> -->
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
      <q-card-section style="width: 100%; min-height: 100px;" class="">

        <q-btn
          @click="onPracticeSubmit"
          color="green"
          style="position: absolute; right: 45px; top: 15px;"
        >
          Vista
        </q-btn>
      </q-card-section>
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
      tot_count: '0',
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
      console.log(formdata)
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
    calc_total_count (e) {
      var i = 0
      var ii = 0
      var tc = 0

      for (i = 0; i < this.cats_count.length; i++) {
        if (typeof this.cats_count[i] !== 'undefined') {
          if (this.cats_count[i].use) {
            tc++
          }
        }
      }
      if (tc === 0) {
        console.log('tc test')
        console.log(tc)
        tc = 1
      }
      // console.log('tc')
      // console.log(tc)

      var qPerCat = Math.round(Number(this.tot_count) / tc)

      // console.log('qPerCat')
      // console.log(qPerCat)
      // console.log('catta count')
      for (ii = 0; ii < this.cats_count.length; ii++) {
        if (typeof this.cats_count[ii] !== 'undefined') {
          if (this.cats_count[ii].use) {
            this.cats_count[ii].num = qPerCat
            // console.log(this.cats_count[ii])
          } else {
            this.cats_count[ii].num = 0
          }
        }
      }
      this.calc_question_count()
    },
    calc_question_count () {
      var i = 0
      var t = 0
      for (i = 0; i < this.cats_count.length; i++) {
        if (typeof this.cats_count[i] !== 'undefined') {
          if (this.cats_count[i].use === true) {
            t = t + (this.cats_count[i].num)
          }
        }
      }
      this.question_count = t
      this.count_time_limit()
      console.log(this.cats_count)
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
        // this.cats_count[cid.id][0] = true
        this.cats_count[cid.id] = { id: cid.id, num: 0, use: true }
      }
      // this.question_count = qc
      console.log(this.cats_count)
    },
    count_time_limit () {
      this.time_limit = Math.round(this.question_count)
      this.manualTime = this.time_limit
    },
    keyprocess (e) {
      // e.preventDefault()
      console.log(e)

      if (e.key === 'Enter') {
        // console.log('ENTER')
        this.onPracticeSubmit()
      }
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
        // console.log(this.myJson)
        this.set_slider()
        this.count_time_limit()
      })
      .catch(error => console.log('Error', error.message))
    // this.myJson = JSON.parse(JSON.stringify(json))
  },
  mounted () {
    window.addEventListener('keyup', this.keyprocess)
  },
  beforeDestroy () {
    window.removeEventListener('keyup', this.keyprocess)
  }
}
</script>

<style scoped>

</style>
