<template>
<!--        <q-btn-->
<!--          v-for="(question, index) in myJson"-->
<!--          :key="index"-->
<!--          id="question.id"-->
<!--          draggable="true"-->
<!--          @dragstart="onDragStart"-->
<!--          :label='question.name'-->
<!--          align="left"-->
<!--          class="full-width "-->
<!--      style="background: #99ccff; color: #4f4f4f; margin: 0 0 5px 0;"-->
<!--        />-->
  <div>
<!--    <div class="row no-wrap justify-around q-px-md q-pt-md">-->
    <q-btn label="hressa" @click="refresh"></q-btn>
    <section>
    <div class="">
      <div
        v-mutation="handler1"
        @dragenter="onDragEnter"
        @dragleave="onDragLeave"
        @dragover="onDragOver"
        @drop="onDrop"
        class="drop-target rounded-borders overflow-auto float-left"
      >

        <div
          v-for="(question, index) in myJson"
          :key="index"
          :id=question.id
          draggable="true"
          @dragstart="onDragStart"
          class="box enambox overflow-hidden"
        >
         {{index}} / {{ question.id}} <br> {{ question.name }}
        </div>

<!--        <div-->
<!--          id="box1"-->
<!--          draggable="true"-->
<!--          @dragstart="onDragStart"-->
<!--          class="box navy"-->
<!--        />-->
<!--        <div-->
<!--          id="box2"-->
<!--          draggable="true"-->
<!--          @dragstart="onDragStart"-->
<!--          class="box red"-->
<!--        />-->
<!--        <div-->
<!--          id="box3"-->
<!--          draggable="true"-->
<!--          @dragstart="onDragStart"-->
<!--          class="box green"-->
<!--        />-->
<!--        <div-->
<!--          id="box4"-->
<!--          draggable="true"-->
<!--          @dragstart="onDragStart"-->
<!--          class="box orange"-->
<!--        />-->
<!--        <div-->
<!--          id="box5"-->
<!--          draggable="true"-->
<!--          @dragstart="onDragStart"-->
<!--          class="box navy"-->
<!--        />-->
<!--        <div-->
<!--          id="box6"-->
<!--          draggable="true"-->
<!--          @dragstart="onDragStart"-->
<!--          class="box red"-->
<!--        />-->
<!--        <div-->
<!--          id="box7"-->
<!--          draggable="true"-->
<!--          @dragstart="onDragStart"-->
<!--          class="box green"-->
<!--        />-->
<!--        <div-->
<!--          id="box8"-->
<!--          draggable="true"-->
<!--          @dragstart="onDragStart"-->
<!--          class="box orange"-->
<!--        />-->
      </div>

      <div
        v-mutation="handler2"
        @dragenter="onDragEnter"
        @dragleave="onDragLeave"
        @dragover="onDragOver"
        @drop="onDrop"
        class="drop-target rounded-borders overflow-auto float-right"
      />
    </div>
    </section>
      <q-separator />
<!--    <section>-->
<!--    <div class="row justify-around items-start">-->
<!--      <div class="col row justify-center q-pa-md">-->
<!--        <div class="text-subtitle1">-->
<!--          Mutation Info-->
<!--        </div>-->
<!--        <div v-for="status in status1" :key="status">-->
<!--          {{ status }}-->
<!--        </div>-->
<!--      </div>-->

<!--      <div class="col row justify-center q-pa-md">-->
<!--        <div class="text-subtitle1">-->
<!--          Mutation Info-->
<!--        </div>-->
<!--        <div v-for="status in status2" :key="status">-->
<!--          {{ status }}-->
<!--        </div>-->
<!--      </div>-->
<!--    </div>-->
<!--    </section>-->
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      status1: [],
      status2: [],
      name: 'CollectQuestions',
      myJson: null
    }
  },

  methods: {
    handler1 (mutationRecords) {
      this.status1 = []
      for (const index in mutationRecords) {
        const record = mutationRecords[index]
        const info = `type: ${record.type}, nodes added: ${record.addedNodes.length > 0 ? 'true' : 'false'}, nodes removed: ${record.removedNodes.length > 0 ? 'true' : 'false'}, oldValue: ${record.oldValue}`
        this.status1.push(info)
      }
    },

    handler2 (mutationRecords) {
      this.status2 = []
      for (const index in mutationRecords) {
        const record = mutationRecords[index]
        const info = `type: ${record.type}, nodes added: ${record.addedNodes.length > 0 ? 'true' : 'false'}, nodes removed: ${record.removedNodes.length > 0 ? 'true' : 'false'}, oldValue: ${record.oldValue}`
        this.status2.push(info)
      }
    },

    // store the id of the draggable element
    onDragStart (e) {
      e.dataTransfer.setData('text', e.target.id)
      e.dataTransfer.dropEffect = 'move'
    },

    onDragEnter (e) {
      // don't drop on other draggables
      if (e.target.draggable !== true) {
        e.target.classList.add('drag-enter')
      }
    },

    onDragLeave (e) {
      e.target.classList.remove('drag-enter')
    },

    onDragOver (e) {
      e.preventDefault()
    },

    onDrop (e) {
      e.preventDefault()

      // don't drop on other draggables
      if (e.target.draggable === true) {
        return
      }

      const draggedId = e.dataTransfer.getData('text')
      const draggedEl = document.getElementById(draggedId)

      console.log(draggedId)
      console.log(draggedEl)

      // check if original parent node
      if (draggedEl.parentNode === e.target) {
        e.target.classList.remove('drag-enter')
        return
      }

      // make the exchange
      draggedEl.parentNode.removeChild(draggedEl)
      e.target.appendChild(draggedEl)
      e.target.classList.remove('drag-enter')
    },
    refresh () {
      this.myJson = null
      axios('http://localhost:8000/api/questions/?format=json')
        .then(response => {
          this.myJson = JSON.parse(JSON.stringify(response.data))
        })
        .catch(error => console.log('Error', error.message))
    // this.myJson = JSON.parse(JSON.stringify(json))
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
</script>

<style scoped lang="sass">
.drop-target
  height: 70vh
  width: 400px
  min-width: 200px
  margin: 50px
  background-color: gainsboro

.drag-enter
  outline-style: dashed

.box
  width: 97%
  height: 100px
  float: none
  cursor: pointer
  color: black
  margin: 5px
  padding: 10px
  font-size: large

@media only screen and (max-width: 500px)
  .drop-target
    height: 200px
    width: 100px
    min-width: 100px
    background-color: gainsboro

  .box
    width: 50px
    height: 50px

.box:nth-child(3)
  clear: both

.enambox
  background-color: #99ccff
.navy
  background-color: navy

.red
  background-color: firebrick

.green
  background-color: darkgreen

.orange
  background-color: orange
</style>
