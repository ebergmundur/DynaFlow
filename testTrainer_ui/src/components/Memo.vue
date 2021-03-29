<template>
  <q-dialog v-model="memo">
    <q-card>
      <q-toolbar>
        <q-avatar>
          <img src="../assets/enam-logo.svg" />
        </q-avatar>

        <q-toolbar-title>
          <span class="text-weight-bold">E-nám</span>
          minnismiðar
        </q-toolbar-title>

        <q-btn flat round dense icon="close" v-close-popup />
      </q-toolbar>

      <!--        style="max-height: 70vh; width: 30vw;"-->
      <q-card-section class="scroll">
        <h6 class="q-ma-sm">{{ currentQuestion.virtname }}</h6>
        <q-form @submit="onMemoSubmit" @reset="onMemoReset" class="q-gutter-md">
          <div class="q-pa-md q-ma-sm">
            Þyngd: {{ difficulty / 10 }}
            <q-slider v-model="difficulty" :step="10" />
          </div>

          <div class="q-pa-md q-ma-xs">
            <q-input v-model="memotext" filled type="textarea" />
          </div>
          <q-toggle v-model="known" label="Kann vel " class="q-ma-sm" />
          <div>
            <q-btn label="Skrá" type="submit" color="primary" />
            <q-btn
              label="Hreinsa"
              type="reset"
              color="primary"
              flat
              class="q-ml-sm"
            />
          </div>
        </q-form>
      </q-card-section>
    </q-card>
  </q-dialog>
</template>
