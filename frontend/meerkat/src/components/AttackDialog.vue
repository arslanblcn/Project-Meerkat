/* eslint-disable */
<template>
  <v-dialog v-model="dialog" max-width="400">
    <v-card width="400">
      <v-card-text>
        <v-row>
          <v-col cols="12" class="mt-6">
            <v-text-field
              dense
              outlined
              label="DNS Name"
              required
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12">
              <v-file-input
              chips
              outlined
              dense
              label="File"
              accept=".txt"
              show-size
              small-chips
              truncate-length="20"
            ></v-file-input>
          </v-col>
        </v-row>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="closeDialog"> Close </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
/* eslint-disable */
export default {
  props: { dialog: { type: Boolean }, attackType: { type: String } },
  data: () => ({}),
  methods: {
    closeDialog() {
      this.$emit("closeDialog");
    },
  },
};
</script>