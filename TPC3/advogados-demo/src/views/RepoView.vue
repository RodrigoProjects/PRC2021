<template>
  <div class="d-flex justify-content-center flex-column align-items-center">
    <h1
      class="pb-2 align-items-center display-4 mt-3 border-bottom border-dark al-center"
      style="width: 70%"
    >
      {{ $route.params.repo_id }} : Classes
    </h1>
    <div class="mt-3" style="width: 40%;">
      <b-spinner v-if="loading" />
      <b-alert variant="danger" show v-if="error">{{ error }}</b-alert>
      <b-list-group class="mt-4" v-if="classes">
        <b-list-group-item v-for="cla in classes" :key="cla" :href="`${$route.params.repo_id}/class/${cla}`">
          <h5> {{ cla }} </h5>
        </b-list-group-item>
      </b-list-group>
      <b-button class="mt-5" @click="$router.back()" variant="outline-primary" size="lg">Anterior</b-button>
    </div>
  </div>
</template>

<script>
const db = require('@/utils/GraphDB.js')
const axios = require('axios')
export default {
    data () {
        return {
            classes : [],
            loading : true,
            error : null
        }
    }, 
    methods : {

    },
    created () {

        axios.get('/api/repositories/' + this.$route.params.repo_id + "?query=" + encodeURIComponent(db.prefixes + "\nSELECT * WHERE { ?s rdf:type owl:Class }"))
            .then(repos => {

                this.classes = repos.data.results.bindings.map(bind => {
                    return bind.s.value.split('#')[1]
                })

                console.log(this.classes)
            })
            .catch(e => {
                this.error = e
            })
            .finally(() => {
                this.loading = false
            })
    }
}
</script>

<style>

</style>