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
    <!-- <br/>
    <div style="float: none; overflow: scroll;" >
      <pre>
      {{this.barChartOption.series}}
      {{this.barChartOption.xAxis}}
      </pre>
    </div> -->
  </q-page>
</template>

<script>
import { date } from 'quasar'
import store from 'src/store'
import IEcharts from 'vue-echarts-v3/src/full.js'
import { getAPI } from 'src/api/axios-base'
// import axios from 'axios'
const access = store.getters.token

var emphasisStyle = {
  itemStyle: {
    borderWidth: 4,
    shadowBlur: 10,
    shadowOffsetX: 0,
    shadowOffsetY: 0,
    shadowColor: 'rgba(0,0,0,0.5)'
  }
}

export default {
  name: 'Dashboard',
  data () {
    return {
      exams: '',
      xAxisData: [],
      xTests: [],
      access: null,
      username: null,
      averagescore: 0,
      barChartOption: {
        width: '70%',
        grid: {
          bottom: '120px'
        },
        toolbox: {
          feature: {
            magicType: {
              type: ['stack', 'tiled']
            },
            dataView: {}
          }
        },
        legend: {
          // data: ['Fag', 'Líffræði', 'Efnafræði', 'Eðlisfræði', 'Stærðfræði', 'Almenn þekking'],
          type: 'scroll',
          orient: 'horisontal',
          right: 10,
          top: 30
        },
        tooltip: {
          trigger: 'item',
          axisPointer: {
            type: 'line'
          },
          formatter: function (params) {
            var tar
            if (params.value < 0) {
              tar = params[1]
            } else {
              tar = params
            }
            return tar.name + '<br/>' + tar.seriesName + ' : ' + tar.value
          }
        },
        xAxis: {
          data: [],
          type: 'category',
          name: 'Próf',
          axisLine: { onZero: true },
          splitLine: { show: false },
          splitArea: { show: false },
          axisLabel: {
            show: true,
            rotate: 60
          }
        },
        yAxis: {
          name: '%',
          inverse: false,
          splitArea: { show: true }
        },
        // visualMap: {
        //   type: 'piecewise',
        //   dimension: 2,
        //   text: ['', ''],
        //   inverse: true,
        //   itemHeight: 20,
        //   calculable: true,
        //   min: 100,
        //   max: -100,
        //   top: 60,
        //   left: 10,
        //   inRange: {
        //     colorLightness: [0.4, 0.8]
        //   },
        //   outOfRange: {
        //     color: '#bbb'
        //   },
        //   controller: {
        //     inRange: {
        //       color: '#2f4554'
        //     }
        //   }
        // },
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
    })
      .then(response => {
        this.exams = JSON.parse(JSON.stringify(response.data))

        var avrgscore = 0
        var i = 0
        var iii = 0

        this.xTests = [[], [], [], [], []]
        const catNames = ['Líffræði', 'Efnafræði', 'Eðlisfræði', 'Stærðfræði', 'Almenn þekking']

        for (i = 0; i < this.exams.length; i++) {
          var testtype
          var ii = 0
          const theTest = this.exams[i]
          if (theTest.practice) {
            testtype = 'Æ'
          } else {
            testtype = 'P'
          }
          const kkey = theTest.name + ' ' + testtype
          const testscore = parseInt(theTest.final_results * 10000) / 1000
          avrgscore = avrgscore + testscore

          this.barChartOption.xAxis.data.push(kkey)
          var catHolder = [0, 0, 0, 0, 0]

          for (ii = 0; ii < theTest.answers.length; ii++) {
            // tekur saman einkunn fyrir hvert fag fyrir sig
            const scorefactor = (theTest.answers.length * catHolder.length) / 100
            const catSlot = theTest.answers[ii].question_category - 1
            catHolder[catSlot] = Number(catHolder[catSlot]) + parseInt(theTest.answers[ii].points_given / scorefactor)

            // this.xTests[i][0] = theTest.answers[ii].question_category_name
            // this.xTests[catSlot][i] = Number(this.xTests[catSlot][i]) + Number(theTest.answers[ii].points_given)
          }

          var c = 0
          for (c = 0; c < catHolder.length; c++) {
            // this.xTests[c][0] = catNames[c]
            this.xTests[c].push(catHolder[c])
          }

          console.log(catHolder)
          console.log(this.barChartOption.xAxis.data)
          console.log(this.barChartOption.series)
          console.log(this.xTests)
        }

        for (iii = 0; iii < catHolder.length; iii++) {
          var lableholder
          if (iii === catHolder.length - 1) {
            lableholder = {
              show: true,
              margin: 15,
              fontSize: 18,
              position: 'top',
              formatter: (params) => {
                let total = 0
                this.barChartOption.series.forEach(serie => {
                  total += serie.data[params.dataIndex]
                })
                return total
              }
            }
          } else {
            lableholder = { show: false }
          }
          var bar = {
            name: catNames[iii],
            stack: 'one',
            type: 'bar',
            emphasis: emphasisStyle,
            label: lableholder,
            data: this.xTests[iii]
          }
          console.log(bar)

          this.barChartOption.series.push(bar)
        }

        this.averagescore = parseInt((avrgscore / this.exams.length) * 100) / 100
      })
      .catch(error => console.log('Error', error.message))
  }
}
</script>

<style scoped>
.echarts {
  width: 100%;
  height: 600px;
}
</style>
<!--Categories-->

<!--Results-->
<!--Time axis-->
