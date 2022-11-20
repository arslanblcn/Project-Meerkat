<template>
<v-app :style="{ background: $vuetify.theme.themes.dark.background }">
<SideBar />
<NavBar />
<v-main>
  <v-container>
    <CardsComp />
    <ChartComp />
    <DataTable />
  </v-container>
</v-main>
</v-app>
</template>

<script>
import SideBar from '@/components/SideBar.vue';
import CardsComp from '@/components/CardsComp.vue';
import ChartComp from '@/components/ChartComp.vue';
import DataTable from '@/components/DataTable.vue';
import NavBar from '../components/NavBar.vue';

  export default {
    name: 'HomeView',

    components: {
    SideBar,
    CardsComp,
    ChartComp,
    DataTable,
    NavBar
},
  }
</script>
