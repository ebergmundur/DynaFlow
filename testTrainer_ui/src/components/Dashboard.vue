<template>
  <div class="q-pa-md row items-start q-gutter-md justify-center">
    <div class="mainlist col-lg-6 col-md-8 col-sm ">

      <q-card>
        <q-card-section>
                <q-toolbar>
        <q-toolbar-title>
          Mælaborð
        </q-toolbar-title>
      </q-toolbar>

          <q-list>
            <q-item
              v-for="(exam, index) in exams"
              :key="index"
            >
              <q-item-section>
                <q-item-label>{{ exam.name }}</q-item-label>
                <q-item-label caption lines="2">
                  {{ formatDate(exam.created_date) }}

                </q-item-label>
              </q-item-section>

              <q-item-section side top>
                <q-item-label caption>{{ exam.results.given_points }}</q-item-label>
                <q-item-label caption>{{ exam.results.optional_points }}</q-item-label>
                <!--                <q-icon name="star" color="yellow"/>-->
              </q-item-section>

            </q-item>

          </q-list>

        </q-card-section>
        <q-card-section class="q-pa-none echarts">
        <IEcharts :option="barChartOption" :resizable="true" />
      </q-card-section>
    </q-card>

    </div>
  </div>
</template>

<script>
// import axios from 'axios'
import { date } from 'quasar'
import store from 'src/store'
import IEcharts from 'vue-echarts-v3/src/full.js'
import { axiosBase } from 'src/api/axios-base'

export default {
  name: 'Dashboard',
  data () {
    return {
      exams: '',
      barChartOption: {
        grid: {
          bottom: '25%'
        },
        legend: {},
        tooltip: {},
        dataset: {
          // dimensions: ['product', '2015', '2016', '2017'],
          dimensions: [],
          source: [
            // { product: 'Matcha Latte', 2015: 43.3, 2016: 85.8, 2017: 93.7 },
            // { product: 'Milk Tea', 2015: 83.1, 2016: 73.4, 2017: 55.1 },
            // { product: 'Cheese Cocoa', 2015: 86.4, 2016: 65.2, 2017: 82.5 },
            // { product: 'Walnut Brownie', 2015: 72.4, 2016: 53.9, 2017: 39.1 }
          ]
        },
        xAxis: {
          type: 'category',
          axisLabel: {
            rotate: 45
          }
        },
        yAxis: {},
        // Declare several bar series, each will be mapped
        // to a column of dataset.source by default.
        series: [
          // { type: 'bar' },
          // { type: 'bar' },
          // { type: 'bar' }
        ]
      }
    }
  },
  components: {
    IEcharts
  },
  methods: {
    formatDate (d) {
      return date.formatDate(d, 'YYYY-MM-DD HH:mm')
    }
  },
  mounted () {
    const access = store.getters.token // attempt to obtain new access token by running 'refreshToken' action
    axiosBase.get({
      headers: { Authorization: `Bearer ${access}` }, // the new access token is attached to the authorization header
      url: '/api/dashboard/'
    })
      .then(response => {
        this.exams = JSON.parse(JSON.stringify(response.data))

        this.barChartOption.dataset.legend = {}
        // this.barChartOption.legend = { 73: '73', 74: '74', 75: '75' }
        // this.barChartOption.dataset.dimensions = ['prof', '73', '74', '75']
        this.barChartOption.dataset.source = [
          { prof: 'PRÓF' }
        ]
        this.barChartOption.series = []

        this.barChartOption.dataset.dimensions = ['prof']
        // this.barChartOption.dataset.source = []
        var i = 0
        for (i = 0; i < this.exams.length; i++) {
          // console.log(this.exams[i].id)
          var kkey = this.exams[i].name
          var testname = this.exams[i].name
          this.barChartOption.dataset.dimensions.push(testname)
          this.barChartOption.legend[kkey] = this.exams[i].name
          this.barChartOption.dataset.source[0][kkey] = parseInt(this.exams[i].final_results * 10000) / 100
          this.barChartOption.series.push({ type: 'bar' })
        }

        // parseInt(item.options_ids * 1) == opt.id
        // console.log('legend')
        // console.log(this.barChartOption.legend)
        // console.log('dataset.dimensions')
        // console.log(this.barChartOption.dataset.dimensions)
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
