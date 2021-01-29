<template>
  <q-page class="flex flex-center">

        <div v-if="spinnegal" class="content-center" style="z-index: 1000;">
      <q-spinner-bars
        color="primary"
        size="8em"
        />
      <q-tooltip :offset="[0, 8]">QSpinnerBars</q-tooltip>
    </div>

    <q-card flat
            class="pagecard"
    >
      <q-toolbar class="q-dark">
        <q-toolbar-title>
          Mælaborð - meðaltal {{ averagescore }}
        </q-toolbar-title>
      </q-toolbar>

      <q-card-section class="q-pa-none echarts">
        <IEcharts :option="option" ref="echart"/>
      </q-card-section>
      <!-- <q-card-actions>
        <q-btn @click="onAnswerSubmit" color="positive" label="Allt"/>
        <q-btn @click="onAnswerSubmit" color="positive" label="Æfingar"/>
        <q-btn @click="onAnswerSubmit" color="positive" label="Próf"/>
      </q-card-actions> -->
      <!-- <h1 style="color: red;">{{testDate}}</h1> -->
    </q-card>
    <!-- <br/>
    <div style="float: none; overflow: scroll;" >
      <pre>
      {{this.option.series}}
      {{this.option.xAxis}}
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
var catQuestScore = []

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
      spinnegal: true,
      startDate: 0,
      endDate: 100,
      fixedStartDate: new Date('2021-01-24 00:00'),
      FixedEndDate: new Date('2021-24-12 23:59'),
      chart: null,
      // testDate: null,
      option: {
        width: '84%',
        grid: {
          bottom: '90px',
          left: '75px'
        },
        toolbox: {
          top: '10px',
          right: '10px',
          feature: {
            magicType: {
              type: ['stack', 'tiled']
            },
            // dataZoom: {
            //   yAxisIndex: 'none'
            // },
            restore: { show: false },
            saveAsImage: {},
            dataView: {}
          }
        },
        legend: {
          // data: ['Fag', 'Líffræði', 'Efnafræði', 'Eðlisfræði', 'Stærðfræði', 'Almenn þekking'],
          type: 'scroll',
          orient: 'horisontal',
          right: 15,
          top: 50
        },
        tooltip: {
          trigger: 'item',
          triggerOn: 'click',
          // position: [10, 10],
          enterable: true,
          confine: true,
          transitionDuration: 1.3,
          axisPointer: {
            type: 'none'
          },
          formatter: function (params) {
            var tar
            // console.log(params)
            if (params.value < 0) {
              tar = params[1]
            } else {
              tar = params
            }
            var name = tar.name.split(',')
            var ahref = '<a style="display: block; border: 1px solid darkgray; text-align: center; backgroundcolor; lightgray; color: black; text-decoration: none;" href="#/review/' + catQuestScore[params.dataIndex].id + '/">'
            var catQuest = ahref + catQuestScore[params.dataIndex][params.seriesIndex][0] + ' spurningar,'
            var catScore = catQuestScore[params.dataIndex][params.seriesIndex][1] + ' stig ' + catQuestScore[params.dataIndex][params.seriesIndex][1] / 5 + ' rétt<br>Sjá niðurstöður</a>'

            return name[1] + '<br/>' + tar.seriesName + ' : ' + tar.value + '<br/>' + catQuest + ' ' + catScore
          }
        },
        xAxis: {
          data: [],
          type: 'category',
          name: 'Próf',
          axisLine: { onZero: true },
          splitLine: { show: false },
          splitArea: { show: false },
          // minInterval: 1,
          // maxInterval: 3600 * 1000 * 24,
          axisLabel: {
            show: true,
            rotate: 0,
            formatter: function (params) {
              var par = params.split(',')
              return par[1]
            }
          }
        },
        yAxis: {
          name: '%',
          inverse: false,
          splitArea: { show: true }
        },
        dataZoom: [{
          show: true,
          type: 'slider',
          // brushSelect: true,
          start: 0,
          end: 100,
          rangeMode: ['percent', 'percent'],
          labelFormatter: function (value, valueStr) {
            var par = valueStr.split(',')
            var dt = par[0]
            return date.formatDate(dt, 'YYYY-MM-DD')
          }
        }],
        series: []
      }
    }
  },
  components: {
    IEcharts
  },
  methods: {
    formatDate (d) {
      return date.formatDate(d, 'YYYY-MM-DD')
    },
    onAnswerSubmit () {

    }
  },
  updated () {
  },
  computed: {
    testDate () {
      return this.$route.params.tdate.toString() || null
    }
  },
  mounted () {
    this.access = store.getters.token // attempt to obtain new access token by running 'refreshToken' action
    this.username = store.getters.getUserInfo.username

    // console.log('mánti')
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

        // console.log('this.exams')
        // console.log(this.exams)

        var avrgscore = 0
        var i = 0
        var iii = 0

        this.xTests = [[], [], [], [], []]
        const catNames = ['Líffræði', 'Efnafræði', 'Eðlisfræði', 'Stærðfræði', 'Almenn þekking']

        for (i = 0; i < this.exams.length; i++) {
          var ii = 0
          const theTest = this.exams[i]

          var testtype
          if (theTest.practice) {
            testtype = 'Æfing'
          } else {
            testtype = 'Próf'
          }
          // const kkey = theTest.created_date
          const tdate = new Date(theTest.modified_date)

          const kkeyText = theTest.name + '\n' + testtype + ' ' + theTest.q_count + ' spurningar'
          // const tdtext = tdate.getFullYear() + '-' + tdate.getMonth() + 1 + '-' + tdate.getDate() + 'T' + tdate.getHours() + ':' + tdate.getMinutes() + ':00Z'
          // const tdtext = tdate.getFullYear() + '-' + tdate.getMonth() + '-' + tdate.getDate()
          const kkey = [tdate, kkeyText]
          const testscore = parseInt(theTest.final_results * 10000) / 1000
          avrgscore = avrgscore + testscore

          this.option.xAxis.data.push(kkey)
          var catHolder = [0, 0, 0, 0, 0]

          catQuestScore.push({ name: kkey, id: theTest.id, 0: [0, 0], 1: [0, 0], 2: [0, 0], 3: [0, 0], 4: [0, 0] })

          for (ii = 0; ii < theTest.answers.length; ii++) {
            // tekur saman einkunn fyrir hvert fag fyrir sig
            const scorefactor = (theTest.answers.length * catHolder.length)
            const catSlot = theTest.answers[ii].question_category - 1
            catHolder[catSlot] = Number(catHolder[catSlot]) + parseInt(Number(theTest.answers[ii].points_given / scorefactor) * 100)
            catQuestScore[i][catSlot][0]++
            catQuestScore[i][catSlot][1] += theTest.answers[ii].points_given

            // this.xTests[i][0] = theTest.answers[ii].question_category_name
            // this.xTests[catSlot][i] = Number(this.xTests[catSlot][i]) + Number(theTest.answers[ii].points_given)
          }

          var c = 0
          for (c = 0; c < catHolder.length; c++) {
            // this.xTests[c][0] = catNames[c]
            this.xTests[c].push(catHolder[c])
          }
        }

        // console.log(this.option.dataZoom)

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
                this.option.series.forEach(serie => {
                  total += serie.data[params.dataIndex]
                })
                return total + '%'
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
          this.option.series.push(bar)
        }
        // this.chart.setOption(this.option)
        this.averagescore = parseInt((avrgscore / this.exams.length) * 100) / 100
        this.spinnegal = false
        this.chart = this.$refs.echart
      })
      .then(response => {
        if (this.testDate !== null) {
          // console.log('range change')
          // console.log(this.testDate)

          // console.log(this.option.dataZoom.start)
          // console.log(this.option.dataZoom.end)

          const start = new Date(this.testDate + 'T00:00:00Z')
          const end = new Date(this.testDate + 'T23:59:59Z')
          // this.testDate + ' 23:59'
          const datalength = this.exams.length
          // console.log('datalength')
          // console.log(datalength)

          var ix = 0
          var idxStart = 0
          var idxEnd = 100
          var startSet = true
          for (ix = 0; ix < datalength; ix++) {
            console.log('dagar', this.option.xAxis.data[ix][0].getDate(), start.getDate())
            // console.log(this.option.xAxis.data[ix][0], this.option.xAxis.data[ix][0].getTime(), this.option.xAxis.data[ix][0].getTime() <= start.getTime(), start, start.getTime())
            if (this.option.xAxis.data[ix][0].getDate() === start.getDate() && startSet) {
              console.log('inn', ix, idxStart, idxEnd, this.testDate)
              idxStart = ix
              startSet = false
            }
            if (this.option.xAxis.data[ix][0].getDate() === end.getDate()) {
              console.log('ut', ix, idxStart, idxEnd, this.testDate)
              idxEnd = ix
            }
          }
          console.log(idxStart, idxEnd)

          if (idxStart === idxEnd) {
            idxStart = idxStart - 0.1
            idxEnd = idxEnd + 0.1
          }

          this.startDate = parseInt((idxStart / datalength) * 100)
          this.endDate = parseInt((idxEnd / datalength) * 100)

          this.chart.instance.setOption({ dataZoom: [{ start: this.startDate }] })
          this.chart.instance.setOption({ dataZoom: [{ end: this.endDate }] })
        }
      })
      .catch(error => console.log('Error', error.message))
    // this.IEcharts.instance.setOption(this.option)
    // console.log(this.IEcharts)
  }
}

</script>

<style lang="sass" scoped>

.echarts
  width: 100%
  height: 600px

.tiplink
  display: block
  border: 1px solid green
  color: red
  text-decoration: none

</style>
<!--Categories-->

<!--Results-->
<!--Time axis-->
