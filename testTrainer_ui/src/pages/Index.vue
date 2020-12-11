<template>
  <q-page class="justify-center">
    <div class="q-pa-lg-md q-mt-md">
      <div class="row q-gutter-md justify-center col">
        <q-card class="logo-card col-lg-8 q-pa-md col-md-8 col-sm-10 ">
          <q-card-section>
            <img
              alt="Enám logo"
              src="../assets/enam-logo.svg"
              style="height: 160px; width: auto; alignment: left; float: left;">
            <div class="text-h3 q-pa-xl text-center">Velkomin á E-náms vefinn</div>
          </q-card-section>
        </q-card>
      </div>
      <q-separator class="q-ma-md"/>

      <div class="row justify-center col-lg-8 q-gutter-md ">

          <q-card class="top-card col-lg-4 col-md-8 col-sm-10">
            <q-card-section>
              <div class="text-h5">Velkomin</div>
            </q-card-section>
            <q-card-section class="q-pt-none wrap">
              E-nám er vettvangur þar sem nemendur geta æft sig fyrir próf.
              Dustaðu rykið af þekkingu þinni og spreyttu þig á stuttum æfingum eða heilum prófum.
              Flettikort þjálfa minnið og hraða.

            </q-card-section>
          </q-card>

          <q-card class="top-card col-lg-4 col-md-8 col-sm-10">
            <q-card-section>
              <div class="text-h5">Leiðbeiningar</div>
            </q-card-section>
            <q-card-section class="q-pt-none wrap">
              Búðu til æfingapróf af heppilegri lengd, getur valið fjölda spurninga í hverjum efnisflokk fyrir sig svo æfingin henti þér á þínum stað í náminu.
              Próf eru af fullri lengd og ekki hægt að gera hlé, svo það er ráðlegt að hafa tímann fyrir sér þegar sú leið er valin.
            </q-card-section>
          </q-card>
      </div>

      <q-separator class="q-ma-md"/>

      <div class="row q-gutter-md justify-center col-lg-8  q-px-lg col ">

        <q-card class="col-lg-2 col-md-4 col-sm-10 ">
          <q-card-section class="text-center">
            <q-icon name="class" size="160px" class="card-icon"/>
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
            <q-icon name="flip" size="160px" class="card-icon"/>
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
            <q-icon name="flaky" size="160px" class="card-icon"/>
            <div class="text-h6">Æfingar</div>
            <div class="text-subtitle2">14% lokið</div>
          </q-card-section>
          <q-card-section class="q-pt-none text-justify">
            Í æfingum getur þú sett saman tiltekinn fjölda spurninga úr þeim flokki eða flokkum sem þú vilt æfa þig í.
          </q-card-section>
        </q-card>

        <q-card class="col-lg-2  col-md-4 col-sm-10">
          <q-card-section class="text-center">
            <q-icon name="school" size="160px" class="card-icon"/>
            <div class="text-h6">Próf</div>
            <div class="text-subtitle2">4% lokið</div>
          </q-card-section>
          <q-card-section class="q-pt-none text-justify">
            Próf eru eins og vænta má með sama sniði og raunverulegt próf, spurningar úr öllum flokkum og skýr tímamörk.
          </q-card-section>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<script>
export default {
  data () {
    return {
      name: 'Index',
      lorem: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    }
  }
}
</script>

<style lang="sass" scoped>

.logo-card
  background-color: #335a73
  color: whitesmoke

.logo-card h3
  font-weight: bolder

.card-icon
  color: #6d91b7

</style>
