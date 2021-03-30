<template>
  <div class="row">
    <div class="flex flex-break q-py-md"></div>
    <div
      class="bg-grey-9 text-white items-end"
      style="clear: all; width: 100%; height: 50px; margin-top: 30px;"
    >
      <!-- <q-footer
    elevated
    class="bg-grey-9 text-white relative-position"
    > -->
      <q-toolbar>
        <q-toolbar-title style="text-align: center;">
          <q-avatar>
            <img src="../assets/enam-logo.svg" />
          </q-avatar>
          ©2021 E-nám ehf. – netfang:
          <a href="mailto:enam@enam.is" style="color: white;">enam@enam.is</a>
        </q-toolbar-title>
      </q-toolbar>
      <!-- </q-footer> -->
    </div>
  </div>
</template>

<script>
export default {
  name: 'Footer'
}
</script>
