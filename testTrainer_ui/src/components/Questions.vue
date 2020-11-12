<template>
  <div class="q-pa-md">
    <q-markup-table>
      <thead>
      <tr>
        <th class="text-left">Id</th>
        <th class="text-left">Spuring</th>
        <th class="text-right">Employee Salary</th>
        <th class="text-right">Employee Age</th>
        <th class="text-right">Profile Image</th>
        <th class="text-right">Delete</th>
      </tr>
      </thead>
      <tbody>
      <tr
        v-for="(data, index) in myJson"
        :key="index"
      >
        <td class="text-left">{{ data.id }}</td>
        <td class="text-left"><a
          href="javascript:void(0)"
          @click="setQuestion(data.id)"
        >{{ data.name }}</a></td>
        <td class="text-left">{{ index }}</td>
        <td class="text-left">{{ data.owner }}</td>
        <td class="text-left">{{ data.points }}</td>
        <td class="text-left">
          <q-btn
            flat
            icon="delete"
            color="negative"
            @click="deleteQuestion(index)"
          />
        </td>
      </tr>
      </tbody>
    </q-markup-table>
  </div>
</template>

<script>
import axios from 'axios'
import store from '../router/store'
// import { mapState } from 'vuex'
export default {
  data () {
    return {
      name: 'Questions',
      leftDrawerOpen: false,
      myJson: null,
      editModal: false,
      question: null,
      editingIndex: null,
      test: []
    }
  },
  methods: {
    setQuestion (id) {
      var index = this.myJson.findIndex(e => e.id === id)
      if (index > -1) {
        this.editingIndex = index
        this.question = JSON.parse(JSON.stringify(this.myJson[index]))
        store.commit({ type: 'setQuestion', payload: this.question })
        // store.commit({ type: 'setTestQuestion', payload: [] })
      } else {
        console.log('Ekki spurning')
      }
    },
    deleteQuestion (id) {
      this.$q.dialog({
        title: 'Confirm',
        message: 'Would you really like to delete?',
        cancel: true,
        persistent: true
      }).onOk(() => {
        var index = this.myJson.findIndex(e => e.id === id)
        if (index > -1) {
          this.myJson.splice(index, 1)
        }
      })
    },
    editQuestion (id) {
      var index = this.myJson.findIndex(e => e.id === id)
      if (index > -1) {
        this.editingIndex = index
        this.question = JSON.parse(JSON.stringify(this.myJson[index]))
        console.log(this.question)
        this.editModal = true
      } else {
        console.log('something went wrong')
      }
    },
    cancelEditQuestion () {
      this.employee = null
      this.editingIndex = null
    },
    saveQuestion () {
      this.myJson[this.editingIndex] = JSON.parse(JSON.stringify(this.employee))
      this.editModal = false
    }
  },
  mounted () {
    axios('http://localhost:8000/api/questions/?format=json')
      .then(response => {
        this.myJson = JSON.parse(JSON.stringify(response.data))
      })
      .catch(error => console.log('Error', error.message))
    // this.myJson = JSON.parse(JSON.stringify(json))
  }
}
// console.log(data)

</script>

<style scoped>

</style>
