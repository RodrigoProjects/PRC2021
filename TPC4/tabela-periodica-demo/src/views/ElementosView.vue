<template>
  <div class="d-flex flex-column align-center justify-center mx-auto">
    <v-progress-circular v-if="loading" indeterminate color="primary" />
    <v-alert border="top" color="red lighten-2" dark v-if="error">
      {{ error }}
    </v-alert>
    <div class="elements" style="width: 80%">
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Procurar elemento"
        hide-details
        v-if="elementos"
      ></v-text-field>
      <v-chip-group class="mt-3" v-if="elementos" center-active column>
        <v-chip color="secondary" v-for="el in filteredElements" :key="el.abv" link :to="'elementos/' + el.abv">
          {{ el.abv }} - {{ el.nome }}
        </v-chip>
      </v-chip-group>
      <v-divider v-if="filteredElements.length" class="mt-3" />

      <router-view />

    </div>
  </div>
</template>

<script>
import { fetchOntobud } from "@/utils/fetchOntobud";

export default {
  data() {
    return {
      elementos: [],
      loading: true,
      error: null,
      search: "",
    };
  },
  methods: {},
  created() {
    fetchOntobud(
      "select * where { ?s rdf:type :Element; :name ?nome } order by ?s"
    )
      .then((res) => {
        console.log(res.data);
        this.elementos = res.data.results.bindings.map((el) => {
          return {
            abv: el.s.value.split("#")[1],
            nome: el.nome.value,
          };
        });
      })
      .catch((e) => {
        this.error = e;
      })
      .finally(() => {
        this.loading = false;
      });
  },
  computed: {
      filteredElements () {
          if(this.search.replace(/\s+/, '') == ""){
              return []
          }

          return this.elementos.filter(e => {
              return (e.abv.toLowerCase().startsWith(this.search.toLowerCase().replace(/\s+/, '')) || e.nome.toLowerCase().startsWith(this.search.toLowerCase().replace(/\s+/, '')))
          })
      }
  }
};
</script>

<style>
.elements span {
  text-transform: capitalize;
}
</style>