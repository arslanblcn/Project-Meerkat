<template>
  <v-row class="mt-10">
    <v-col cols="12" sm="12">
      <v-card>
        <v-card-title>
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
          :items="results"
          :search="search"
        ></v-data-table>
      </v-card>
    </v-col>
  </v-row>
</template>
<script>
import axios from "axios";
export default {
  created() {
    axios
      .get("http://localhost:8000/api/sublist3r/")
      .then((response) => {
        console.log(response);
        this.results = response.data;
      });
  },
  data() {
    return {
      search: "",
      headers: [
        {
          text: "Scanname",
          align: "start",
          value: "scanname",
        },
        { text: "Domains", filterable: false, value: "domains" },
        { text: "Created at", filterable: false, value: "created_at" },
      ],
      results: [
   
      ],
    };
  },
};
</script>
