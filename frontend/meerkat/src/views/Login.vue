<template>
  <v-app :style="{ background: $vuetify.theme.themes.dark.background }">
    <NavBar />
    <v-main>
      <v-form
        ><v-card elevation="0">
          <v-col cols="3">
            <v-text-field
              v-model="name"
              label="User Name"
              outlined
              dense
              clearable
            ></v-text-field
          ></v-col>
          <v-col cols="3">
            <v-text-field
              v-model="password"
              label="Password"
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
              @click="login"
              >Login</v-btn
            ></v-col
          >
        </v-card>
      </v-form>
    </v-main>
  </v-app>
</template>

<script>
/* eslint-disable */
import NavBar from "../components/NavBar.vue";
export default {
  name: "Login",
  data() {
    return {
      name: null,
      password: null,
    };
  },
  components: {
    NavBar,
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
    login() {
      let user = { name: this.name, password: this.passwords };
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
