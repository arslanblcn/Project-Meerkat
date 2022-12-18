/* eslint-disable */
<template>
  <v-dialog v-model="dialog" @click:outside="closeDialog" max-width="400">
    <v-card width="400">
      <v-card-text>
        <v-row>
          <v-col cols="12" class="mt-6">
            <v-text-field
              v-model="url"
              dense
              disabled
              outlined
              label="DNS Name"
              required
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12">
            <v-select
              label="File Name"
              dense
              outlined
              :items="wordlist"
              v-model="fileName"
            ></v-select>
          </v-col>
        </v-row>
        Founded Directories
        <v-row class="ml-1" v-if="responses.length === 0"
          >There is no founded directory</v-row
        >
        <v-row>
          <v-chip-group>
            <v-chip class="ml-2" v-for="item in responses" :key="item">
              {{ item }}
            </v-chip>
          </v-chip-group></v-row
        >
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" :loading="loading" text @click="save">
          Run
        </v-btn>
        <v-btn color="blue darken-1" text @click="closeDialog"> Close </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
import axios from "axios";
/* eslint-disable */
export default {
  watch: {
    dirDiscoveryObj: {
      handler: function (n) {
        this.url = n.domain;
      },
      immediate: true,
    },
  },
  props: { dialog: { type: Boolean }, dirDiscoveryObj: { type: Object } },
  data: () => ({
    loading: false,
    wordlist: [],
    url: "",
    fileName: null,
    responses: [],
  }),
  methods: {
    save() {
      this.loading = true;
      let dirDiscovery = { url: "http://" + this.url, filename: this.fileName };
      console.log(dirDiscovery);
      axios
        .post("http://localhost:8000/api/dirDiscovery/", dirDiscovery)
        .then((response) => {
          this.responses = response.data;
          this.loading = false;
        });
    },
    closeDialog() {
      this.$emit("closeDialog");
      this.fileName = null;
      this.responses = [];
      this.loading = false;
    },
  },
  created() {
    axios.get("http://localhost:8000/api/dirDiscovery/").then((response) => {
      console.log(response.data);
      this.wordlist = response.data;
    });
  },
};
</script>
