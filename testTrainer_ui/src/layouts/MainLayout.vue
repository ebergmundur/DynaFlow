<template>
  <q-layout view="hHh lpR fFf">

    <q-header elevated class="bg-primary text-white" height-hint="98">
      <q-toolbar>
        <q-btn dense flat round icon="menu" @click="leftDrawer = !leftDrawer"/>

        <q-toolbar-title>
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo/svg/quasar-logo.svg">
          </q-avatar>
          E-nám
        </q-toolbar-title>

        <q-btn dense flat round icon="menu" @click="rightDrawer = !rightDrawer"/>
      </q-toolbar>

      <q-tabs align="left">
        <q-route-tab to="/" label="Heim"/>
        <q-route-tab to="/page2" label="Æfingar"/>
        <q-route-tab to="/page3" label="Þjálfun"/>
        <q-route-tab to="/page4" label="Próf"/>
        <q-route-tab to="/question" label="Annað"/>
      </q-tabs>
    </q-header>

    <q-drawer show-if-above v-model="leftDrawer" side="left" bordered>
      <!-- drawer content -->
<!--      <q-list>-->
        <q-item-label
          header
          class="text-grey-8"
        >
          Spurningar
        </q-item-label>
      <Questions></Questions>
<!--        <questionsset-->
<!--          v-for="link in essentialLinks"-->
<!--          :key="link.title"-->
<!--          v-bind="link"-->
<!--        />-->
<!--      </q-list>-->
    </q-drawer>

    <q-drawer show-if-above v-model="rightDrawer" side="right" bordered>
      <!-- drawer content -->
    </q-drawer>

    <q-page-container>
      <router-view/>
    </q-page-container>

    <q-footer bordered class="bg-grey-8 text-white">
      <q-toolbar>
        <q-toolbar-title>
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo/svg/quasar-logo.svg">
          </q-avatar>
          Eitthvað spennandi
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>

  </q-layout>
</template>

<script>
// export default {
//   data () {
//     return {
//       left: false,
//       right: false
//     }
//   }
// }

// import EssentialLink from 'components/EssentialLink.vue'
import Questions from '../components/Questions.vue'

// const linksData = [
//   {
//     title: 'Docs',
//     caption: 'quasar.dev',
//     icon: 'school',
//     link: 'https://quasar.dev'
//   },
//   {
//     title: 'Github',
//     caption: 'github.com/quasarframework',
//     icon: 'code',
//     link: 'https://github.com/quasarframework'
//   },
//   {
//     title: 'Discord Chat Channel',
//     caption: 'chat.quasar.dev',
//     icon: 'chat',
//     link: 'https://chat.quasar.dev'
//   },
//   {
//     title: 'Forum',
//     caption: 'forum.quasar.dev',
//     icon: 'record_voice_over',
//     link: 'https://forum.quasar.dev'
//   },
//   {
//     title: 'Twitter',
//     caption: '@quasarframework',
//     icon: 'rss_feed',
//     link: 'https://twitter.quasar.dev'
//   },
//   {
//     title: 'Facebook',
//     caption: '@QuasarFramework',
//     icon: 'public',
//     link: 'https://facebook.quasar.dev'
//   },
//   {
//     title: 'Quasar Awesome',
//     caption: 'Community Quasar projects',
//     icon: 'favorite',
//     link: 'https://awesome.quasar.dev'
//   }
// ]

export default {
  name: 'MainLayout',
  components: { Questions },
  data () {
    return {
      leftDrawer: true,
      rightDrawer: false
    }
  }
}
</script>
