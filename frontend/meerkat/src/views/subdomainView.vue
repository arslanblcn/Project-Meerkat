<template>
<v-app :style="{ background: $vuetify.theme.themes.dark.background }">
<SideBar />
<NavBar />
  <v-main>
    <template>
      <v-form>
        <v-container>
          <v-row>
            <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            v-model="message4"
            label="Outlined"
            outlined
            clearable
          ></v-text-field>
        </v-col>
          </v-row>
        </v-container>
      </v-form>
    </template>
    <v-row class="mt-3">
      <v-col cols="12" sm="9">
        <v-card>
        <v-card-title>
          Results
          <v-spacer></v-spacer>
          <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Search"
            single-line
            hide-details
          ></v-text-field>
        </v-card-title>
        <v-data-table
          :headers="headers"
          :items="desserts"
          :search="search"
        ></v-data-table>
      </v-card>
      </v-col>
    </v-row>
  </v-main>
</v-app>
</template>

<script>
import SideBar from '@/components/SideBar.vue';
import NavBar from '../components/NavBar.vue';

  export default {
    name: 'subdomainView',
    components: {
    SideBar,
    NavBar
  },
  data () {
      return {
        loader: null,
        loading4: false,
        search: '',
        headers: [
          {
            text: 'Dessert (100g serving)',
            align: 'start',
            sortable: false,
            value: 'name',
          },
          { text: 'Calories', value: 'calories' },
          { text: 'Fat (g)', value: 'fat' },
          { text: 'Carbs (g)', value: 'carbs' },
          { text: 'Protein (g)', value: 'protein' },
          { text: 'Iron (%)', value: 'iron' },
        ],
        desserts: [
          {
            name: 'Frozen Yogurt',
            calories: 159,
            fat: 6.0,
            carbs: 24,
            protein: 4.0,
            iron: '1%',
          },
          {
            name: 'Ice cream sandwich',
            calories: 237,
            fat: 9.0,
            carbs: 37,
            protein: 4.3,
            iron: '1%',
          },
        ],
      }
    },
    watch: {
      loader () {
        const l = this.loader
        this[l] = !this[l]

        setTimeout(() => (this[l] = false), 3000)

        this.loader = null
      },
    },
}
</script>
<style>
  .custom-loader {
    animation: loader 1s infinite;
    display: flex;
  }
  @-moz-keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
  @-webkit-keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
  @-o-keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
  @keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
</style>