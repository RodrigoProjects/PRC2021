<template>
  <div class="d-flex align-center justify-center">
    <div class="mt-12 d-flex flex-column align-center" style="width: 70%">
      <div class="text-h4 blue--text lighten-2 font-weight-black">Entidades:</div>
      <v-divider class="mt-9 mb-6" style="width: 70%"></v-divider>
      <div class="mt-4 d-flex justify-space-around" style="width: 70%">
        <v-btn elevation="2" outlined x-large to="/authors">Autores</v-btn>
        <v-btn elevation="2" outlined x-large to="/pubs">Publicações</v-btn>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
</style>