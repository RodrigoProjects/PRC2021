<template>
  <div class="d-flex justify-content-center flex-column align-items-center">
    <h1
      class="pb-2 align-items-center display-4 mt-3 border-bottom border-dark al-center"
      style="width: 70%"
    >
      {{ $route.params.repo_id }} : {{ $route.params.class }} : Individuals
    </h1>
    <div class="mt-3" style="width: 40%;">
      <b-spinner v-if="loading" />
      <b-alert variant="danger" show v-if="error">{{ error }}</b-alert>
      <b-list-group class="mt-4" v-if="individuals">
        <b-list-group-item style="cursor:pointer" v-for="cla in individuals" :key="cla" @click="showModal(cla)">
          <h5> {{ cla }} </h5>
        </b-list-group-item>
      </b-list-group>
      <div>
          <b-button class="mt-5" @click="$router.back()" variant="outline-primary" size="lg">Anterior</b-button>
          <b-button class="mt-5 ml-2" @click="$router.push('/')" variant="outline-dark" size="lg">Página Principal</b-button>
      </div>
      
    </div>

    <IndModal v-for="ind in individuals" :key="ind" :id="ind" />

  </div>
</template>

<script>
const db = require('@/utils/GraphDB.js')
const axios = require('axios')


import IndModal from '@/components/IndModal'

export default {
    data () {
        return {
            individuals : [],
            loading : true,
            error : null,
            selected : null
        }
    }, 
    methods : {
        showModal (id){
            this.$bvModal.show(id)
        }
    },
    created () {

        axios.get('/api/repositories/' + this.$route.params.repo_id + "?query=" + encodeURIComponent(db.prefixes + "\nSELECT * WHERE { ?s rdf:type adv:" + this.$route.params.class + " }"))
            .then(repos => {

                this.individuals = repos.data.results.bindings.map(bind => {
                    return bind.s.value.split('#')[1]
                })

            })
            .catch(e => {
                this.error = e
            })
            .finally(() => {
                this.loading = false
            })
    },
    components : {
        IndModal
    }
}
</script>

<style>

</style>