<template>
  <q-page
    class="flex flex-center"
    @focusin.native="activateNavigation"
    @focusout.native="deactivateNavigation"
    @keydown.native="keyprocess"
  >
    <div class="content" >
    <div class="card"  ref="cardholder" v-touch-swipe.mouse.touch="doSomething"  v-on:click="toggleCard" >
    <div class="front" id="cardfrontID" ref="cardfront">
       <div class="">{{ currentQuestion.question }}</div>
                      {{ currentQuestion.description }}
    </div>
    <div class="back" id="cardbackID" ref="cardback">
      <div>
        <div
                      v-for="opt in currentOptions"
                      :key="opt.id"
                      class="col-12 q-pa-md scroll"
                    >
                      <div v-if="opt.correct" class="content-center">
                        {{ opt.answer }}
                      </div>
                    </div>
        <!-- <button class="button">Click Here</button> -->
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
    }
  },
  methods: {
    flippit () {
      console.log('flippit')
      getAPI({
        method: 'get',
        headers: { Authorization: `Bearer ${access}` },
        url: '/api/flipcard/'
      })
        .then(response => {
          // this.$refs.cardfront.setAttribute('style', 'color: #5566f7;')
          this.myJson = JSON.parse(JSON.stringify(response.data))
          this.setQuestion(1)
        })
        .catch(error => console.log('Error', error.message))
    },
    setQuestion (e) {
      var index = 0
      if (e > -1) {
        index = e - 1
      } else {
        index = 0
      }
      // this.$refs.cardfront.setAttribute('style', 'color: #5566f7;')
      this.editingIndex = index
      this.question = JSON.parse(JSON.stringify(this.myJson[index]))

      store.commit({ type: 'setQuestion', payload: this.question })
      // index.commit({ type: 'setTestQuestion', payload: [] })
      // Question.setAnswerChecked()
      this.questNum = index + 1
      // this.flippclass = 'flippover'
      // this.position = 300
      // this.$refs.scrollArea.setScrollPosition(this.position, 200)

      // setTimeout(function () {
      //   this.$refs.cardfront.setAttribute('style', 'transform: color: #FFFFF; transition: color 800ms;')
      // }, 1200)
    },
    doSomething ({ evt, ...info }) {
      // this.$refs.cardfront.setAttribute('style', 'color: #5566f7;')
      evt.preventDefault()

      if (info.direction === 'left') {
        // console.log('spacebar')
        this.goLeft()
      } else if (info.direction === 'right') {
        // console.log('right')
        this.goRight()
      } else if (info.direction === 'up') {
        // console.log('top')
        this.goUp()
      } else if (info.direction === 'down') {
        // console.log('down')
        this.goDown()
      }
    },
    keyprocess (e) {
      // this.$refs.cardfront.setAttribute('style', 'color: #5566f7;')
      e.preventDefault()

      if (e.keyCode === 32) {
        // console.log('spacebar')
        this.toggleCard()
      } else if (e.keyCode === 39) {
        // console.log('right')
        this.goRight()
      } else if (e.keyCode === 38) {
        // console.log('top')
        this.goUp()
      } else if (e.keyCode === 37) {
        // console.log('left')
        this.goLeft()
      } else if (e.keyCode === 40) {
        // console.log('down')
        this.goDown()
      } else {

      }
    },
    goLeft () {
      console.log('goLeft')
      this.$refs.cardfront.setAttribute('style', 'color: #5566f7;')
      this.$refs.cardholder.setAttribute('style', 'transform: rotateY(5deg); left: -600px; opacity: 0.01; transition: 600ms linear;')
      this.reset(this.$refs.cardholder)
    },
    goRight () {
      console.log('goRight')
      this.$refs.cardholder.setAttribute('style', 'transform: rotateY(5deg); right: -600px; opacity: 0.01; transition: 600ms linear;')
      this.reset(this.$refs.cardholder)
    },
    goUp () {
      console.log('goUp')
      this.$refs.cardholder.setAttribute('style', 'transform: rotateY(0deg); top: -600px; opacity: 0.01; transition: 600ms linear;')
      this.reset(this.$refs.cardholder)
    },
    goDown () {
      console.log('goDown')
      this.$refs.cardholder.setAttribute('style', 'transform: rotateY(0deg); bottom: -600px; opacity: 0.01; transition: 600ms linear;')
      this.reset(this.$refs.cardholder)
    },
    toggleCard () {
      console.log('toggleCard')
      // console.log(this.$refs.cardholder)
      if (this.flipped) {
        this.$refs.cardfront.setAttribute('style', 'transform: rotateY(0deg);')
        this.$refs.cardback.setAttribute('style', 'transform: rotateY(-180deg)')
      } else {
        this.$refs.cardback.setAttribute('style', 'transform: rotateY(0deg)')
        this.$refs.cardfront.setAttribute('style', 'transform: rotateY(180deg);')
      }
      this.flipped = !this.flipped
    },
    reset (f) {
      var frontur = this.$refs.cardfront
      var bak = this.$refs.cardback
      this.$refs.cardfront.setAttribute('style', 'color: #5566f7;')

      setTimeout(function () {
        frontur.setAttribute('style', 'transform: rotateY(0deg)')
        bak.setAttribute('style', 'transform: rotateY(-180deg)')
        f.setAttribute('style', 'transform: rotateY(0deg); bottom: 0; left: 0; opacity: 1; transition: opacity 800ms;')
        this.$refs.cardfront.setAttribute('style', 'transform: color: #FFFFF; transition: color 800ms;')
      }, 1200)
      this.flippit()
    }
  },
  mounted () {
    this.flippit()
    window.addEventListener('keyup', this.keyprocess)
  },
  beforeDestroy () {
    clearTimeout(this.timer)
    window.removeEventListener('keyup', this.keyprocess)
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
      flipped: false,
      position: 0,
      frontside: true,
      // cardfront: this.$refs.cardfront,
      // cardback: this.$refs.cardback,
      cards: [
        {
          frontT: 'The "First Computer Programmer"',
          backT: 'Ada Lovelace',
          flipped: false
        },
        {
          frontT: 'Invented the "Clarke Calculator"',
          backT: 'Edith Clarke',
          flipped: false

        },
        {
          frontT: 'Famous World War II Enigma code breaker',
          backT: 'Alan Turing',
          flipped: false
        },
        {
          frontT: 'Created satellite orbit analyzation software for NASA',
          backT: 'Dr. Evelyn Boyd Granville',
          flipped: false
        }
      ]
    }
  }

}
// TODO Hreinsa currTestQuest á milli spurninga
</script>

<style scoped lang='scss'>
$primary: rgb(6, 2, 245);
$primary-light: rgb(82, 131, 247);

$secondary: rgb(187, 226, 78);

$red: hsl(10,80%,50%);
$orange: rgb(227, 230, 25);

*, *:before, *:after {
  box-sizing: border-box;
}

@mixin mobile ($size: 640px) {
  @media screen and (max-width: $size) {
    @content;
  }
}

.content {
  display: flex;
  margin: 0 0;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  max-width: 1000px;
}

.card {
  color: inherit;
  cursor: pointer;
  // width: calc(33% - 2rem);
  // min-width: calc(33% - 2rem);
  // height: 400px;
  width: 300px;
  height: 483px;
  // min-height: 400px;
  perspective: 1000px;
  margin: 0.02rem;
  position: relative;
  // @include mobile (800px) {
  //   width: 80%;
  // }
  // @include mobile (500px) {
  //   width: 100%;
  // }
}

.front,
.back {
  display: flex;
  border-radius: 6px;
  background-position: center;
  background-size: cover;
  text-align: center;
  justify-content: center;
  align-items: center;
  position: absolute;
  height: 100%;
  width: 100%;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  transform-style: preserve-3d;
  transition: all ease-in-out 600ms;
  // overflow: hidden;
}

.front {
  background-size: cover;
  background-blend-mode: overlay;
  padding: 2rem;
  font-size: 1.418rem;
  font-weight: 600;
  color: #fff;
  overflow: hidden;
  font-family: Poppins, sans-serif;
  &:before {
    position: absolute;
    display: block;
    content: '';
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(135deg,$primary-light, $primary);
    opacity: .85;
    z-index: -1;
  }
  // .card:hover & {
  //   transform: rotateY(180deg);
  // }
  // .card:nth-child(even):hover & {
  //   transform: rotateY(-180deg);
  // }
}

.back {
  background: rgb(208, 211, 206);
  transform: rotateY(-180deg);
  padding: 0 2em;
  font-weight: 600;
  font-size: 1.24rem;

  // .button {
  //   background: linear-gradient(135deg, adjust-hue($primary, -20deg), $primary);
  //   &:before {
  //     box-shadow: 0 0 10px 10px rgba($primary, 0.25);
  //   background-color: rgba($primary, 0.25);
  //   }
  // }
  // .card:hover & {
  //   transform: rotateY(0deg);
  // }
  .card:nth-child(even) & {
    transform: rotateY(180deg);
    .button {
    background: linear-gradient(135deg, adjust-hue($secondary, -20deg), $secondary);
    &:before {
      box-shadow: 0 0 10px 10px rgba($secondary, 0.25);
    background-color: rgba($secondary, 0.45);
    }
  }
  }
  }
</style>
