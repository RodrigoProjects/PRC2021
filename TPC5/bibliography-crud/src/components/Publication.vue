<template>
  <div>
    <v-card v-if="pub" elevation="4">
       <v-card-title>
           {{ id }}
       </v-card-title>
       <v-card-text>
           <div v-for="p in pub" :key="p.p + p.o">
               <v-divider></v-divider>
               <b>{{ p.p }}:</b> <span>{{ p.o }}</span>
           </div>
       </v-card-text>
    </v-card>
  </div>
</template>

<script>
import { fetchOntobud } from "@/utils/fetchOntobud.js";

export default {
  props: {
    id: String,
  },
  data() {
    return {
      pub: [],
      loading: true,
      error: null,
      page: 1,
    };
  },
  methods: {},
  created() {
    fetchOntobud(`select * where { :${this.id} ?p ?o }`)
      .then((d) => {
        this.pub = d.data.results.bindings.map((e) => {
          return {
            p: e.p.type == "literal" ? e.p.value : e.p.value.split("#")[1],
            o: e.o.type == "literal" ? e.o.value : e.o.value.split("#")[1],
          };
        });

      })
      .catch((e) => (this.error = e))
      .finally(() => (this.loading = false));
  },
};
</script>

<style>
</style>