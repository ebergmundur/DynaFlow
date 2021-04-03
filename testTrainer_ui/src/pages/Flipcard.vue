<template>
  <q-page class="flex flex-center" @keydown.native="keyprocess">
    <!-- @focusin.native="activateNavigation"
    @focusout.native="deactivateNavigation" -->

    <div
      class="content"
    >
      <div
        v-if="activeSession"
        class="card"
        ref="cardholder"
        v-on:click="toggleCard"
        v-touch-swipe.mouse.touch="doSomething"
      >
        <div class="front row q-pa-none " id="cardfrontID" ref="cardfront">
          <div class="q-pa-none flex flex-center non-selectable">
            {{ currentQuestion.question }}
          </div>
          <div style="position: absolute; bottom: 0; right: 10px; font-size: 0.9rem; font-weight: 100;">
            {{progressLabel}}
          </div>
        </div>
        <div class="back" id="cardbackID" ref="cardback">
          <div v-if="activeSession">
            <div
              v-for="opt in currentQuestion.options"
              :key="opt.id"
              class="col-12 q-pa-md scroll"
            >
              <div v-if="opt.correct" class="content-center non-selectable">
                {{ opt.answer }}
              </div>
            </div>
            <!-- <button class="button">Click Here</button> -->
          </div>
        </div>
      </div>
    </div>

    <q-dialog
      v-model="persistent"
      persistent
      full-height
      full-width
      transition-show="scale"
      transition-hide="scale"
      style="width: 90vw; height: 90vh"
    >
      <q-card>
        <q-toolbar class="bg-dark text-white">
          <q-avatar>
            <img src="../assets/enam-logo.svg" />
          </q-avatar>
          <q-toolbar-title>Fjöldi spurninga og fög:</q-toolbar-title>
        </q-toolbar>

        <q-card-section class="q-ma-lg">
          <!-- <q-input v-model="tot_count" label="Fjöldi" /> -->
          <!-- @input="setup_session" -->
          <q-input
          v-model="tot_count"
          type="number" label=""
          class="text-h4"
          :rules="[ val => val <= 50 || 'Hámark 50']"
          style="height: 80px; margin-top: -40px;"/>
          <q-slider
            v-model="tot_count"
            :min="0"
            color="primary"
            label
            :max="50"
            :step="5"
          />
          <!-- @input="setup_session" -->
          <!-- </q-field> -->
          <!-- <div v-if="!activeSession">
            <q-checkbox
              v-for="(data, index) in questions"
              :key="index"
              :value="data.id"
              :label="data.name"
              v-model="cats_count[index].use"
            />
          </div> -->
        </q-card-section>
        <q-card-section class="">
          <div class="row wrap q-gutter-md justify-evenly">
            <q-card
              v-for="(cat, index) in cats"
              :key="index"
              :value="cat.category.id"
              class="col-xs-12 col-sm-5 col-md-6 col-lg"
            >
              <q-toolbar class="q-dark text-center">
                  <q-checkbox
              v-model="cats_count[index].use"
              size="lg"
              dark
            />
                <q-toolbar-title >
                  {{ cat.category.name }}
                </q-toolbar-title>
            <q-checkbox
              size="lg"
              v-model="hideCheck"
              value=-1
              style="visibility: hidden;"
            />
              </q-toolbar>
               <q-item
               clickable
               class="flex-center"
               @click="cats_count[index].use = !cats_count[index].use"
               >
               <!-- :to="'/test/'+cat.category.id" -->
              <q-card-section class="text-center" >
               <!-- <q-item clickable class="flex-center" @click="catSelect(cat.id)"> -->
                <q-icon :name="cat.category.icon" size="8vh"  />
              </q-card-section>
                </q-item>
                <q-card-section class="text-center">
                <div  class="text-h5">
                 {{cat.answcount}} af {{cat.catcount}} lokið
                <q-linear-progress  rounded size="20px" :value="cat.answcount/cat.catcount" :class="cat.category.color_class" />
                </div>
                <div class="q-pt-none text-justify"  v-html="cat.category.description">
                </div>
              </q-card-section>

            </q-card>
          </div>
        </q-card-section>
        <q-separator></q-separator>
        <q-card-actions align="right" class="bg-white">
          <q-btn color="positive" label="Byrja" @click="setup_session" size="lg" />
        </q-card-actions>
      </q-card>
    </q-dialog>

    <q-dialog
      v-model="finale"
      transition-show="scale"
      transition-hide="scale"
      persistent
    >
      <q-card class="" style="width: 500px">
        <q-toolbar class="bg-dark text-white">
          <q-avatar>
            <img src="../assets/enam-logo.svg" />
          </q-avatar>
          <q-toolbar-title>Spjöldin eru búin.</q-toolbar-title>
        </q-toolbar>
        <q-card-section class="flex flex-center">
          <div class="row q-gutter-lg q-pa-md flex flex-center">
            <q-btn
              dense
              color="primary"
              size="lg"
              label="Skoða aftur"
              class="q-pa-sm col-xs-12 col-lg-3"
              @click="finale = false"
            />

            <q-btn
              dense
              color="primary"
              size="lg"
              label="Nýtt sett"
              class="q-pa-sm col-xs-12 col-lg-3"
              @click="newSet"
            />

            <q-btn
              dense
              color="primary"
              size="lg"
              label="Gott í bili"
              class="q-pa-sm col-xs-12 col-lg-3"
              to="/"
            />
          </div>
        </q-card-section>
      </q-card>
    </q-dialog>
  </q-page>
</template>

<script>
import store from 'src/store'
// import { date } from 'quasar'
import { getAPI } from 'src/api/axios-base'
// import axios from 'axios'

const access = store.getters.token // attempt to obtain new access token by running 'refreshToken' action

export default {
  name: 'Flipcard',
  data () {
    return {
      // currentOptions: this.currentQuestion.options,
      cQ: 0,
      navigationActive: false,
      // cancel: 0,
      tot_count: 5,
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
      persistent: true,
      cats_count: [],
      cats: [],
      hideCheck: true,
      qPerCat: 2,
      questions: [],
      question_count: 0,
      currentQnum: 0,
      currentQuestion: null,
      activeSession: false,
      progress: 0,
      finale: false,
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
  },
  computed: {
    progressLabel () {
      return this.currentQnum + 1 + '/' + this.questions.length
    }
  },
  methods: {
    flippit () {
      console.log('flippit')
      // getAPI({
      //   method: 'get',
      //   headers: { Authorization: `Bearer ${access}` },
      //   url: '/api/flipcard/'
      // })
      //   .then(response => {
      //     // this.$refs.cardfront.setAttribute('style', 'color: #5566f7;')
      //     this.questions = JSON.parse(JSON.stringify(response.data))
      //     this.setQuestion(1)
      //   })
      //   .catch(error => console.log('Error', error.message))
    },
    setup_session (e) {
      this.persistent = false

      getAPI({
        method: 'POST',
        headers: { Authorization: `Bearer ${access}` },
        data: {
          cats: this.cats_count,
          count: this.tot_count
        },
        url: '/api/flip/'
      })
        .then(response => {
          this.questions = JSON.parse(JSON.stringify(response.data))
          console.log(this.questions)
          this.setQuestion(0)
        })
        .catch(error => console.log('Error', error.message))
      console.log(this.cats_count)
      // console.log(this.qPerCat)
    },
    setQuestion (n) {
      this.currentQnum = this.currentQnum + Number(n)
      if (this.currentQnum <= 0 && this.activeSession) {
        this.currentQnum = 0
        // alert('fyrsta spjald')
      } else if (this.currentQnum >= this.questions.length) {
        this.currentQnum = this.questions.length
        this.finale = true
      } else {
        if (
          this.currentQnum <= this.questions.length &&
          this.currentQnum >= 0
        ) {
          // console.log('range ok')
          this.activeSession = true
          this.currentQuestion = this.questions[this.currentQnum]
          // console.log(this.currentQuestion)
          this.progress = (this.currentQnum + 1) / this.questions.length
        } else if (this.currentQnum > this.questions.length) {
          this.activeSession = false
          alert('Búið!')
        }
      }
    },
    doSomething ({ evt, ...info }) {
      // this.$refs.cardfront.setAttribute('style', 'color: #5566f7;')
      evt.preventDefault()

      if (info.direction === 'left') {
        this.goLeft()
      } else if (info.direction === 'right') {
        this.goRight()
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
        // this.goUp()
      } else if (e.keyCode === 37) {
        // console.log('left')
        this.goLeft()
      } else if (e.keyCode === 40) {
        // console.log('down')
        // this.goDown()
      } else if (e.keyCode === 13) {
        // console.log('down')
        this.setup_session()
      }
    },
    goLeft () {
      // goRight () {
      console.log('goLeft')
      // this.$refs.cardfront.setAttribute('style', 'color: #5566f7;')
      this.$refs.cardholder.setAttribute(
        'style',
        'left: -400px; opacity: 0.0; transition: 200ms ease-in-out;'
      )
      this.reset(this.$refs.cardholder)
      this.setQuestion(1)
    },
    // goLeft () {
    goRight () {
      console.log('goRight')
      this.$refs.cardholder.setAttribute(
        'style',
        'right: -400px; opacity: 0.0; transition: 200ms ease-in-out;'
      )
      this.reset(this.$refs.cardholder)
      this.setQuestion(-1)
    },
    // goUp () {
    //   console.log('goUp')
    //   this.$refs.cardholder.setAttribute('style', 'transform: rotateY(0deg); top: -600px; opacity: 0.01; transition: 600ms linear;')
    //   this.reset(this.$refs.cardholder)
    // },
    // goDown () {
    //   console.log('goDown')
    //   this.$refs.cardholder.setAttribute('style', 'transform: rotateY(0deg); bottom: -600px; opacity: 0.01; transition: 600ms linear;')
    //   this.reset(this.$refs.cardholder)
    // },
    toggleCard () {
      // console.log('toggleCard')
      // console.log(this.$refs.cardholder)
      if (this.flipped) {
        this.$refs.cardfront.setAttribute('style', 'transform: rotateY(0deg);')
        this.$refs.cardback.setAttribute(
          'style',
          'transform: rotateY(-180deg)'
        )
      } else {
        this.$refs.cardback.setAttribute('style', 'transform: rotateY(0deg)')
        this.$refs.cardfront.setAttribute(
          'style',
          'transform: rotateY(180deg);'
        )
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
        f.setAttribute(
          'style',
          'transform: rotateY(0deg); bottom: 0; left: 0; opacity: 1; transition: opacity 200ms ease-in-out;'
        )
        // this.$refs.cardfront.setAttribute('style', 'transform: color: #FFFFF; transition: color 800ms;')
      }, 200)
      // this.flippit()
    },
    newSet () {
      this.finale = false
      this.persistent = true
      // this.$router
      //   .push({ path: '/flipcard' })
      //   .catch(err => {
      //     console.log(err.message)
      //   })
    },
    pageSetUp () {
      const username = store.getters.getUserName
      getAPI({
        url: '/api/catstat/',
        method: 'post',
        data: {
          user: username,
          timed: true,
          time_allowed: 0
        },
        headers: { Authorization: `Bearer ${access}` }
      })
        .then(response => {
        // console.log(response)
          this.cats = JSON.parse(JSON.stringify(response.data))
          // console.log(this.cats)
          var i
          for (i = 0; i < this.cats.length; i++) {
            var cid = this.cats[i].category
            this.cats_count.push({ id: cid.id, use: true })
          // this.cats_count.push(false)
          }
        })
        .catch(error => console.log('Error', error.message))
    }
  },
  beforeMount () {
    // getAPI({
    //   url: '/api/category/',
    //   method: 'get',
    //   headers: { Authorization: `Bearer ${access}` }
    // })

    // this.questions = JSON.parse(JSON.stringify(json))
  },
  mounted () {
    // this.flippit()
    this.pageSetUp()
    window.addEventListener('keyup', this.keyprocess)
  },
  beforeDestroy () {
    clearTimeout(this.timer)
    window.removeEventListener('keyup', this.keyprocess)
  }
}
</script>

<style scoped lang="scss">
$primary: rgb(6, 2, 245);
$primary-light: rgb(82, 131, 247);

$secondary: rgb(187, 226, 78);

$red: hsl(10, 80%, 50%);
$orange: rgb(227, 230, 25);

*,
*:before,
*:after {
  box-sizing: border-box;
}

@mixin mobile($size: 640px) {
  @media screen and (max-width: $size) {
    @content;
  }
}

.content {
  display: flex;
  margin: 10px 0 0 0;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  // max-width: 1000px;
  width: 95vw;
  height: 90vh;
}

.card {
  color: inherit;
  cursor: pointer;
  // width: calc(33% - 2rem);
  // min-width: calc(33% - 2rem);
  // height: 400px;
  width: 100%;
  height: 100%;
  // min-height: 400px;
  perspective: 1000px;
  margin: 0.02rem;
  position: relative;
  @include mobile (900px) {
    height: 77vh;
    margin-top: 40px;
  }
  position: relative;
  @include mobile (800px) {
    height: 90vh;
    margin-top: 30px;
  }
  @include mobile (500px) {
    margin-top: 40px;
    height: 85vh;
  }
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
  transition: all ease-in-out 200ms;
  // overflow: hidden;
}

.front {
  background-size: cover;
  background-blend-mode: overlay;
  padding: 1rem;
  // font-size: 1.3rem;
  font-size: 4vh;
  font-weight: 600;
  color: #fff;
  overflow: hidden;
  font-family: Poppins, sans-serif;
  &:before {
    position: absolute;
    display: block;
    content: "";
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(135deg, $primary-light, $primary);
    opacity: 0.85;
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
  // padding: 0 2em;
  padding: 4rem;
  font-weight: 600;
  // font-size: 1.24rem;
  font-size: 4vh;

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
      background: linear-gradient(
        135deg,
        adjust-hue($secondary, -20deg),
        $secondary
      );
      &:before {
        box-shadow: 0 0 10px 10px rgba($secondary, 0.25);
        background-color: rgba($secondary, 0.45);
      }
    }
  }
}
</style>
