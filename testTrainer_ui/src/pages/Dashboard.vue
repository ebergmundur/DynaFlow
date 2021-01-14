<template>
  <q-page class="flex flex-center">
    <q-card flat
            class="pagecard"
    >
      <q-toolbar class="q-dark">
        <q-toolbar-title>
          Mælaborð - meðaltal {{ averagescore }}
        </q-toolbar-title>
      </q-toolbar>

      <q-card-section class="q-pa-none echarts">
        <IEcharts :option="barChartOption" :resizable="true"/>
      </q-card-section>
      <q-card-actions>
        <q-btn @click="onAnswerSubmit" color="positive" label="Allt"/>
        <q-btn @click="onAnswerSubmit" color="positive" label="Æfingar"/>
        <q-btn @click="onAnswerSubmit" color="positive" label="Próf"/>
      </q-card-actions>
    </q-card>
  </q-page>
</template>

<script>
import { date } from 'quasar'
import store from 'src/store'
import IEcharts from 'vue-echarts-v3/src/full.js'
import { getAPI } from 'src/api/axios-base'
// import axios from 'axios'
const access = store.getters.token

export default {
  name: 'Dashboard',
  data () {
    return {
      exams: '',
      access: null,
      username: null,
      averagescore: 0,
      barChartOption: {
        width: '70%',
        grid: {
          bottom: '15%'
        },
        legend: {
          type: 'scroll',
          orient: 'vertical',
          right: 0
        },
        tooltip: {},
        dataset: {
          dimensions: ['prof', '2015', '2016', '2017'],
          source: [
            { prof: 'Próf', 2015: 43.3, 2016: 85.8, 2017: 93.7 }
          ]
        },
        xAxis: {
          // data: ['2015', '2016', '2017'],
          type: 'category',
          axisLabel: {
            rotate: 45
          }

        },
        yAxis: {
          // data: [43.3, 85.8, 93.7]
        },
        // Declare several bar series, each will be mapped
        // to a column of dataset.source by default.
        series: []
      }
    }
  },
  components: {
    IEcharts
  },
  methods: {
    formatDate (d) {
      return date.formatDate(d, 'YYYY-MM-DD HH:mm')
    },
    onAnswerSubmit () {

    }
  },
  beforeCreate () {
    this.access = store.getters.token // attempt to obtain new access token by running 'refreshToken' action
    this.username = store.getters.getUserInfo.username
  },
  created () {
  },
  mounted () {
    getAPI({
      url: '/api/dashboarddata/',
      method: 'post',
      data: {
        username: store.getters.getUserInfo.username
      },
      headers: { Authorization: `Bearer ${access}` }
    }
    )
      .then(response => {
        this.exams = JSON.parse(JSON.stringify(response.data))

        this.barChartOption.dataset.source = [{ prof: 'Próf' }]
        this.barChartOption.dataset.dimensions = ['prof']

        var avrgscore = 0
        var i = 0
        for (i = 0; i < this.exams.length; i++) {
          var practice
          if (this.exams[i].practice) {
            practice = 'Æ'
          } else {
            practice = 'P'
          }
          const kkey = this.exams[i].name + ' ' + practice + ' ' + this.exams[i].id
          const testscore = parseInt(this.exams[i].final_results * 10000) / 1000
          avrgscore = avrgscore + testscore

          this.barChartOption.dataset.dimensions.push(kkey)
          this.barChartOption.dataset.source[0][kkey.toString()] = testscore
          this.barChartOption.series.push({ type: 'bar' })
        }

        this.averagescore = parseInt((avrgscore / this.exams.length) * 100) / 100

        // this.barChartOption.series.push({ type: 'line' })
        // console.log('this.barChartOption')
        // console.log(this.barChartOption.dataset.source[0])
      })
      .catch(error => console.log('Error', error.message))
  }
}
</script>

<style scoped>
.echarts {
  width: 100%;
  height: 400px;
}
</style>
<!--Categories-->

<!--Results-->
<!--Time axis-->
