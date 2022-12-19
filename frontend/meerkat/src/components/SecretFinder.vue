/* eslint-disable */
<template>
  <v-dialog
    v-model="dialog"
    @click:outside="closeSecretFinderDialog"
    max-width="600"
  >
    <v-card width="600">
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
        Founded Secrets

        <v-row>
          <v-data-table
            :headers="headers"
            :items="dataTableItems"
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
        <v-btn color="blue darken-1" text @click="closeSecretFinderDialog">
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
    search: null,
    loading: false,
    responses: [],
    dataTableItems: [],
    headers: [
      { text: "Url", value: "url", width: 200, align: "start" },
      { text: "Key", value: "key", width: 200, align: "start" },
    ],
  }),
  methods: {
    save() {
      this.loading = true;
      let secretFinder = [];
      secretFinder.push("https://" + this.url);
      let sendingObj = { urls: secretFinder };
      axios
        .post("http://localhost:8000/api/secretFinder/", sendingObj)
        .then((response) => {
          this.loading = false;
          this.dataTableItems = response.data;
        });
    },
    closeSecretFinderDialog() {
      this.$emit("closeSecretFinderDialog");
      this.responses = [];
      this.loading = false;
    },
  },
};
</script>
