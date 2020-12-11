<template>
  <div class="container">
    <line-chart
      v-if="loaded"
      :chartdata="chartdata"
      :options="options"/>
  </div>
</template>

<script>
import LineChart from './Chart.vue'

export default {
  name: 'LineChartContainer',
  components: { LineChart },
  data: () => ({
    loaded: false
  }),
  props: {
    chartdata: {
      labels: ['January', 'February'],
      datasets: [{
        label: 'Data One',
        backgroundColor: '#f87979',
        data: [40, 20]
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false
    }
  },
  async mounted () {
    this.loaded = false
    try {
      // const { userlist } = await fetch('/api/userlist')
      // this.chartdata = userlist
      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  }
}
</script>
