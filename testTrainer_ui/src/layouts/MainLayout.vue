<template>
  <q-layout view="hHh lpR fFf">

    <q-header elevated class="bg-primary text-white row" height-hint="98">
      <!--      <q-toolbar>-->
      <!--        <q-btn dense flat round icon="menu" @click="leftDrawer = !leftDrawer"/>-->

      <!--        <q-toolbar-title>-->
      <!--          <q-avatar>-->
      <!--&lt;!&ndash;            <img src="https://cdn.quasar.dev/logo/svg/quasar-logo.svg">&ndash;&gt;-->
      <!--            <img src="../assets/enam-logo.svg">-->
      <!--          </q-avatar>-->
      <!--        </q-toolbar-title>-->

      <!--        <q-btn dense flat round icon="menu" @click="rightDrawer = !rightDrawer"/>-->
      <!--      </q-toolbar>-->

      <q-tabs align="left" class="col-lg">

        <q-route-tab to="/" label="">
          <q-avatar class="q-ma-md">
            <!--            <img src="https://cdn.quasar.dev/logo/svg/quasar-logo.svg">-->
            <img src="../assets/enam-logo.svg">
          </q-avatar>
        </q-route-tab>
        <q-route-tab to="/createtest" label="Æfingar"/>
        <!--        <q-btn-dropdown auto-close stretch flat label="Æfingar">-->
        <!--          <q-list>-->
        <!--            <q-route-tab to="/createtest" label="Búa til æfingapróf"/>-->
        <!--&lt;!&ndash;            <q-item clickable @click="tab = 'movies'">&ndash;&gt;-->
        <!--&lt;!&ndash;              <q-item-section>Búa til æfingapróf</q-item-section>&ndash;&gt;-->
        <!--&lt;!&ndash;            </q-item>&ndash;&gt;-->

        <!--&lt;!&ndash;            <q-item clickable @click="tab = 'photos'">&ndash;&gt;-->
        <!--&lt;!&ndash;              <q-item-section>Skoða tekin próf</q-item-section>&ndash;&gt;-->
        <!--&lt;!&ndash;            </q-item>&ndash;&gt;-->
        <!--          </q-list>-->
        <!--        </q-btn-dropdown>-->
        <q-route-tab to="/testpractice" label="Æfing"/>
        <q-route-tab to="/testreal" label="Próf"/>
        <q-route-tab to="/review" label="Niðurstöður"/>
        <q-route-tab to="/flipcard" label="Flettikort"/>
        <q-route-tab to="/dashboard" label="Mælaborð"/>
      </q-tabs>
      <!--      <q-tabs-->
      <!--        class="col-1"-->
      <!--        style="border: 1px solid greenyellow;"-->
      <!--      >-->

      <div style="margin-right: 200px; margin-top: 20px;">

                    <h5>//{{authenticated}}//</h5>
<!--      <button-->
<!--        class="btn btn-primary btn-margin"-->
<!--        v-if="!authenticated"-->
<!--        @click="login()">-->
<!--        Log In-->
<!--      </button>-->

<!--      <button-->
<!--        class="btn btn-primary btn-margin"-->
<!--      v-if="authenticated"-->
<!--        @click="privateMessage()">-->
<!--        Call Private-->
<!--      </button>-->

<!--      <button-->
<!--        class="btn btn-primary btn-margin"-->
<!--        v-if="!authenticated"-->
<!--        @click="logout()">-->
<!--        Log Out-->
<!--      </button>-->
<!--      {{ message }}-->
<!--      <br>-->
        </div>
      <clock></clock>
      <!--      </q-tabs>-->

    </q-header>

    <!--    <q-drawer show-if-above v-model="leftDrawer" side="left" bordered>-->
    <!-- drawer content -->
    <!--      <q-list>-->
    <!--        <q-item-label-->
    <!--          header-->
    <!--          class="text-grey-8"-->
    <!--        >-->
    <!--          Spurningar-->
    <!--        </q-item-label>-->
    <!--&lt;!&ndash;      <Questions></Questions>&ndash;&gt;-->
    <!--&lt;!&ndash;        <questionsset&ndash;&gt;-->
    <!--&lt;!&ndash;          v-for="link in essentialLinks"&ndash;&gt;-->
    <!--&lt;!&ndash;          :key="link.title"&ndash;&gt;-->
    <!--&lt;!&ndash;          v-bind="link"&ndash;&gt;-->
    <!--&lt;!&ndash;        />&ndash;&gt;-->
    <!--&lt;!&ndash;      </q-list>&ndash;&gt;-->
    <!--    </q-drawer>-->

    <!--    <q-drawer show-if-above v-model="rightDrawer" side="right" bordered>-->
    <!--      &lt;!&ndash; drawer content &ndash;&gt;-->
    <!--    </q-drawer>-->

    <q-page-container>
      <router-view/>
    </q-page-container>

    <!--    <q-footer bordered class="bg-grey-8 text-white">-->
    <!--      <q-toolbar>-->
    <!--        <q-toolbar-title>-->
    <!--          <q-avatar>-->
    <!--            <img src="../assets/enam-logo.svg">-->
    <!--          </q-avatar>-->
    <!--          Eitthvað spennandi-->
    <!--        </q-toolbar-title>-->
    <!--      </q-toolbar>-->
    <!--    </q-footer>-->

  </q-layout>
</template>

<script>
import { App } from '../App'
import Clock from 'components/Clock'

export default {
  name: 'MainLayout',
  components: {
    Clock
  },
  data () {
    return {
      loginblock: '',
      authenticated: App.authenticated
    }
  }
}
</script>
