<template>
  <v-app :style="{ background: $vuetify.theme.themes.dark.background }">
    <SideBar />
    <NavBar />
    <v-main>
      <v-form>
        <v-row class="mt-6">
          <v-col cols="2">
            <v-text-field
              v-model="name"
              label="Name"
              outlined
              dense
              clearable
            ></v-text-field
          ></v-col>
          <v-col cols="4">
            <v-file-input
              chips
              outlined
              dense
              label="File"
              accept=".txt"
              show-size
              small-chips
              truncate-length="20"
            ></v-file-input></v-col
          ><v-col
            ><v-btn elevation="2" outlined rounded>Add Wordlist</v-btn></v-col
          ></v-row
        >
      </v-form>

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
              :items="wordlistList"
              :search="search"
            ></v-data-table>
          </v-card>
        </v-col>
      </v-row>
    </v-main>
  </v-app>
</template>

<script>
import SideBar from "@/components/SideBar.vue";
import NavBar from "../components/NavBar.vue";

export default {
  name: "subdomainView",
  components: {
    SideBar,
    NavBar,
  },
  data() {
    return {
      loader: null,
      loading4: false,
      search: "",
      headers: [
        {
          text: "Name",
          align: "start",
          sortable: false,
          value: "name",
          width: 100,
        },
        { text: "File", value: "iron", width: 75, sortable:false },
      ],
      wordlistList: [],
    };
  },
  watch: {
    loader() {
      const l = this.loader;
      this[l] = !this[l];

      setTimeout(() => (this[l] = false), 3000);

      this.loader = null;
    },
  },
};
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
