<template>
    <v-navigation-drawer
      v-model="drawer"
      :mini-variant.sync="mini"
      dark
      permanent
      class="py-7"
      app
    >
      <v-list-item class="px-3">
        <v-list-item-avatar>
          <v-img src="https://randomuser.me/api/portraits/lego/0.jpg"></v-img>
        </v-list-item-avatar>

        <v-list-item-title>John Doe</v-list-item-title>

        <v-btn
          icon
          @click.stop="mini = !mini"
        >
          <v-icon>mdi-chevron-left</v-icon>
        </v-btn>
      </v-list-item>

      <v-divider></v-divider>

      <v-list dense>
        <v-list-item
          v-for="item in items"
          :key="item.title"
          :to="item.path"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
</template>

<script>
  export default {
    data () {
      return {
        drawer: true,
        items: [
          { title: 'Dashboard', icon: 'fa-solid fa-house-crack', path: '/' },
          { title: 'Subdomain Discover', icon: 'fa-solid fa-subscript', path: '/subdomain' },
          { title: 'Create Wordlist', icon: 'fa-solid fa-folder-open', path: '/createWordlist' },
        ],
        mini: true,
      }
    },
  }
</script>

