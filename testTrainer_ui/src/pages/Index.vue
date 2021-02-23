<template>
  <q-page class="">
    <!--    <div class="row q-pa-md">-->
    <div class="flex row">

      <q-carousel
        v-model="slide"
        transition-prev="slide-right"
        transition-next="slide-left"
        :autoplay="autoplay"
        infinite
        @mouseenter="autoplay = 0"
        @mouseleave="autoplay = 5500"
        swipeable
        animated
        control-color="primary"
        control-type="flat"
        navigation
        padding
        height="500px"
        arrows
        class="carshadow col-12"
      >

        <q-carousel-slide
          name="welcome"
          class="flex flex-center cslide"
        >
          <div class="q-mt-md text-center">
            <img
              alt="Enám logo"
              src="../assets/DokktNam.svg"
              style="height: 140px; width: auto; alignment: left; float: none; margin: 0 0 0 0;"
            >
            <div class="text-h3 text-center">Velkomin á e-nám</div>
            <div style="max-width: 600px;">
              <p></p>
              <p class="splashtext">E-nám er vettvangur þar sem nemendur geta æft sig fyrir próf.</p>
            </div>
          </div>
        </q-carousel-slide>

        <q-carousel-slide
          name="welcome2"
          class="flex flex-center cslide"
        >
          <div class="q-mt-md text-center">
            <img
              alt="Enám logo"
              src="../assets/DokktNam.svg"
              style="height: 140px; width: auto; alignment: left; float: none; margin: 0 0 0 0;"
            >
            <div class="text-h3 text-center">Velkomin á e-nám</div>
            <div style="max-width: 600px;">
              <p></p>
              <p class="splashtext">Dustaðu rykið af þekkingu þinni og spreyttu þig á stuttum æfingum eða heilum prófum.
                Flettikort þjálfa minnið og hraða.</p>
            </div>
          </div>
        </q-carousel-slide>
        <q-carousel-slide
          name="welcome3"
          class="column no-wrap flex-center cslide"
        >
          <div class="q-mt-md text-center">
            <img
              alt="Enám logo"
              src="../assets/DokktNam.svg"
              style="height: 140px; width: auto; alignment: left; float: none; margin: 0 0 0 0;"
            >
            <div class="text-h3 text-center">Velkomin á e-nám</div>
            <div style="max-width: 600px;">
              <p></p>

              <p class="splashtext"> Búðu til æfingapróf af heppilegri lengd, getur valið fjölda spurninga í hverjum efnisflokk fyrir sig
                svo
                æfingin henti þér á þínum stað í náminu.</p>
            </div>
          </div>
        </q-carousel-slide>
        <q-carousel-slide
          name="welcome4"
          class="column no-wrap flex-center cslide"
        >
          <div class="q-mt-md text-center">
            <img
              alt="Enám logo"
              src="../assets/DokktNam.svg"
              style="height: 140px; width: auto; alignment: left; float: none; margin: 0 0 0 0;"
            >
            <div class="text-h3 text-center">Velkomin á e-nám</div>
            <div style="max-width: 600px;">
             <p></p>
              <p class="splashtext">
                Próf eru af fullri lengd og ekki hægt að gera hlé, svo það er ráðlegt að hafa tímann fyrir sér þegar sú
                leið er valin.</p>
            </div>
          </div>
        </q-carousel-slide>

        <q-carousel-slide
          name="style"
          class="column no-wrap flex-center cslide"
        >
          <q-icon
            name="class"
            size="124px"
          />
          <div class="q-mt-md text-center">
            <div class="text-h6">Mælaborð</div>
            <div style="max-width: 600px;">
              <p class="splashtext">
                Yfirlit yfir árangur í æfingum og prófum. Hægt að skoða eftir efnisflokkum líka.
                Svo getur þú farið yfir minnisatriði við spurningar og skoðað betur.
              </p>
            </div>
          </div>
        </q-carousel-slide>

        <q-carousel-slide
          name="flip"
          class="column no-wrap flex-center cslide"
        >
          <q-icon
            name="flip"
            size="124px"
          />
          <div class="q-mt-md text-center">
            <div class="text-h6">Flettikort</div>
            <div style="max-width: 600px;">
              <p class="splashtext">

                Spurningar af handahófi, svarmöguleikar ekki sýndir strax til að þjálfa hugann án stuðnings. Gefið
                rétt/rangt engin tímamörk en hægt að sjá fjölda svara og tíma sem lota tók.
              </p>
            </div>
          </div>
        </q-carousel-slide>

        <q-carousel-slide
          name="layers"
          class="column no-wrap flex-center cslide"
        >
          <q-icon
            name="flaky"
            size="124px"
          />
          <div class="q-mt-md text-center">
            <!--             <q-icon name="flaky" size="160px" class="card-icon"/>-->
            <div class="text-h6">Æfingar</div>
            <div style="max-width: 600px;">
              <p class="splashtext">

                Í æfingum getur þú sett saman tiltekinn fjölda spurninga úr þeim flokki eða flokkum sem þú vilt æfa þig í.
              </p>
            </div>
          </div>
        </q-carousel-slide>

        <q-carousel-slide
          name="map"
          class="column no-wrap flex-center cslide"
        >
          <q-icon
            name="school"
            size="124px"
          />
          <div class="q-mt-md text-center">
            <!--            <q-icon name="school" size="160px" class="card-icon"/>-->
            <div class="text-h6">Próf</div>
            <div style="max-width: 600px;">
              <p class="splashtext">
                Próf eru eins og vænta má með sama sniði og raunverulegt próf, spurningar úr öllum flokkum og skýr
                tímamörk.
              </p>
            </div>
          </div>
        </q-carousel-slide>

      </q-carousel>

      <div class="row q-gutter-md justify-center col q-mt-md flex col-12">
        <q-card class="col-lg-2 col-md-4 col-sm-10 ">
          <q-card-section class="text-center">
          <a href="/#/dashboard/allt" class="iconlink">
            <q-icon
              name="class"
              size="160px"
              class="card-icon"
            /></a>
            <div class="text-h6">Mælaborð</div>
            <div class="text-subtitle2">0% lokið</div>
          </q-card-section>
          <q-card-section class="q-pt-none text-justify">
            Yfirlit yfir árangur í æfingum og prófum. Hægt að skoða eftir efnisflokkum líka.
            Svo getur þú farið yfir minnisatriði við spurningar og skoðað betur.
          </q-card-section>
        </q-card>

        <q-card class="col-lg-2 col-md-4 col-sm-10">
          <q-card-section class="text-center">
            <a href="/#/flipcard" class="iconlink"><q-icon
              name="flip"
              size="160px"
              class="card-icon"
            /></a>
            <div class="text-h6">Flettikort</div>
            <div class="text-subtitle2">14% lokið</div>
          </q-card-section>
          <q-card-section class="q-pt-none text-justify">
            Spurningar af handahófi, svarmöguleikar ekki sýndir strax til að þjálfa hugann án stuðnings. Gefið
            rétt/rangt engin tímamörk en hægt að sjá fjölda svara og tíma sem lota tók.
          </q-card-section>
        </q-card>

        <q-card class="col-lg-2 col-md-4 col-sm-10">
          <q-card-section class="text-center">
            <a href="/#/createtest" class="iconlink"><q-icon
              name="flaky"
              size="160px"
              class="card-icon"
            /></a>
            <div class="text-h6">Æfingar</div>
            <div class="text-subtitle2">14% lokið</div>
          </q-card-section>
          <q-card-section class="q-pt-none text-justify">
            Í æfingum getur þú sett saman tiltekinn fjölda spurninga úr þeim flokki eða flokkum sem þú vilt æfa þig í.
          </q-card-section>
        </q-card>

        <q-card class="col-lg-2  col-md-4 col-sm-10">
          <q-card-section class="text-center">
            <a href="/#/testreal" class="iconlink"><q-icon
              name="school"
              size="160px"
              class="card-icon"
            /></a>
            <div class="text-h6">Próf</div>
            <div class="text-subtitle2">4% lokið</div>
          </q-card-section>
          <q-card-section class="q-pt-none text-justify">
            Próf eru eins og vænta má með sama sniði og raunverulegt próf, spurningar úr öllum flokkum og skýr tímamörk.
          </q-card-section>
        </q-card>
      </div>

      <!--      <q-separator class="q-ma-md"/>-->

      <!--      <div class="row q-gutter-md justify-center col-lg-8  q-px-lg col ">-->

      <!--        <q-card class="col-lg-2 col-md-4 col-sm-10 ">-->
      <!--          <q-card-section class="text-center">-->
      <!--            <q-icon name="class" size="160px" class="card-icon"/>-->
      <!--            <div class="text-h6">Mælaborð</div>-->
      <!--            <div class="text-subtitle2">0% lokið</div>-->
      <!--          </q-card-section>-->
      <!--          <q-card-section class="q-pt-none text-justify">-->
      <!--            Yfirlit yfir árangur í æfingum og prófum. Hægt að skoða eftir efnisflokkum líka.-->
      <!--            Svo getur þú farið yfir minnisatriði við spurningar og skoðað betur.-->
      <!--          </q-card-section>-->
      <!--        </q-card>-->

      <!--        <q-card class="col-lg-2 col-md-4 col-sm-10">-->
      <!--          <q-card-section class="text-center">-->
      <!--            <q-icon name="flip" size="160px" class="card-icon"/>-->
      <!--            <div class="text-h6">Flettikort</div>-->
      <!--            <div class="text-subtitle2">14% lokið</div>-->
      <!--          </q-card-section>-->
      <!--          <q-card-section class="q-pt-none text-justify">-->
      <!--            Spurningar af handahófi, svarmöguleikar ekki sýndir strax til að þjálfa hugann án stuðnings. Gefið-->
      <!--            rétt/rangt engin tímamörk en hægt að sjá fjölda svara og tíma sem lota tók.-->
      <!--          </q-card-section>-->
      <!--        </q-card>-->

      <!--        <q-card class="col-lg-2 col-md-4 col-sm-10">-->
      <!--          <q-card-section class="text-center">-->
      <!--            <q-icon name="flaky" size="160px" class="card-icon"/>-->
      <!--            <div class="text-h6">Æfingar</div>-->
      <!--            <div class="text-subtitle2">14% lokið</div>-->
      <!--          </q-card-section>-->
      <!--          <q-card-section class="q-pt-none text-justify">-->
      <!--            Í æfingum getur þú sett saman tiltekinn fjölda spurninga úr þeim flokki eða flokkum sem þú vilt æfa þig í.-->
      <!--          </q-card-section>-->
      <!--        </q-card>-->

      <!--        <q-card class="col-lg-2  col-md-4 col-sm-10">-->
      <!--          <q-card-section class="text-center">-->
      <!--            <q-icon name="school" size="160px" class="card-icon"/>-->
      <!--            <div class="text-h6">Próf</div>-->
      <!--            <div class="text-subtitle2">4% lokið</div>-->
      <!--          </q-card-section>-->
      <!--          <q-card-section class="q-pt-none text-justify">-->
      <!--            Próf eru eins og vænta má með sama sniði og raunverulegt próf, spurningar úr öllum flokkum og skýr tímamörk.-->
      <!--          </q-card-section>-->
      <!--        </q-card>-->
      <!--      </div>-->
    </div>
    <!--    </div>-->
    <br>
    <!-- <Footer></Footer> -->

  </q-page>
</template>

<script>
// import Footer from 'components/Footer'
export default {
  data () {
    return {
      name: 'Index',
      slide: 'welcome',
      autoplay: 5500,
      lorem: 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Itaque voluptatem totam, architecto cupiditate officia rerum, error dignissimos praesentium libero ab nemo.'
    }
  },
  components: {
    // Footer
  },
  methods: {
  },
  created () {
    // this.$q.dark.set(true)
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
  opacity: 0.8
  // color: #271ce0
  // color: #6d91b7

.ebbg-primary
  background: linear-gradient(to right, $primary, $secondary)
  min-height: 500px
  color: #f3f3f3

.splashtext
  font-size: large

.iconlink
  color: black
  text-decoration: none
  :hover
    opacity: 0.6

.cslide
  min-width: 100%
  flex-wrap: nowrap
</style>
