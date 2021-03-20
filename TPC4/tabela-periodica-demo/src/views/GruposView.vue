<template>
  <div class="d-flex flex-column align-center justify-center mx-auto">
    <div class="text-h2 font-weight medium">Grupos</div>
    <v-progress-linear
      class="mt-6"
      style="width: 70%"
      v-if="loading"
      indeterminate
      color="secondary"
    />
    <v-alert border="top" color="red lighten-2" dark v-if="error">
      {{ error }}
    </v-alert>
    <div v-if="grupos && !loading" class="mt-5" style="width:70%">
      <v-expansion-panels>
        <v-expansion-panel v-for="el in grupos" :key="el">
          <v-expansion-panel-header> Grupo {{ el.charAt(0).toUpperCase() + el.slice(1) }}</v-expansion-panel-header>
          <v-expansion-panel-content>
            <GroupElements :grupo="el" />
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </div>
  </div>
</template>

<script>
import { fetchOntobud } from "@/utils/fetchOntobud";
import GroupElements from "@/components/GroupElements"

export default {
  data() {
    return {
      grupos: [],
      loading: true,
      error: null,
    };
  },
  components: {
      GroupElements
  },
  created() {
    fetchOntobud(`select ?s where { ?s rdf:type :Group } `)
      .then((res) => {
        let mapped = res.data.results.bindings.map((el) => {
          return el.s.value.split("#")[1].split("_")[1];
        });

        this.grupos = mapped.sort((fst, snd) => {
          return parseInt(fst) >= parseInt(snd);
        });
      })
      .catch((e) => {
        this.error = e;
      })
      .finally(() => {
        this.loading = false;
      });
  }
};
</script>

<style>
</style>