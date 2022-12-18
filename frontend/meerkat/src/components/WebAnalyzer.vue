/* eslint-disable */
<template>
  <v-dialog
    @click:outside="closeAnalyzerDialog"
    v-model="dialog"
    max-width="400"
  >
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
        Founded Technologies
        <v-row class="ml-1" v-if="responses.length === 0"
          >There is no founded technologies</v-row
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
        <v-btn color="blue darken-1" text @click="closeAnalyzerDialog">
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
  data: () => ({ loading: false, responses: [] }),
  methods: {
    save() {
      this.loading = true;
      let sendingUrl = [];
      sendingUrl.push(this.url);
      let dirDiscovery = { urls: sendingUrl };
      console.log(dirDiscovery);
      axios
        .post("http://localhost:8000/api/webAnalyzer/", dirDiscovery)
        .then((response) => {
          console.log(response.data);
          this.responses = Object.values(response.data)[0];
          console.log(this.responses);
          this.loading = false;
        });
    },
    closeAnalyzerDialog() {
      this.$emit("closeAnalyzerDialog");
      this.responses = [];
      this.loading = false;
    },
  },
};
</script>
