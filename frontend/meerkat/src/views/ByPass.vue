<template>
  <v-app :style="{ background: $vuetify.theme.themes.dark.background }">
    <SideBar />
    <NavBar />
    <v-main>
      <v-form>
        <v-row class="mt-6">
          <v-col cols="4">
            <v-text-field
              v-model="domain"
              label="URL"
              dense
              outlined
              clearable
            ></v-text-field
          ></v-col>
          <v-col cols="4">
            <v-text-field
              v-model="path"
              label="Path"
              dense
              outlined
              clearable
            ></v-text-field></v-col
          ><v-col
            ><v-btn
              :loading="loading"
              elevation="2"
              outlined
              rounded
              @click="getList"
              >Find</v-btn
            ></v-col
          ></v-row
        >
      </v-form>

      <v-row class="mt-3 ml-1">
        <v-card>
          <v-card-title>
            Results
            <v-spacer></v-spacer>
          </v-card-title>
          <v-card-text>
            <v-row class="ml-1" v-if="domains.length === 0"
              >There is no founded secret</v-row
            >
            <v-row>
              <v-chip-group>
                <v-chip class="ml-2" v-for="item in domains" :key="item">
                  {{ item }}
                </v-chip>
              </v-chip-group></v-row
            ></v-card-text
          >
        </v-card>
      </v-row>
    </v-main>
  </v-app>
</template>

<script>
/* eslint-disable */
import SideBar from "@/components/SideBar.vue";
import NavBar from "../components/NavBar.vue";
import axios from "axios";
export default {
  name: "ByPass",
  components: {
    SideBar,
    NavBar,
  },
  data() {
    return {
      loading: false,
      path: null,

      domain: null,

      domains: [],
    };
  },
  methods: {
    getList() {
      this.loading = true;
      const article = { url: this.domain, path: this.path };
      axios
        .post("http://localhost:8000/api/bypass403/", article)
        .then((response) => {
          console.log(response);
          this.loading = false;
          this.domains = response.data;
        });
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
