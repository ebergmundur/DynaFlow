<template>
  <!--MEMOS-->
  <q-dialog v-model="memolist" position="right">
    <q-card class="memowing">
      <q-card-section class="row items-center q-pb-none col-lg-8">
        <div class="text-h6">Minnismiðar</div>
        <q-space />
        <q-btn icon="close" flat round dense v-close-popup />
      </q-card-section>
      <q-card-section>
        <div class="q-pa-md items-start q-gutter-md col">
          <q-card
            flat
            bordered
            class="my-card bg-grey-1 scroll col"
            v-for="data in currentQuestion.memos"
            :key="data.id"
          >
            <q-card-section>
              <div class="row items-center no-wrap">
                <div class="col">
                  <div class="text-h6">
                    {{ formatDate(data.created_date) }}
                  </div>
                  <div>
                    <q-toggle
                      v-model="data.known"
                      label="Kann vel "
                      class="q-ma-sm"
                      disable
                    />
                    <!-- <q-toggle v-model="data.postpone" label="Geymd" class=" q-ma-sm" disable/> -->
                  </div>
                  <div class="text-subtitle2">
                    Þyngd: {{ data.difficulty }}
                    <q-linear-progress
                      size="14px"
                      :value="data.difficulty / 15"
                      color="red"
                      track-color="orange"
                      class="q-mt-sm"
                    />
                  </div>
                </div>
              </div>
              <div class="text-subtitle2 q-mt-sm">Minnistatriði</div>
              {{ data.memo }}
            </q-card-section>
          </q-card>
        </div>
      </q-card-section>
    </q-card>
  </q-dialog>
</template>
