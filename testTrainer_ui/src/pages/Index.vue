<template>
  <q-page class="">
    <!--    <div class="row q-pa-md">-->
    <div class="flex row">
      <q-carousel
        v-model="slide"
        transition-prev="slide-right"
        transition-next="slide-left"
        autoplay="autoplay"
        infinite
        @mouseenter="autoplay = 0"
        @mouseleave="autoplay = 3500"
        swipeable
        animated
        control-color="primary"
        padding
        height="40vh"
        arrows
        class="carshadow col-12"
      >
        <q-carousel-slide
          v-for="t in topCards"
          :key="t.id"
          :name="t.order"
          class="flex flex-center cslide"
          >
          <div class="q-mt-md text-center q-pa-md">
            <img
              alt="Enám logo"
              src="../assets/DokktNam.png"
              style="height: 15vh; width: auto; alignment: left; float: none; margin: 0 0 0 0;"
            />
            <div class="text-h3 text-center" v-html="t.name" ></div>
            <div style="max-width: 600px;">
              <p class="splashtext"  v-html="t.description">
              </p>
            </div>
          </div>
        </q-carousel-slide>
      </q-carousel>

      <div class="row q-gutter-md justify-center col q-mt-md flex col-12">

        <q-card
          v-for="c in boxCards"
          :key="c.id"
          class="col-lg-2 col-md-4 col-sm-10">
            <q-item clickable class="flex-center" :to="c.urlpath">
          <q-card-section class="text-center">
            <!-- <a href="/#/dashboard/allt" class="iconlink dark"> -->
              <q-icon :name="c.icon_code" size="12vh" />
            <!-- </a> -->
            <div class="text-h6">{{c.name}}</div>
            <!-- <div class="text-subtitle2">0% lokið {{c.icon_code}}</div> -->
          </q-card-section>
            </q-item>
          <q-card-section class="q-pt-none text-justify" v-html="c.description">

          </q-card-section>
        </q-card>

      </div>
    </div>
    <br />
  </q-page>
</template>

<script>
// import Footer from 'components/Footer'
import { getAPI } from 'src/api/axios-base'
import store from 'src/store'

const access = store.getters.token || null

export default {
  data () {
    return {
      name: 'Index',
      slide: 0,
      autoplay: 5500,
      topCards: [],
      boxCards: [],
      lorem:
        'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Itaque voluptatem totam, architecto cupiditate officia rerum, error dignissimos praesentium libero ab nemo.'
    }
  },
  // components: {
  //   // Footer
  // },
  // methods: {},
  // created () {
  //   // this.$q.dark.set(true)
  // },
  beforeMount () {
    getAPI({
      url: '/api/indexcards/',
      headers: { Authorization: `Bearer ${access}` },
      method: 'get'
    })
      .then(response => {
        const rdata = JSON.parse(JSON.stringify(response.data))
        console.log('rdata')
        // console.log(rdata)

        var i = 0
        for (i = 0; i < rdata.length; i++) {
          // console.log(this.myJson.question_collection[i].name)
          if (rdata[i].spot === 1) {
            this.topCards.push(rdata[i])
          } else if (rdata[i].spot === 2) {
            this.boxCards.push(rdata[i])
          }
        }
        console.log(this.topCards)
      })
      .catch(error => console.log('Error', error.message))
  }
}
</script>

<style lang="sass" scoped>
// .logo-card
  // background-color: #ffffff
  // color: whitesmoke

// .logo-card h3
//   font-weight: bolder
.carshadow
  box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.2), 0 3px 5px 0 rgba(0, 0, 0, 0.1)

.card-icon
  opacity: 0.7
  // color: #271ce0
  // color: #6d91b7

.ebbg-primary
  background: linear-gradient(to right, $primary, $secondary)
  min-height: 500px
  color: #f3f3f3

.splashtext
  font-size: large

.iconlink
  color: #8b8989
  text-decoration: none
  :hover
    opacity: 0.6

.iconlink--dark
  color: white

.cslide
  min-width: 100%
  flex-wrap: nowrap
</style>
