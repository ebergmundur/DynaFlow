<template>
  <div class="callback">Callback</div>
</template>

<script>
export default {
  name: 'callback',
  mounted () {
    this.$auth.handleAuthentication().then((data) => {
      console.log(data)
      this.$router.push({ name: 'front' })
    })
  }
}
</script>
