<template>
  <div class="d-flex flex-column align-center justify-center mx-auto">
    <v-progress-circular v-if="loading" indeterminate color="primary" />
    <v-alert border="top" color="red lighten-2" dark v-if="error">
      {{ error }}
    </v-alert>
  </div>
</template>

<script>
import {fetchOntobud} from '@/utils/fetchOntobud.js'

export default {
    data() {
        return {
            pubs : [],
            loading : true,
            error : null
        }
    },
    methods : {

    },
    created(){
        fetchOntobud('SELECT * WHERE { ?s rdf:type :Resource}')
            .then(d => {
                console.log(d.data.results.bindings)
            })
            .catch(e => this.error = e)
            .finally(() => this.loading = false)
    }
};
</script>

<style>
</style>