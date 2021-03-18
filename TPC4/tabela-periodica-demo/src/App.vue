<template>
  <v-app>
    <v-navigation-drawer app dark clipped :mini-variant.sync="mini">
      <v-divider></v-divider>

      <v-list dense nav>

        <v-list-item link to="/elementos">
          <v-list-item-icon>
            <v-icon>mdi-flask-outline</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>Elementos</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link to="/grupos">
          <v-list-item-icon>
            <v-icon>mdi-table-column</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>Grupos</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link to="/periodos">
          <v-list-item-icon>
            <v-icon>mdi-table-row</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>Períodos</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item link to="/blocos">
          <v-list-item-icon>
            <v-icon>mdi-table</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>Blocos</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app color="dark" dark clipped-left>
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="@/assets/logo2.png"
          transition="scale-transition"
          width="60"
        />

        <h2>Tabela Periódica</h2>
      </div>

      <v-spacer></v-spacer>

      <v-btn href="https://github.com/RodrigoProjects" target="_blank" text>
        <span class="mr-2">GitHub</span>
        <v-icon>mdi-github</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  components: {},

  data: () => ({
  }),
};
</script>
