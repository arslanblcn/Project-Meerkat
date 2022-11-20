<template>
  <v-row justify="center">
    <v-col cols="12" sm="3">
      <v-card
        elevation="9"
        outlined
        shaped
        width="280"
        class="mt-7 ml-0"
      >
        <v-card-title>
          Total Analysis
          <v-icon large right class="mx-auto" color="red">
           fa-solid fa-chart-line
          </v-icon>
        </v-card-title>
        <v-card-text>
          19
        </v-card-text>
      </v-card>
    </v-col>
    <v-col cols="12" sm="3">
      <v-card
        elevation="9"
        outlined
        shaped
        width="280"
        class="mt-7 ml-2"
      >
        <v-card-title>
          Founded Indicators
          <v-icon large right class="mx-auto" color="success">
            fa-solid fa-bug
          </v-icon>
        </v-card-title>
        <v-card-text>
          30
        </v-card-text>
      </v-card>
    </v-col>
    <v-col cols="12" sm="3">
      <v-card
        elevation="9"
        outlined
        shaped
        width="280"
        class="mt-7 ml-2"
      >
        <v-card-title>
          Windows Analysis
           <v-icon large right class="mx-auto" color="blue">
            fa-brands fa-windows
           </v-icon>
        </v-card-title>
        <v-card-text>
          5
        </v-card-text>
      </v-card>
    </v-col>
    <v-col cols="12" sm="3">
      <v-card
        elevation="9"
        outlined
        shaped
        width="280"
        class="mt-7 ml-2"
      >
        <v-card-title>
          Linux Analysis
          <v-icon large right class="mx-auto" color="pink">
            fa-brands fa-linux
           </v-icon>
        </v-card-title>
        <v-card-text>
          14
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
}
</script>

<style>
</style>