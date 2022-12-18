/* eslint-disable */
<template>
  <v-dialog  @click:outside="closeScanDialog" v-model="dialog" max-width="600">
    <v-card width="600">
      <v-card-text>
        <v-row>
          <v-col cols="6" class="mt-6">
            <v-text-field
              v-model="url"
              dense
              disabled
              outlined
              label="DNS Name"
              required
            ></v-text-field>
          </v-col>
          <v-col cols="6" class="mt-6">
            <v-text-field
              v-model="year"
              dense
              outlined
              label="Year"
              required
            ></v-text-field>
          </v-col>
        </v-row>
        Founded Urls
        <v-row>
          <v-data-table
            :headers="headers"
            :items="responses"
            hide-default-header
            :search="search"
          >
          </v-data-table
        ></v-row>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" :loading="loading" text @click="save">
          Run
        </v-btn>
        <v-btn color="blue darken-1" text @click="closeScanDialog">
          Close
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
import axios from "axios";
/* eslint-disable */
export default {
  props: { dialog: { type: Boolean }, url: { type: String } },
  data: () => ({
    loading: false,
    responses: [],
    year: null,
    search: null,
    headers: [{ text: "Url", value: "url", width: 200, align: "start" }],
  }),
  methods: {
    save() {
      this.loading = true;
      let dirDiscovery = { url: this.url, year: this.year };
      console.log(dirDiscovery);
      axios
        .post("http://localhost:8000/api/wayback/", dirDiscovery)
        .then((response) => {
          console.log(response.data);
          this.responses = [];
          let item = null;
          for (const res of response.data) {
            item = { url: res };
            this.responses.push(item);
          }
          this.loading = false;
        });
    },
    closeScanDialog() {
      this.$emit("closeScanDialog");
      this.responses = [];
      this.loading = false;
      this.year=null
    },
  },
};
</script>
