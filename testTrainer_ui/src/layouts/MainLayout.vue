<template>
  <q-layout view="hHh lpr fFf">
    <div class="q-pa-none q-ma-none">
      <Header></Header>
      <q-page-container class="basebackground">
        <router-view/>
      </q-page-container>
     <Footer></Footer>

    </div>
  </q-layout>
</template>

<script>
// import { mapState } from 'vuex'
import Header from 'components/Header'
import Footer from 'components/Footer'

export default {
  name: 'MainLayout',
  components: {
    Header,
    Footer
  },
  data () {
    return {}
  }
  // computed: mapState(['accessToken'])
}
</script>

<style scoped lang="css">
@import url(https://fonts.googleapis.com/css?family=Quicksand);
/*.nav-bar {*/
/*  background-color: #2f3033;*/
/*  width: 100%;*/
/*  position: fixed;*/
/*  top: 0;*/
/*  left: 0;*/
/*  overflow: hidden;*/
/*}*/
.nav-bar ul {
  position: absolute;
  right: -70px;
  top: 15px;
  list-style: none;
  margin: 0 14%;
  padding: 0;
  text-align: center;
  color: white;
}

.nav-bar ul li {
  display: inline-block;
  margin: 0 5px;
  /*padding: 25px;*/
  float: right;
}

.nav-bar:after {
  content: '';
  display: block;
  clear: both;
}

.nav-bar ul li a {
  text-decoration: none;
  font-family: 'Quicksand', sans-serif;
  font-size: 10px;
  font-weight: bold;
  color: white;
  padding: 5px;
  border-radius: 7px;
}

.nav-bar ul li a:hover {
  background-color: #a72a64;
}

.router-link-active {
  background-color: #a72a64
}

.basebackground {
  background-color: #fefefe;
}
</style>
