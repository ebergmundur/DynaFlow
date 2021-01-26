<template>
      <IEcharts :option="options" :loading="loading" />
</template>

<script>

import IEcharts from 'vue-echarts-v3/src/full.js'
import { getAPI } from 'src/api/axios-base'
import store from 'src/store'

const access = store.getters.token

export default {
  name: 'Heatmap',
  data () {
    return {
      loading: false,
      data: [],
      options: {
        tooltip: {},
        visualMap: {
          min: 1,
          max: 5,
          // type: 'piecewise',
          orient: 'horizontal',
          left: 'center',
          text: ['High', '1'],
          top: 65,
          textStyle: {
            // color: '#000'
          }
        },
        toolbox: {
          top: '10px',
          right: '10px',
          feature: {
            saveAsImage: {}
          }
        },
        calendar: {
          top: 120,
          left: 60,
          right: 30,
          cellSize: ['auto', 16],
          range: ['2020-01-01', '2021-12-31'],
          monthLabel: {
            nameMap: ['jan', 'feb', 'mar', 'apr', 'maí', 'jún', 'júl', 'ágú', 'sep', 'okt', 'nóv', 'des']
          },
          dayLabel: {
            nameMap: ['su', 'má', 'þr', 'mi', 'fi', 'fö', 'la']
          },
          itemStyle: {
            borderWidth: 0.5
          },
          yearLabel: {
            show: true
          }
        },
        series: {
          type: 'heatmap',
          coordinateSystem: 'calendar',
          data: []
        },
        dataZoom: [{
          type: 'inside'
        }]
      }
    }
  },
  components: {
    IEcharts
  },
  methods: {
  },
  mounted () {
    console.log('mounted chart')
    console.log(this.option)
    getAPI({
      url: '/api/heatmap/',
      method: 'post',
      data: {
        username: store.getters.getUserInfo.username
      },
      headers: { Authorization: `Bearer ${access}` }
    })
      .then(response => {
        this.exams = JSON.parse(JSON.stringify(response.data))

        var slotValue = 0
        var dateslot = 0
        var minYear = 2020
        var maxYear = 2030
        var maxScore = 5
        var i = 0
        for (i = 0; i < this.exams.length; i++) {
          const ddd = new Date(this.exams[i].modified_date)
          const dd = new Date(ddd.getFullYear(), ddd.getMonth(), ddd.getDate())

          if (i === 0) {
            // console.log('initial pDate: ' + dd)
            this.options.series.data.push([dd, 1])
            maxYear = ddd.getFullYear()
            minYear = ddd.getFullYear()
          }

          if (maxYear < ddd.getFullYear()) {
            maxYear = ddd.getFullYear()
          }
          if (minYear > ddd.getFullYear()) {
            minYear = ddd.getFullYear()
          }

          // console.log('dd: ' + dd)
          // console.log('pDate: ' + previousDate)
          // console.log('slott: ' + this.options.series.data[dateslot][0])
          // console.log(this.options.series.data[dateslot][0].toString() === dd.toString())

          if (this.options.series.data[dateslot][0].toString() === dd.toString()) {
            // if the date is still the same
            slotValue++
            this.options.series.data[dateslot][1] = slotValue
          } else {
            dateslot++
            // should kick when new date appears in array
            slotValue = 0
            this.options.series.data.push([dd, 1])
          }
          if (maxScore < slotValue) {
            maxScore = slotValue
          }
        }

        this.options.calendar.range = [(minYear - 1) + '-01-01', maxYear + '-12-31']
        this.options.visualMap.max = maxScore + 3
        this.options.visualMap.text[0] = maxScore + 2
        console.log(this.options)
      })
      .catch(error => console.log('Error', error.message))
  },
  beforeCreate () {
    console.log('to be created chart')
  }
}
</script>

<style lang='css' scoped >
/* .echarts {
  width: 100%;
  height: 600px;
} */
</style>
