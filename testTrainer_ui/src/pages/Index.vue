<template>
  <q-page class="flex flex-center" style="background-color: #d0d0d0">
    <div class="row q-gutter-md justify-center">
      <q-card class="logo-card">
        <q-card-section>
          <img
            alt="Enám logo"
            src="../assets/enam-logo.svg"
          style="height: 160px; width: auto; alignment: left; float: left;">
<div class="text-h3 q-ma-xl text-center">Velkomin á E-náms vefinn</div>
        </q-card-section>
      </q-card>

      <q-separator class="q-ma-md"/>

        <q-card class="top-card">
        <q-card-section>
          <div class="text-h5">Velkomin</div>
        </q-card-section>
        <q-card-section class="q-pt-none">
          E-nám er vettvangur þar sem nemendur geta æft sig fyrir próf...

        </q-card-section>
      </q-card>

      <q-card class="top-card">
        <q-card-section>
          <div class="text-h5">Leiðbeiningar</div>
        </q-card-section>
        <q-card-section class="q-pt-none">
          Dustaðu rykið af þekkingu þinni og spreyttu þig á stuttum æfingum eða heilum prófum.

        </q-card-section>
      </q-card>
<!--    </div>-->

    <q-separator class="q-ma-md"/>

<!--    <div class="row q-gutter-md">-->
      <q-card class="my-card">
        <q-card-section>
          <q-icon name="class" size="210px" class="card-icon"/>
          <div class="text-h6">Námið</div>
          <div class="text-subtitle2">0% lokið</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          {{ lorem }}
        </q-card-section>
      </q-card>
      <q-card class="my-card">
        <q-card-section>
          <q-icon name="flaky" size="210px" class="card-icon"/>
          <div class="text-h6">Æfingar</div>
          <div class="text-subtitle2">14% lokið</div>
        </q-card-section>
        <q-card-section class="q-pt-none">
          {{ lorem }}
        </q-card-section>
      </q-card>
      <q-card class="my-card">
        <q-card-section>
          <q-icon name="school" size="210px" class="card-icon"/>
          <div class="text-h6">Próf</div>
          <div class="text-subtitle2">4% lokið</div>
        </q-card-section>
        <q-card-section class="q-pt-none">
          {{ lorem }}
        </q-card-section>
      </q-card>
    </div>
  </q-page>
</template>

<script>
export default {
  data () {
    return {
      name: 'PageIndex',
      lorem: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    }
  }
}
</script>

<style lang="sass" scoped>
.my-card
  width: 100%
  max-width: 315px
  text-align: center

.logo-card
  background-color: #335a73
  width: 100%
  max-width: 976px
  color: whitesmoke

.logo-card h3
    font-weight: bolder

.card-icon
  color: #6d91b7

.top-card
  width: 100%
  text-align: justify
  max-width: 480px
</style>
