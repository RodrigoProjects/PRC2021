<template>
  <b-modal :id="id" ok-only :title="'Individual :' + id" footer="">
      <div class="d-flex justify-content-center flex-column align-items-center"> 
           <b-spinner v-if="loading" />
           <b-alert variant="danger" show v-if="error">{{ error }}</b-alert>
           <b-list-group style="width: 80%" class="mt-4" v-if="data">
                <b-list-group-item style="cursor:pointer" v-for="(el, idx) in data" :key="idx">
                    <h5> <b>{{ el.p }}</b> : {{ el.o }} </h5>
                </b-list-group-item>
            </b-list-group>
      </div>
  </b-modal>
</template>

<script>
const db = require('@/utils/GraphDB.js')
const axios = require('axios')

export default {
    props : {
        id : String
    },
    data () {
        return {
            data : [],
            loading : true,
            error : null
        }
    },
    created () {
        axios.get('/api/repositories/' + this.$route.params.repo_id + "?query=" + encodeURIComponent(db.prefixes + "\nSELECT * WHERE { adv:" + this.id + " ?p ?o }"))
            .then(repos => {

                this.data = repos.data.results.bindings.map(bind => {
                    return {
                        'p' : bind.p.value.split('#')[1],
                        'o' : bind.o.value.includes('#') ? bind.o.value.split('#')[1] : bind.o.value
                    }
                })
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