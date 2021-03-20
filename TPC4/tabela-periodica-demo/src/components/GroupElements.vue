<template>
  <div class="d-flex flex-column align-center justify-center mx-auto">
    <v-progress-linear v-if="loading" indeterminate color="secondary" />
    <v-alert border="top" color="red lighten-2" dark v-if="error">
      {{ error }}
    </v-alert>
    <v-chip-group class="mt-3" v-if="elementos" center-active column>
      <v-chip
        color="secondary"
        v-for="el in elementos"
        :key="el"
        link
        exact
        :to="'/elementos/' + el"
      >
        {{ el }}
      </v-chip>
    </v-chip-group>
  </div>
</template>

<script>
import { fetchOntobud } from "@/utils/fetchOntobud";

export default {
  props: {
    grupo: String,
  },
  data() {
    return {
      elementos: [],
      loading: true,
      error: null,
    };
  },
  created() {
    fetchOntobud(`select ?s where { ?s :group :group_${this.grupo} } `)
      .then((res) => {
        let mapped = res.data.results.bindings.map((el) => {
          return el.s.value.split("#")[1];
        });

        this.elementos = mapped.sort();
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
</style>