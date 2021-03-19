<template>
  <div class="mt-6 d-flex flex-column align-center">
    <div
      v-if="loading"
      style="width: 70%"
      class="d-flex flex-column align-center"
    >
      <div class="text-h5 mb-5 d-flex flex-column align-center justify-center">
        Procurando o elemento <b>{{ this.$route.params.element }}</b>
        <v-img
          lazy-src="@/assets/logo2.gif"
          max-height="300"
          max-width="300"
          src="@/assets/logo2.gif"
        ></v-img>
      </div>
      <v-progress-linear indeterminate color="secondary" />
    </div>

    <v-alert border="top" color="red lighten-2" dark v-if="error">
      {{ error }}
    </v-alert>
    <div v-if="data && !loading" style="width: 70%">
      <div class="text-h2">
        <div class="d-flex align-center header flex-column justify-center">
          <v-img
            lazy-src="@/assets/logo3.gif"
            max-height="180"
            max-width="180"
            src="@/assets/logo3.gif"
          ></v-img>
          <div
            class="text-h3 mr-1 font-weight-medium"
            transition="fade-transition"
          >
            {{ data.name }}
          </div>
        </div>
        <v-divider class="mt-10"></v-divider>
        <div class="d-flex align-center justify-center pt-3" style="">
          <v-card tile width="60%">
            <v-list-item v-for="k in Object.keys(data)" :key="k" class="header">
              <v-list-item-content>
                <v-list-item-title class="font-weight-bold text-h5">{{ k }}:</v-list-item-title>
                <v-list-item-subtitle class="font-weight-black text-h6">{{ data[k] }} </v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-card> 
        </div>
      </div>
      <div></div>
    </div>
  </div>
</template>

<script>
import { fetchOntobud } from "@/utils/fetchOntobud";

export default {
  data() {
    return {
      data: [],
      loading: true,
      error: null,
    };
  },
  methods: {},
  created() {
    fetchOntobud(
      `select * where { :${this.$route.params.element} ?key ?value } `
    )
      .then((res) => {
        let acc = {};

        res.data.results.bindings.map((el) => {
          let key =
            el.key.type == "literal"
              ? el.key.value
              : el.key.value.split("#")[1];

          acc[key] =
            el.value.type == "literal"
              ? el.value.value
              : el.value.value.split("#")[1];
        });

        this.data = acc;
        console.log(this.data);
      })
      .catch((e) => {
        this.error = e;
      })
      .finally(() => {
        this.loading = false;
      });
  },
};
</script>

<style>
.header {
  text-transform: capitalize;
}
</style>