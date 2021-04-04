<template>
  <div class="d-flex flex-column align-center justify-center mx-auto">
    <div
      v-if="pubs && !error"
      class="d-flex flex-column align-center justify-center mt-9"
    >

    <div class="text-h2">Publicações:</div>
    <v-divider class="mt-4" width="60%"></v-divider>
    <v-dialog transition="dialog-bottom-transition" max-width="600">
        <template v-slot:activator="{ on, attrs }">
          <v-btn class="mt-8" color="success" outlined v-bind="attrs" v-on="on"
            >Adicionar</v-btn
          >
        </template>
        <template v-slot:default="dialog">
          <v-card>
            <v-toolbar color="success" dark>Criar uma nova Publicação</v-toolbar>
            <v-card-text>
              <div class="text-h2 pa-12">Formulário</div>
            </v-card-text>
            <v-card-actions class="justify-end">
              <v-btn color="red lighten-2" text @click="dialog.value = false">Fechar</v-btn>
            </v-card-actions>
          </v-card>
        </template>
      </v-dialog>
    <v-pagination v-model="page" class="my-10" :length="Math.floor(pubs.length / 10)" :total-visible="15"></v-pagination>
      <div class="d-flex align-center justify-space-around flex-wrap" style="vertical-align: top;">
        <Publication class="mb-6" :id="pub" v-for="pub in pubs_page" :key="pub" style="flex: 0 1 21%;"/>
      </div>
      
      
    </div>

    <v-progress-circular v-if="loading" indeterminate color="primary" class="mt-5" />
    <v-alert border="top" color="red lighten-2" dark v-if="error">
      {{ error }}
    </v-alert>
  </div>
</template>

<script>
import { fetchOntobud } from "@/utils/fetchOntobud.js";
import Publication from "@/components/Publication";

export default {
  data() {
    return {
      pubs: null,
      loading: true,
      error: null,
      page: 1,
    };
  },
  components: {
    Publication,
  },
  methods: {},
  created() {
    fetchOntobud("select * where { ?s rdf:type :Resource }")
      .then((d) => {
        this.pubs = d.data.results.bindings.map((e) => e.s.value.split("#")[1]);
      })
      .catch((e) => (this.error = e))
      .finally(() => (this.loading = false));
  },
  computed: {
    pubs_page() {
      return this.pubs.slice((this.page - 1) * 10, this.page * 10);
    },
  },
};
</script>

<style>
</style>