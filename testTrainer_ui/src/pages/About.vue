<template>
  <q-page class="flex flex-center">
    <q-card flat class="pagecard">
      <q-toolbar class="q-dark">
        <q-toolbar-title>
          Um vefinn
        </q-toolbar-title>
      </q-toolbar>
      <q-cardsection v-for="block in rdata" :key="block.id">
        <div class="text-h4 q-pl-lg q-pt-lg q-pr-lg " v-html="block.name"></div>
        <div  class="q-pl-lg q-pr-lg " v-html="block.description"></div>
      </q-cardsection>
    </q-card>
  </q-page>
</template>

<script>
import { getAPI } from 'src/api/axios-base'
import store from 'src/store'

const access = store.getters.token || null

export default {
  data () {
    return {
      name: 'About',
      rdata: null
    }
  },
  beforeMount () {
    getAPI({
      url: '/api/about/',
      headers: { Authorization: `Bearer ${access}` },
      method: 'get'
    })
      .then(response => {
        console.log(response)
        this.rdata = JSON.parse(JSON.stringify(response.data))

        console.log(this.rdata)
      })
      .catch(error => console.log('Error', error.message))
  }
}
</script>

<style scoped></style>
