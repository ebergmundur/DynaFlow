<template>
  <IEcharts
    :option="options"
    :loading="loading"
  />
</template>

<script>

import IEcharts from 'vue-echarts-v3/src/full.js'
import { getAPI } from 'src/api/axios-base'
import store from 'src/store'

const access = store.getters.token

// function dash2 (d) {
//   alert(d)
// }

export default {
  name: 'Heatmap',
  data () {
    return {
      loading: false,
      data: [],
      options: {
        tooltip: {
          trigger: 'item',
          triggerOn: 'click',
          enterable: true,
          appendToBody: true,
          formatter: function (params, ticket, callback) {
            // console.log(params)
            var months = ['jan', 'feb', 'mar', 'apr', 'maí', 'jún', 'júl', 'ágú', 'sep', 'okt', 'nóv', 'des']
            var ahref = '<a style="display: block; border: 1px solid darkgray; text-align: center; backgroundcolor; lightgray; color: black; text-decoration: none;" href="#/dashboard/' + params.value[0].getFullYear() + '-' + params.value[0].getMonth() + 1 + '-' + params.value[0].getDate() + '" >Sjá mælaborð</a>'
            var lbl = params.value[0].getDate() + '. ' + months[params.value[0].getMonth()] + '. ' + params.value[0].getFullYear() +
              '<br><strong>' + params.value[1] + ' próf/æfingar</strong><br>' + ahref
            return lbl
          }
        },
        dayLabel: {
          show: true,
          fontSize: 12
        },
        visualMap: {
          min: 1,
          max: 5,
          // type: 'piecewise',
          orient: 'horizontal',
          left: 'center',
          text: ['High', '1'],
          top: 65,
          textStyle: {
            color: '#868686'
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
          left: 70,
          right: 30,
          width: 'auto',
          height: 'auto',
          cellSize: ['auto', 16],
          range: ['2020-01-01', '2021-12-31'],
          monthLabel: {
            nameMap: ['jan', 'feb', 'mar', 'apr', 'maí', 'jún', 'júl', 'ágú', 'sep', 'okt', 'nóv', 'des'],
            color: '#929292'
          },
          dayLabel: {
            nameMap: ['su', 'má', 'þr', 'mi', 'fi', 'fö', 'la'],
            color: '#929292'
          },
          itemStyle: {
            borderWidth: 0.5
          },
          yearLabel: {
            show: true,
            color: '#929292',
            margin: 40
          }
        },
        series: {
          type: 'heatmap',
          coordinateSystem: 'calendar',
          data: [],
          label: {
            show: true,
            fontSize: 9,
            formatter: function (params, ticket, callback) {
              return params.value[0].getDate()
            }
          }
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
    dash (d) {
      // console.log(d)
      alert(d)
    }
  },
  mounted () {
    // console.log('mounted chart')
    // console.log(this.option)
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

        var dateslot = 0
        var minYear = 2020
        var maxYear = 2030
        var maxScore = 5
        var i = 0
        for (i = 0; i < this.exams.length; i++) {
          const ddd = new Date(this.exams[i].modified_date)
          var dd = new Date(ddd.getFullYear(), ddd.getMonth(), ddd.getDate())

          if (i === 0) {
            maxYear = ddd.getFullYear()
            minYear = ddd.getFullYear()
          }

          if (maxYear < ddd.getFullYear()) {
            maxYear = ddd.getFullYear()
          }
          if (minYear > ddd.getFullYear()) {
            minYear = ddd.getFullYear()
          }

          if (i === 0) {
            this.options.series.data.push([dd, 1])
          } else {
            if (this.options.series.data[dateslot][0].toString() === dd.toString()) {
              // if the date is still the same
              this.options.series.data[dateslot][1] = this.options.series.data[dateslot][1] + 1
            } else {
              // should kick when new date appears in array
              this.options.series.data.push([dd, 1])
              dateslot++
            }
            if (maxScore < this.options.series.data[dateslot][1]) {
              maxScore = this.options.series.data[dateslot][1]
            }
          }
        }

        this.options.calendar.range = [minYear + '-01-01', maxYear + '-12-31']
        this.options.visualMap.max = maxScore + 3
        this.options.visualMap.text[0] = maxScore + 2
        // console.log(this.options.series.data)
      })
      .catch(error => console.log('Error', error.message))
  },
  beforeCreate () {
    // console.log('to be created chart')
  }
}
</script>

<style lang='css' scoped >
/* .echarts {
  width: 100%;
  height: 600px;
} */
</style>
