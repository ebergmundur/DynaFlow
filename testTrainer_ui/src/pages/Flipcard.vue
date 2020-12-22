<template>
  <q-page class="justify-center"
          @focusin.native="activateNavigation"
          @focusout.native="deactivateNavigation"
          @keydown.native="keyprocess"
  >
    <div class="q-pa-lg-md q-mt-md ">
      <div class="row q-gutter-md justify-center col"
      >

        <q-slide-item
          id="sledinn"
          @left="onLeft"
          @right="onRight"
          @top="onTop"
          @bottom="onBottom"
          @click="flipcard"
          left-color="transparent"
          right-color="transparent"
          top-color="transparent"
          bottom-color="transparent"
          class="flip-card"
          style="width: 300px; height: 460px;"
        >
          <!--      @click="flippit"-->

          <template v-slot:top>
            <q-icon name="link"/>
          </template>
          <template v-slot:right>
            <q-icon name="forward"/>
          </template>
          <template v-slot:bottom>
            <q-icon name="link_off"/>
          </template>
          <template v-slot:left>
            <q-icon name="back"/>
          </template>

          <q-scroll-area
            horizontal
            ref="scrollArea"
            class=""
            position=300
            style="height: 460px; max-width: 300px; overflow: visible;"
          >
            <q-item
              class="q-pa-none flip-card justify-center"
              style="width: 900px; height: 400px; margin-top: 30px;"
            >
              <div
                id="thecard"
                class="flip-card-inner"
                v-bind="props1"
                :class="flippclass"

              >

                <div class="col q-pa-none flip-card-front">
                  <q-toolbar class="q-dark q-ma-none" style="background-color: #616161;">
                    <q-toolbar-title>
                      Spurning
                    </q-toolbar-title>
                  </q-toolbar>
                  <div class="row content-center xtext-justify " style="height: 90%;">

                    <div class="col-12 q-pa-md scroll">
                      <div class="">{{ currentQuestion.question }}</div>
                      {{ currentQuestion.description }}
                    </div>

                  </div>
                </div>

                <div class="flip-card-back">
                  <q-toolbar class="q-dark q-ma-none" style="background-color: #616161;">
                    <q-toolbar-title>
                      Svar
                    </q-toolbar-title>
                  </q-toolbar>

                  <div class="row content-center" style="height: 90%;">
                    <div
                      v-for="opt in currentOptions"
                      :key="opt.id"
                      class="col-12 q-pa-md scroll"
                    >
                      <div v-if="opt.correct" class="content-center">
                        {{ opt.answer }}
                      </div>
                    </div>
                  </div>
                </div>
              </div>

            </q-item>
          </q-scroll-area>
        </q-slide-item>
        <q-separator></q-separator>

        <div class="col-2 col-lg-offset-5 align-center text-center redborder">
          <div class="row col">
            <div class="col-12">Merkja „kann vel“ {{frontside}}</div>
          </div>
          <div class="row col-12">
            <div class="col-3 redborder" style="float: left;">Fyrri</div>
            <div class="col-6 redborder" style="float: left;">{{ navigationActive }}</div>
            <div class="col-3 redborder" style="float: right;">Svar</div>
          </div>
          <div class="row col">
            <div class="col-12">Næsta spurning</div>
          </div>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
import store from 'src/store'
import { date } from 'quasar'
import { getAPI } from 'src/api/axios-base'
// import axios from 'axios'

const access = store.getters.token // attempt to obtain new access token by running 'refreshToken' action

// const card = document.getElementById('thecard')

// const sledinn = document.getElementById('sledinn')

export default {
  name: 'Question',
  computed: {
    currentQuestion () {
      return store.getters.currQest.payload
    },
    formDate () {
      return date.formatDate(this.date, 'YYYY-MM-DD')
    },
    currentOptions () {
      return store.getters.currQest.payload.options
    },
    props1 () {
      return this.toggle1 === true
        ? {
          class: 'flip-card-inner',
          style: 'width: 0px; margin-right: 300px; color: transparent;'
        }
        : {
          class: 'flip-card-inner',
          style: 'width: 300px;'
        }
    }
  },
  methods: {
    setQuestion (e) {
      var index = 0
      if (e > -1) {
        index = e - 1
      } else {
        index = 0
      }
      this.hinttext = ''
      this.editingIndex = index
      this.question = JSON.parse(JSON.stringify(this.myJson[index]))
      store.commit({ type: 'setQuestion', payload: this.question })
      // index.commit({ type: 'setTestQuestion', payload: [] })
      // Question.setAnswerChecked()
      this.currPoints = this.question.points
      this.questNum = index + 1
      this.flippclass = 'flippover'
      this.position = 300
      this.$refs.scrollArea.setScrollPosition(this.position, 200)
    },
    activateNavigation () {
      this.navigationActive = true
    },

    deactivateNavigation () {
      this.navigationActive = false
    },
    flipcard () {
      if (this.flippclass === 'flipp') {
        this.flippclass = 'flippover'
        this.frontside = true
      } else {
        this.flippclass = 'flipp'
        this.frontside = false
      }
    },
    keyprocess (e) {
      if (e.keyCode === 32) {
        // console.log('spacebar')
        // console.log(card)
        this.flipcard()
        // this.onRight()
      } else if (e.keyCode === 39) {
        console.log('right')
        // console.log(e.keyCode)
        if (this.position === 600) {
          this.position = 300
        } else {
          this.position = 600
        }
        this.$refs.scrollArea.setScrollPosition(this.position, 200)
        if (!this.frontside) {
          this.flippit()
        }
      } else if (e.keyCode === 38) {
        console.log('top')
        console.log(e.keyCode)
        // sledinn.onTop()
      } else if (e.keyCode === 37) {
        console.log('left')
        // console.log(e.keyCode)
        if (this.position >= 300) {
          this.position = 0
        } else {
          this.position = 300
        }
        this.$refs.scrollArea.setScrollPosition(this.position, 200)
        // sledinn.onBottom()
      } else if (e.keyCode === 40) {
        console.log('bottom')
        console.log(e.keyCode)
      }
    },
    finalize (reset) {
      this.time = setTimeout(() => {
        reset()
      }, 500)
    },
    onLeft ({ reset }) {
      this.$q.notify('Left action triggered. Resetting in 1 second.')
      this.finalize(reset)
    },
    onRight ({ reset }) {
      this.flippit()
      // this.$q.notify('Right action triggered. Resetting in 1 second.')
      // console.log(flippers)
      // flippers.childNodes[0]
      // document.getElementsByClassName('flip-card-inner').childNodes[1].className += ' flipp'
      // this.finalize(reset)
    },
    onBottom ({ reset }) {
      this.$q.notify('Bottom action triggered. Resetting in 1 second.')
      this.finalize(reset)
    },
    onTop ({ reset }) {
      this.$q.notify('Top action triggered. Resetting in 1 second.')
      this.finalize(reset)
    },
    // rottto (i) {
    //   i.setAttribute('style', 'transform: rotateY(180deg)')
    // },
    flippit () {
      // console.log('flippit')
      getAPI({
        method: 'get',
        headers: { Authorization: `Bearer ${access}` },
        url: '/api/flipcard/'
      })
        .then(response => {
          this.myJson = JSON.parse(JSON.stringify(response.data))
          // console.log(this.myJson)
          this.setQuestion(1)
        })
        .catch(error => console.log('Error', error.message))
    }
  },
  mounted () {
    this.flippit()
    window.addEventListener('keyup', this.keyprocess)
  },
  beforeDestroy () {
    clearTimeout(this.timer)
    window.removeEventListener('keydown', this.handleKeyUp)
  },
  data () {
    return {
      // currentOptions: this.currentQuestion.options,
      cQ: 0,
      navigationActive: false,
      // cancel: 0,
      toggle1: false,
      time_allowed: 0,
      time_taken: 0,
      time_step: 0,
      time: null,
      tesing_user: 1,
      flippclass: '',
      position: 0,
      frontside: true
    }
  }
}

// TODO Hreinsa currTestQuest á milli spurninga
</script>

<style scoped lang="css">
.quest-options {
  border: 1px solid #8d8c8c;
  padding: 5px;
  margin: 5px 0;
  background-color: #eaeaea;
}

div.q-slide-item:focus {
  border: 1px solid crimson;
  background-color: pink;
}

/* The flip card container - set the width and height to whatever you want. We have added the border property to demonstrate that the flip itself goes out of the box on hover (remove perspective if you don't want the 3D effect */
.flip-card {
  background-color: transparent;
  /*width: 300px;*/
  /*height: 200px;*/
  border: 1px solid #f1f1f1;
  perspective: 1000px; /* Remove this if you don't want the 3D effect */
}

/* This container is needed to position the front and back side */
.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  text-align: center;
  transition: transform 0.8s;
  transform-style: preserve-3d;
}

/*Do an horizontal flip when you move the mouse over the flip box container*/
/*.flip-card:hover .flip-card-inner {*/
/*  transform: rotateY(180deg);*/
/*}*/

/*Do an horizontal flip when you move the mouse over the flip box container */
.flipp {
  transform: rotateY(180deg);
}

.flippover {
  transform: rotateY(-0deg);
}

/* Position the front and back side */
.flip-card-front, .flip-card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  -webkit-backface-visibility: hidden; /* Safari */
  backface-visibility: hidden;
}

/* Style the front side (fallback if image is missing) */
.flip-card-front {
  /*background-color: #bbb;*/
  background-color: #FFFFFF;
  /*color: black;*/
}

/* Style the back side */
.flip-card-back {
  /*background-color: dodgerblue;*/
  background-color: #FFFFFF;
  /*color: white;*/
  transform: rotateY(180deg);
}

</style>
