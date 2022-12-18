<template>
  <v-app :style="{ background: $vuetify.theme.themes.dark.background }">
    <NavBar />
    <v-main>
      <v-form ref="form" v-model="valid" lazy-validation
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
                  v-model="email"
                  label="E-mail"
                  outlined
                  dense
                  clearable
                ></v-text-field
              ></v-col>
              <v-col cols="12">
                <v-text-field
                  v-model="password"
                  label="Password"
                  dense
                  outlined
                  @click:append="show1 = !show1"
                  :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                  :type="show1 ? 'text' : 'password'"
                  clearable
                ></v-text-field></v-col
              ><v-row
                ><v-spacer></v-spacer
                ><v-col class="ml-16"
                  ><v-btn
                    elevation="2"
                    outlined
                    class="mr-4"
                    rounded
                    @click="goToLogin"
                    >Login</v-btn
                  ><v-btn elevation="2" outlined rounded @click="save"
                    >Save</v-btn
                  ></v-col
                ></v-row
              >
              <v-row>
                <v-alert
                  class="ml-8"
                  v-if="alert"
                  dense
                  outlined
                  v-model="alert"
                  type="success"
                >
                  User added <strong>successfully</strong>
                </v-alert>
                <v-alert
                  class="ml-8"
                  v-if="alertDanger"
                  dense
                  outlined
                  v-model="alert"
                  type="error"
                >
                  User name or email <strong>already used</strong>
                </v-alert></v-row
              >
            </v-card>
          </v-col>
        </v-row>
      </v-form>
    </v-main>
  </v-app>
</template>

<script>
import axios from "axios";
/* eslint-disable */
import NavBar from "../components/NavBar.vue";
export default {
  name: "Register",
  data() {
    return {
      alertDanger: false,
      valid: false,
      show1: false,
      alert: false,
      email: null,
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
    goToLogin() {
      this.$router.push("/login");
      this.alert = false;
      this.alertDanger = false;
    },
    save() {
      let user = {
        username: this.name,
        password: this.password,
        email: this.email,
      };
      axios
        .post("http://localhost:8000/api/register/", user)
        .then((response) => {
          if (response.status === 200) {
            this.alert = true;

            this.alertDanger = false;
            this.$refs.form.reset();
          } else {
            this.alertDanger = true;
            this.alert = false;
          }
          console.log(response);
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
