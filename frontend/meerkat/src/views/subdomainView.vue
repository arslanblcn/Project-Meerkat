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
            <v-text-field
              v-model="domain"
              label="Domain Address"
              dense
              outlined
              clearable
            ></v-text-field></v-col
          ><v-col
            ><v-btn elevation="2" outlined rounded @click="getList"
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
            <v-text-field
              v-model="search"
              append-icon="mdi-magnify"
              label="Search"
              single-line
              hide-details
            ></v-text-field>
          </v-card-title>
          <v-data-table :headers="headers" :items="domains" :search="search">
            <template v-slot:[`item.actions`]="{ item }">
              <v-menu top>
                <template v-slot:activator="{ on, attrs }">
                  <v-btn v-bind="attrs" v-on="on" icon>
                    <v-icon>mdi-cog-outline</v-icon>
                  </v-btn>
                </template>

                <v-list dense>
                  <v-list-item link @click="subdomainBruteForce(item, 'subF')">
                    <v-list-item-title>
                      <v-icon left>mdi-arrow-collapse-all </v-icon>Subdomain
                      Bruteforce
                    </v-list-item-title>
                  </v-list-item>
                  <v-list-item link>
                    <v-list-item-title @click="wafDetect(item)">
                      <v-icon left>mdi-arrow-collapse-all</v-icon>Waf Detect
                    </v-list-item-title>
                  </v-list-item>
                  <v-list-item link>
                    <v-list-item-title @click="wafDetect(item)">
                      <v-icon left>mdi-arrow-collapse-all</v-icon>Port Scan
                    </v-list-item-title>
                  </v-list-item>
                  <v-list-item link>
                    <v-list-item-title @click="wafDetect(item)">
                      <v-icon left>mdi-arrow-collapse-all</v-icon>Wayback Scan
                    </v-list-item-title>
                  </v-list-item>
                </v-list>
              </v-menu>
            </template>
   
          </v-data-table>
        </v-card>
      </v-row>
      <Dialog
        :dialog="dialog"
        :attackType="attackType"
        @closeDialog="dialog = false"
      />
    </v-main>
  </v-app>
</template>

<script>
/* eslint-disable */
import SideBar from "@/components/SideBar.vue";
import NavBar from "../components/NavBar.vue";
import Dialog from "../components/AttackDialog.vue";
import axios from "axios";
export default {
  name: "subdomainView",
  components: {
    SideBar,
    NavBar,
    Dialog,
  },
  data() {
    return {
      loader: null,
      loading4: false,
      domain: null,
      dialog: false,
      name: null,
      attackType: null,
      search: "",
      headers: [
        { text: "Header", value: "header", width: 200, align: "start" },
        {
          text: "Domain Address",
          sortable: false,
          value: "domain",
          width: 125,
          align: "center",
        },
        { text: "IP", value: "ip", width: 125, align: "center" },
        {
          text: "Reverse DNS",
          value: "reverse_dns",
          sortable: false,
          width: 100,
          align: "center",
        },
        {
          text: "As",
          value: "as",
          sortable: false,
          width: 125,
          align: "center",
        },
        {
          text: "Provider",
          value: "provider",
          width: 125,
          sortable: false,
          align: "center",
        },
        {
          text: "Country",
          value: "country",
          width: 125,
          sortable: false,
          align: "center",
        },

        { text: "Actions", value: "actions", align: "end" },
      ],
      domains: [

      ],
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
  methods: {
    getList() {
      const article = { scanname: this.name, domains: this.domain,user:1 };
      axios
        .post("http://localhost:8000/api/sublist3r/",article)
        .then((response) =>{console.log(response); this.domains=response.data.dns_records.host} );
    },
    subdomainBruteForce(item, attackType) {
      this.dialog = true;
      this.attackType = attackType;
      console.log(item);
    },
    wafDetect(item) {
      console.log(item);
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
