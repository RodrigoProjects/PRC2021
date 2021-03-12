<template>
  <div class="d-flex justify-content-center flex-column align-items-center">
    <h1
      class="pb-2 align-items-center display-3 mt-3 border-bottom border-dark al-center"
      style="width: 70%"
    >
      GraphDB Repos
    </h1>
    <div class="mt-3" style="width: 40%;">
      <b-spinner v-if="loading" />
      <b-alert variant="danger" show v-if="error">{{ error }}</b-alert>
      <b-list-group v-if="repos">
        <b-list-group-item v-for="repo in repos" :key="repo.id" :href="`/repo/${repo.id}`">
          <h5> {{ repo.id }} </h5>
          <span class="text-muted" style="width: 40%;"> {{ repo.title }}</span>
        </b-list-group-item>
      </b-list-group>
    </div>
  </div>
</template>

<script>

import axios from 'axios'

export default {
  data() {
    return {
      repos: [],
      loading: true,
      error: null
    };
  },
  methods: {
    teste() {
      this.msg = "Testeeee";
    },
  },
  created() {
    axios.get('rest/repositories')
      .then(repos => {
        this.repos = repos.data
      })
      .catch(e => {
        this.error = e
      })
      .finally(() => {
        this.loading = false
      })
  }
};
</script>
