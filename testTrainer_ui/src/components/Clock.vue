<template>
  <div class="clockframe">
    <div style="float: left; height: 200px;">
    {{ timeNow }}
    </div>
<div style="float: left;">
    <q-circular-progress
      show-value
      font-size="12px"
      :value="circle"
      size="67px"
      :thickness="0.22"
      color="info"
      track-color="grey-3"
      class=""
      style=""
    >
            {{ totaltime }}
<!--            {{ display }}-->
    </q-circular-progress>
</div>
    <div class="butts">

      <q-btn
        dense
        size="xs"
        :icon="mdiRestart"
      />
<!--        @click="reset"-->

      <q-btn
        dense
        size="xs"
        :icon="mdiPlay"
      />
<!--        @click="start"-->
    </div>
  </div>

  <!--      <div class="pBox" @click="start" title="Click to start">-->
  <!--        <div class="timer">-->
  <!--          {{ stateMsg }}-->
  <!--          <br>-->
  <!--          {{ display }} <br> {{circle}}-->
  <!--        </div>-->
  <!--<div class="hover-play" v-bind:class="{ 'hover-playing': state}">-->
  <!--          <i class="fa fa-play-circle"></i>-->
  <!--        </div>-->
  <!--      </div>-->
  <!--      <div class="timer-ctrl">-->
  <!--        <label>Session: &nbsp;-->
  <!--          <input type="text" v-model="sessionCtrl" maxlength="2" class="timer-box-input">-->
  <!--        </label>-->
  <!--        <input type="range" v-model="sessionCtrl" min="0" max="60" class="timer-slider">-->
  <!--        <label>Break: &nbsp;-->
  <!--          <input type="text" v-model="breakCtrl" maxlength="2" class="timer-box-input">-->
  <!--        </label>-->
  <!--        <input type="range" v-model="breakCtrl" min="0" max="60" class="timer-slider">-->
  <!--        <button type="button" class="btn btn-danger" @click="reset">Reset</button>-->
</template>

<script>
// import { mdiPlay, mdiPause, mdiRestart } from '@quasar/extras/mdi-v5'
// import store from 'src/store/index'
import { date } from 'quasar'

// const AUDIO = [new Audio('https://www.dropbox.com/s/5d2dy8xr29246l3/KeyChimes.mp3?raw=1')]
// var
// STOP = 0,
// START = 1,
// BREAK = 2,
// PAUSE = 3,
// TIMEOUT = 4,
// DEFAULT_TIME = 750000,
// DEFAULT_TIME = 1500000,
// DEFAULT_BREAK_TIME = 300000,
// DEFAULT_MINUTE = 12.5,
// DEFAULT_BREAK = 5,
// RESET_TOKEN = 0

export default {
  // el: '#pomoApp',
  name: 'clock',
  data: function () {
    return {
      // limit: 0,
      // counter: 0,
      // sessionCtrl: 0,
      // breakCtrl: 0,
      startTime: null,
      // timerID: null,
      // state: STOP,
      // stateMsg: 'Session',
      timeNow: null,
      totaltime: null,
      clock: null
    }
  },
  computed: {
    // display: function () {
    //   return this.cMinute + ':' + this.cSecond
    // },
    // timeAllowed: function () {
    //   return store.getters.currTimeAllowed.payload
    // },
    // circle: function () {
    //   return (this.limit - this.counter) / 10000
    // },
    // cMinute: function () {
    //   var strMin = 0
    //   if (this.state === STOP) {
    //     strMin = this.sessionCtrl
    //   } else {
    //     strMin = ((this.counter / 1000) / 60) | 0
    //   }
    //
    //   if (strMin < 10) {
    //     return '0' + strMin
    //   } else {
    //     return strMin
    //   }
    // },
    // cSecond: function () {
    //   var strSec = ((this.counter / 1000) % 60) | 0
    //   if (strSec < 10) {
    //     return '0' + strSec
    //   } else {
    //     return strSec
    //   }
    // }
  },
  created: function () {
    this.clock = setInterval(this.clockNow, 1000)
    this.startTime = Date.now()
    // console.log('timeAllowed')
    // console.log(this.timeAllowed)
    // this.limit = this.timeAllowed * 60000
    // this.counter = 0
    // DEFAULT_MINUTE = this.timeAllowed
    // this.reset()

    // if (localStorage.length) {
    //   this.syncLocalStorage()
    // } else {
    //   this.sessionCtrl = DEFAULT_MINUTE
    //   this.breakCtrl = DEFAULT_BREAK
    // }
    // this.mdiPlay = mdiPlay
    // this.mdiPause = mdiPause
    // this.mdiRestart = mdiRestart
  },
  watch: {
    // sessionCtrl: function (val) {
    //   if (RESET_TOKEN !== 1) {
    //     localStorage.setItem('sessionCtrl', val)
    //   }
    // },
    // breakCtrl: function (val) {
    //   if (RESET_TOKEN !== 1) {
    //     localStorage.setItem('breakCtrl', val)
    //   }
    // }
  },
  methods: {
    clockNow () {
      this.timeNow = date.formatDate(Date.now(), 'HH:mm:ss').toString()
    }
    // start: function () {
    //   if (this.state !== START) {
    //     this.state = START
    //     this.startTime = Date.now()
    //
    //     var newLimit = this.sessionCtrl * 60 * 1000
    //
    //     if (newLimit !== this.limit) {
    //       this.limit = newLimit
    //       this.counter = newLimit
    //     }
    //
    //     if (!this.timerID) {
    //       this.timerID = setInterval(this.countdown.bind(this), 100)
    //     }
    //   }
    //   return this.timerID
    // },
    // countdown: function () {
    //   if (this.state === START || this.state === BREAK) {
    //     this.counter = this.limit - (Date.now() - this.startTime)
    //     if (this.counter <= 0) {
    //       AUDIO[0].play()
    //       if (this.state === BREAK) {
    //         this.state = START
    //         this.stateMsg = 'Session'
    //         this.startTime = Date.now()
    //         this.limit = this.sessionCtrl * 60 * 1000
    //       } else if (this.state === START) {
    //         this.state = BREAK
    //         this.stateMsg = '- Break -'
    //         this.startTime = Date.now()
    //         this.limit = this.breakCtrl * 60 * 1000
    //       }
    //     }
    //   }
    //   return this.counter
    // },
    // reset: function () {
    //   RESET_TOKEN = 1
    //   this.state = STOP
    //   this.stateMsg = 'Session'
    //   this.sessionCtrl = DEFAULT_MINUTE
    //   this.breakCtrl = DEFAULT_BREAK
    //   clearInterval(this.timerID)
    //   this.startTime = this.timerID = null
    //   this.counter = this.limit = this.limit = DEFAULT_TIME
    //   localStorage.clear()
    //   return this.counter
    // },
    // syncLocalStorage: function () {
    //   this.sessionCtrl = localStorage.getItem('sessionCtrl')
    //   this.breakCtrl = localStorage.getItem('breakCtrl')
    // }
  }
}
</script>

<style scoped lang="css">
.clockframe {
  /*border: 1px solid greenyellow;*/
  position: absolute;
  right: 10px;
  top: 10px;
  height: 75px;
  width: 320px;
}

.clockframe div.butts {
  float: right;
  width: 40px;
}

</style>
