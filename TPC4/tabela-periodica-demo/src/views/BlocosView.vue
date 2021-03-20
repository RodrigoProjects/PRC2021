<template>
  <div class="d-flex flex-column align-center justify-center mx-auto">
    <div class="text-h2 font-weight medium">Blocos</div>
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
    <div v-if="blocos && !loading" class="mt-5" style="width:70%">
      <v-expansion-panels>
        <v-expansion-panel v-for="el in blocos" :key="el">
          <v-expansion-panel-header> Bloco {{ el.charAt(0).toUpperCase() + el.slice(1) }}</v-expansion-panel-header>
          <v-expansion-panel-content>
            <BlockElements :bloco="el" />
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </div>
  </div>
</template>

<script>
import { fetchOntobud } from "@/utils/fetchOntobud";
import BlockElements from "@/components/BlockElements"

export default {
  data() {
    return {
      blocos: [],
      loading: true,
      error: null,
    };
  },
  components: {
      BlockElements
  },
  created() {
    fetchOntobud(`select ?s where { ?s rdf:type :Block } `)
      .then((res) => {
        let mapped = res.data.results.bindings.map((el) => {
          return el.s.value.split("#")[1].split("-")[0];
        });

        this.blocos = mapped.sort()
        
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