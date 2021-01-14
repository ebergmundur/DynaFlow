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

var emphasisStyle = {
  itemStyle: {
    barBorderWidth: 1,
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
          bottom: '15%'
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
          type: 'scroll',
          orient: 'vertical',
          right: 0
        },
        tooltip: {
          trigger: 'item',
          axisPointer: {
            type: 'line'
          },
          formatter: function (params) {
            console.log(params)
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
          name: 'Próf',
          axisLine: { onZero: true },
          splitLine: { show: false },
          splitArea: { show: false }
        },
        yAxis: {
          name: '%',
          inverse: false,
          splitArea: { show: true }
        },
        visualMap: {
          type: 'continuous',
          dimension: 2,
          text: ['', ''],
          inverse: true,
          itemHeight: 200,
          calculable: true,
          min: 100,
          max: -100,
          top: 60,
          left: 10,
          inRange: {
            colorLightness: [0.4, 0.8]
          },
          outOfRange: {
            color: '#bbb'
          },
          controller: {
            inRange: {
              color: '#2f4554'
            }
          }
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
    })
      .then(response => {
        this.exams = JSON.parse(JSON.stringify(response.data))
        console.log(this.exams)
        var avrgscore = 0
        var i = 0
        var iii = 0
        for (i = 0; i < this.exams.length; i++) {
          var testtype
          var ii = 0
          const theTest = this.exams[i]
          if (theTest.practice) {
            testtype = 'Æ'
          } else {
            testtype = 'P'
          }
          const kkey = theTest.name + ' ' + testtype + ' ' + theTest.id
          const testscore = parseInt(theTest.final_results * 10000) / 1000
          avrgscore = avrgscore + testscore

          this.barChartOption.xAxis.data.push(kkey)
          this.xTests.push([])

          this.xTests[i].push(0, 0, 0, 0, 0)

          for (ii = 0; ii < theTest.answers.length; ii++) {
            const catSlot = theTest.answers[ii].question_category
            this.xTests[i][catSlot] = Number(this.xTests[i][catSlot]) + Number(theTest.answers[ii].points_given)
          }
        }

        for (iii = 0; iii < this.xTests[0].length; iii++) {
          var lableholder
          if (iii === this.xTests[0].length - 1) {
            lableholder = {
              normal: {
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
            }
          } else {
            lableholder = { show: false }
          }
          var bar = {
            name: iii.toString(),
            stack: 'one',
            type: 'bar',
            emphasis: emphasisStyle,
            label: lableholder,
            data: this.xTests[iii]
          }

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
  height: 400px;
}
</style>
<!--Categories-->

<!--Results-->
<!--Time axis-->
