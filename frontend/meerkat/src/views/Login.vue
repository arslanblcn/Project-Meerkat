<template>
  <v-app :style="{ background: $vuetify.theme.themes.dark.background }">
    <NavBar />
    <v-main>
      <v-form
        ><v-row class="mt-3"
          ><v-col cols="4"></v-col
          ><v-col cols="4"
            ><v-card class="justify-center" elevation="0">
              <v-col cols="12">
                <v-text-field
                  v-model="name"
                  label="User Name"
                  outlined
                  dense
                  clearable
                ></v-text-field
              ></v-col>
              <v-col cols="12">
                <v-text-field
                @click:append="show1 = !show1"
                  :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                  :type="show1 ? 'text' : 'password'"
                  v-model="password"
                  label="Password"
                  dense
                  outlined
                  clearable
                ></v-text-field></v-col
              ><v-row
                ><v-spacer></v-spacer
                ><v-col
                  ><v-btn
                    elevation="2"
                    outlined
                    class="mr-4"
                    rounded
                    @click="goToRegister"
                    >Register</v-btn
                  ><v-btn
                    elevation="2"
                    outlined
                    rounded
                    @click="login"
                    >Login</v-btn
                  ></v-col
                ></v-row
              >
            </v-card>
          </v-col>
        </v-row>
      </v-form>
    </v-main>
  </v-app>
</template>

<script>
/* eslint-disable */
import axios from "axios";
import NavBar from "../components/NavBar.vue";
export default {
  name: "Login",
  data() {
    return {
      name: null,
      password: null,
      show1: false,
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
    goToRegister() {
      this.$router.push("/register");
    },
    login() {
      let user = { username: this.name, password: this.password };
      axios
        .post("http://localhost:8000/api//login/", user)
        .then((response) => {
          if (response.status===200) {
            this.$router.push("/");
          }
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
