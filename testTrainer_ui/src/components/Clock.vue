<template>
  <div class="clockframe">
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
      {{ display }}
    </q-circular-progress>

    <div class="butts">

      <q-btn
        dense
        :size="xs"
        :icon="mdiRestart"
        @click="reset"

      />

      <q-btn
        dense
        :size="xs"
        :icon="mdiPlay"
        @click="start"
      />
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
import { mdiPlay, mdiPause, mdiRestart } from '@quasar/extras/mdi-v5'
import store from 'src/router/store'

const AUDIO = [new Audio('https://www.dropbox.com/s/5d2dy8xr29246l3/KeyChimes.mp3?raw=1')]
var STOP = 0,
  START = 1,
  BREAK = 2,
  // PAUSE = 3,
  // TIMEOUT = 4,
  // DEFAULT_TIME = 750000,
  DEFAULT_TIME = 1500000,
  // DEFAULT_BREAK_TIME = 300000,
  DEFAULT_MINUTE = 20,
  DEFAULT_BREAK = 5,
  RESET_TOKEN = 0

export default {
  // el: '#pomoApp',
  name: 'clock',
  data: function () {
    return {
      limit: 0,
      counter: 0,
      sessionCtrl: 0,
      breakCtrl: 0,
      startTime: null,
      timerID: null,
      state: STOP,
      stateMsg: 'Session'
    }
  },
  computed: {
    display: function () {
      return this.cMinute + ':' + this.cSecond
    },
    timeAllowed: function () {
      return store.getters.currTimeAllowed.payload
    },
    circle: function () {
      return (this.limit - this.counter) / 10000
    },
    cMinute: function () {
      var strMin = 0
      if (this.state === STOP) {
        strMin = this.sessionCtrl
      } else {
        strMin = ((this.counter / 1000) / 60) | 0
      }

      if (strMin < 10) {
        return '0' + strMin
      } else {
        return strMin
      }
    },
    cSecond: function () {
      var strSec = ((this.counter / 1000) % 60) | 0
      if (strSec < 10) {
        return '0' + strSec
      } else {
        return strSec
      }
    }
  },
  created: function () {
    console.log('timeAllowed')
    console.log(this.timeAllowed)
    this.limit = this.timeAllowed * 60000
    this.counter = 0
    DEFAULT_MINUTE = this.timeAllowed
    // this.reset()

    if (localStorage.length) {
      this.syncLocalStorage()
    } else {
      this.sessionCtrl = DEFAULT_MINUTE
      this.breakCtrl = DEFAULT_BREAK
    }
    this.mdiPlay = mdiPlay
    this.mdiPause = mdiPause
    this.mdiRestart = mdiRestart
  },
  watch: {
    sessionCtrl: function (val) {
      if (RESET_TOKEN !== 1) {
        localStorage.setItem('sessionCtrl', val)
      }
    },
    breakCtrl: function (val) {
      if (RESET_TOKEN !== 1) {
        localStorage.setItem('breakCtrl', val)
      }
    }
  },
  methods: {
    start: function () {
      if (this.state !== START) {
        this.state = START
        this.startTime = Date.now()

        var newLimit = this.sessionCtrl * 60 * 1000

        if (newLimit !== this.limit) {
          this.limit = newLimit
          this.counter = newLimit
        }

        if (!this.timerID) {
          this.timerID = setInterval(this.countdown.bind(this), 100)
        }
      }
      return this.timerID
    },
    countdown: function () {
      if (this.state === START || this.state === BREAK) {
        this.counter = this.limit - (Date.now() - this.startTime)
        if (this.counter <= 0) {
          AUDIO[0].play()
          if (this.state === BREAK) {
            this.state = START
            this.stateMsg = 'Session'
            this.startTime = Date.now()
            this.limit = this.sessionCtrl * 60 * 1000
          } else if (this.state === START) {
            this.state = BREAK
            this.stateMsg = '- Break -'
            this.startTime = Date.now()
            this.limit = this.breakCtrl * 60 * 1000
          }
        }
      }
      return this.counter
    },
    reset: function () {
      RESET_TOKEN = 1
      this.state = STOP
      this.stateMsg = 'Session'
      this.sessionCtrl = DEFAULT_MINUTE
      this.breakCtrl = DEFAULT_BREAK
      clearInterval(this.timerID)
      this.startTime = this.timerID = null
      this.counter = this.limit = this.limit = DEFAULT_TIME
      localStorage.clear()
      return this.counter
    },
    syncLocalStorage: function () {
      this.sessionCtrl = localStorage.getItem('sessionCtrl')
      this.breakCtrl = localStorage.getItem('breakCtrl')
    }
  },
  mounted () {
    // DEFAULT_TIME = 12 * 60000
    // this.reset()
    // this.limit = 24 * 60000
    // this.counter = 24 * 60000
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
  width: 120px;
}

.clockframe div.butts {
  float: right;
  width: 40px;
}

/*.btn-danger {*/
/*  background: transparent;*/
/*  border-radius: 10px;*/
/*  color: #d9534f;*/
/*  font-family: 'Source San Pro', sans-serif;*/
/*  font-size: 20px;*/
/*  font-weight: 200;*/
/*  transition: all 0.5s ease-in;*/
/*}*/

/*.btn-danger:hover {*/
/*  color: #e79290;*/
/*}*/

/*h1, h2 {*/
/*  font-family: Lato, sans-serif;*/
/*}*/

/*.header {*/
/*  color: #EFB509;*/
/*  height: 100%;*/
/*  text-align: center;*/
/*  padding-top: 5px;*/
/*}*/

/*.header .cover-heading {*/
/*  font-size: 58px;*/
/*  color: #EFB509;*/
/*  margin-bottom: 3.6rem;*/
/*}*/

/* slider */
input[type=range] {
  -webkit-appearance: none;
  margin: 20px 0 40px;
  width: 100%;
}

input[type=range]:focus {
  outline: none;
}

input[type=range]::-webkit-slider-runnable-track {
  width: 100%;
  height: 1px;
  cursor: pointer;
  transition: all 0.5s ease;
  background: #002C54;
  border-radius: 5px;
  border: 0px solid #000101;
}

input[type=range]::-webkit-slider-thumb {
  box-shadow: 0px 0px 0px #000000, 0px 0px 0px #0d0d0d;
  border: 0px solid #000000;
  height: 21px;
  width: 20px;
  border-radius: 10px;
  background: #EFB509;
  cursor: pointer;
  -webkit-appearance: none;
  margin-top: -10px;
}

input[type=range]:focus::-webkit-slider-runnable-track {
  background: #EFB509;
}

input[type=range]::-moz-range-track {
  width: 100%;
  height: 1px;
  cursor: pointer;
  animate: 0.2s;
  box-shadow: 0px 0px 0px #000000, 0px 0px 0px #0d0d0d;
  background: #CD7213;
  border-radius: 25px;
  border: 0px solid #000101;
}

input[type=range]::-moz-range-thumb {
  box-shadow: 0px 0px 0px #000000, 0px 0px 0px #0d0d0d;
  border: 0px solid #000000;
  height: 21px;
  width: 20px;
  border-radius: 10px;
  background: #EFB509;
  cursor: pointer;
}

input[type=range]::-ms-track {
  width: 100%;
  height: 1px;
  cursor: pointer;
  animate: 0.2s;
  background: transparent;
  border-color: transparent;
  border-width: 39px 0;
  color: transparent;
}

input[type=range]::-ms-fill-lower {
  background: #CD7213;
  border: 0px solid #000101;
  border-radius: 50px;
  box-shadow: 0px 0px 0px #000000, 0px 0px 0px #0d0d0d;
}

input[type=range]::-ms-fill-upper {
  background: #CD7213;
  border: 0px solid #000101;
  border-radius: 50px;
  box-shadow: 0px 0px 0px #000000, 0px 0px 0px #0d0d0d;
}

input[type=range]::-ms-thumb {
  box-shadow: 0px 0px 0px #000000, 0px 0px 0px #0d0d0d;
  border: 0px solid #000000;
  height: 21px;
  width: 20px;
  border-radius: 7px;
  background: #EFB509;
  cursor: pointer;
}

input[type=range]:focus::-ms-fill-lower {
  background: #EFB509;
}

input[type=range]:focus::-ms-fill-upper {
  background: #EFB509;
}

/* end of slider */

/*label.disc {*/
/*  background: rgba(75, 105, 123, .7);*/
/*  position: fixed;*/
/*  bottom: 0;*/
/*  right: 5px;*/
/*  font-size: 1.5rem;*/
/*  font-weight: 100;*/
/*  text-align: center;*/
/*  letter-spacing: 2px;*/
/*  padding: 1rem;*/
/*  cursor: pointer;*/
/*  box-shadow: 0 0 3px rgba(25, 42, 46, .75);*/
/*}*/

.disc-href, .disc-href:visited {
  color: #ccc;
}

.disc-href:hover {
  color: #fff;
  text-decoration: none;
}

label.disc:hover {
  background: rgba(75, 105, 123, .85);
}

.pBox {
  height: 64px;
  width: 164px;
  /*border: 1px solid #EFB509;*/
  position: absolute;
  top: 10px;
  right: 10px;
  /*border-radius: 50%;*/
  cursor: pointer;
  /*margin: 1px auto;*/
  overflow: hidden;
  /* prevent selection of text inside keys */
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.pBox:hover .hover-play {
  opacity: 1;
}

.hover-playing {
  opacity: 0 !important;
}

.hover-play {
  /*position: relative;*/
  display: block;
  background: rgba(153, 150, 150, 0.8);
  /*top: 0px;*/
  /*right: 0px;*/
  width: 64px;
  height: 64px;
  border-radius: 50%;
  /*margin: -60px 0 50px 0px;*/
  /*padding: 9px;*/
  z-index: 50;
  opacity: 0;
  transition: opacity 0.5s ease-in;
}

.hover-play i {
  font-size: 7em;
  color: #906d05;
}

.timer {
  /*margin: 50px auto;*/
  /*font-size: 60px;*/
  z-index: 10;
}

.timer-box-input {
  background: #16253D;
  border: 1px solid #EFB509;
  border-radius: 4px;
  width: 45px;
  font-size: 20px;
  text-align: center;
  transition: all 0.4s ease;
}

.timer-box-input:focus {
  border: 1px solid #CD7213;
  box-shadow: none;
  outline: none;
}

.timer-ctrl {
  width: 50%;
  margin: 0 auto 50px;
  font-family: Lato, sans-serif;
  font-size: 20px;
}

.timer-slider {
  margin: 10px 0 20px;
}
</style>
