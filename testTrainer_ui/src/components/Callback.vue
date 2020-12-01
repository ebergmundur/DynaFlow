<template>
  <div class="callback">
    <h3>CALLBACK</h3>
    Callback</div>
</template>

<script>
export default {
  name: 'callback',
  mounted () {
    this.$auth.handleAuthentication().then((data) => {
      this.$router.push({ name: 'home' })
    })
  }
}
</script>
