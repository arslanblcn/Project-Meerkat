<template>
    <div>
        <v-toolbar extended>
            <img class="mt-8 ml-12" :src="require('../assets/logo.png')" height="80"/>

            <v-spacer></v-spacer>

            <v-btn icon class="mt-8">
                <v-icon>mdi-magnify</v-icon>
            </v-btn>
                <v-btn icon @click="toggle_dark_mode" class="mt-8">
                    <v-icon>mdi-theme-light-dark</v-icon>
            </v-btn>
        </v-toolbar>
    </div>
</template>
<script>
export default {
    name: "NavigationBar",
    methods: {
        toggle_dark_mode: function() {
            this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
            localStorage.setItem("dark_theme", this.$vuetify.theme.dark.toString());
        }
    },
    mounted() {
        const theme = localStorage.getItem("dark_theme");
        if (theme) {
            if (theme === "true") {
                this.$vuetify.theme.dark = true;
            } else {
                this.$vuetify.theme.dark = false;
            }
        } else if (
            window.matchMedia &&
            window.matchMedia("(prefers-color-scheme: dark)").matches
        ) {
            this.$vuetify.theme.dark = true;
            localStorage.setItem(
                "dark_theme",
                this.$vuetify.theme.dark.toString()
            );
        }
    }
};
</script>
