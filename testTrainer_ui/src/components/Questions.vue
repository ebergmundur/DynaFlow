<template>
    <div class="q-pa-md">
      <q-markup-table>
        <thead>
        <tr>
          <th class="text-left">Id</th>
          <th class="text-left">Spuring</th>
  <!--        <th class="text-right">Employee Salary</th>-->
  <!--        <th class="text-right">Employee Age</th>-->
  <!--        <th class="text-right">Profile Image</th>-->
  <!--        <th class="text-right">Delete</th>-->
        </tr>
        </thead>
        <tbody>
        <tr
          v-for="(data, index) in myJson"
          :key="index"
        >

          <td class="text-left">{{ data.id }}</td>
          <td class="text-left">
            <draggable
              ghost-class="ghost"
              @start="dragging = true"
              @end="dragging = false">
              <a
                href="javascript:void(0)"
                @click="setQuestion(data.id)"
              >{{ data.name }}</a>
            </draggable>
          </td>
  <!--        <td class="text-left">{{ index }}</td>-->
  <!--        <td class="text-left">{{ data.owner }}</td>-->
  <!--        <td class="text-left">{{ data.points }}</td>-->
  <!--        <td class="text-left">-->
  <!--          <q-btn-->
  <!--            flat-->
  <!--            icon="delete"-->
  <!--            color="negative"-->
  <!--            @click="deleteQuestion(index)"-->
  <!--          />-->
  <!--        </td>-->
        </tr>
        </tbody>
      </q-markup-table>
    </div>
<!--  <div>-->
<!--    <div class="row no-wrap justify-around q-px-md q-pt-md">-->
<!--      <div-->
<!--        v-mutation="handler1"-->
<!--        @dragenter="onDragEnter"-->
<!--        @dragleave="onDragLeave"-->
<!--        @dragover="onDragOver"-->
<!--        @drop="onDrop"-->
<!--        class="drop-target rounded-borders overflow-hidden"-->
<!--      >-->
<!--&lt;!&ndash;        <q-btn&ndash;&gt;-->
<!--&lt;!&ndash;          v-for="(question, index) in myJson"&ndash;&gt;-->
<!--&lt;!&ndash;          :key="index"&ndash;&gt;-->
<!--&lt;!&ndash;          id="question.id"&ndash;&gt;-->
<!--&lt;!&ndash;          draggable="true"&ndash;&gt;-->
<!--&lt;!&ndash;          @dragstart="onDragStart"&ndash;&gt;-->
<!--&lt;!&ndash;          :label='question.name'&ndash;&gt;-->
<!--&lt;!&ndash;          align="left"&ndash;&gt;-->
<!--&lt;!&ndash;          class="full-width "&ndash;&gt;-->
<!--&lt;!&ndash;      style="background: #99ccff; color: #4f4f4f; margin: 0 0 5px 0;"&ndash;&gt;-->
<!--&lt;!&ndash;        />&ndash;&gt;-->
<!--      </div>-->

<!--    </div>-->
<!--  </div>-->
</template>

<script>
import axios from 'axios'
import store from '../router/store'
import Question from './Question'
// import draggable from 'vuedraggable'
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
        Question.setAnswerChecked()
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
    axios('http://einars-macbook-pro.local:8000/api/questions/?format=json')
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
