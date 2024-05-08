<template>
  <div class="page-wrapper">
    <AltNav v-if="$store.state.user.isAuthenticated" />
    <router-view class="content-wrapper" />
    <Footer v-if="$store.state.user.isAuthenticated" />
  </div>
</template>

<style scoped>
.page-wrapper {
  display: flex;
  min-height: 100vh;
  flex-direction: column;
}

.content-wrapper {
  flex: 1;
}
</style>

<style lang="scss">
$family-sans-serif: "Arial", "Tahoma", sans-serif;
// Import Bulma's core
@import "~bulma/sass/utilities/_all";
// Set your colors
$primary: #e7cf6e;
$primary-light: findLightColor($primary);
$primary-dark: findDarkColor($primary);
$primary-invert: findColorInvert($primary);

// Setup $colors to use as bulma classes (e.g. 'is-twitter')
$colors: mergeColorMaps(("white": ($white,
        $black,
      ),
      "black": ($black,
        $white,
      ),
      "light": ($light,
        $light-invert,
      ),
      "dark": ($dark,
        $dark-invert,
      ),
      "primary": ($primary,
        $primary-invert,
        $primary-light,
        $primary-dark,
      ),
      "link": ($link,
        $link-invert,
        $link-light,
        $link-dark,
      ),
      "info": ($info,
        $info-invert,
        $info-light,
        $info-dark,
      ),
      "success": ($success,
        $success-invert,
        $success-light,
        $success-dark,
      ),
      "warning": ($warning,
        $warning-invert,
        $warning-light,
        $warning-dark,
      ),
      "danger": ($danger,
        $danger-invert,
        $danger-light,
        $danger-dark,
      ),
    ),
    $custom-colors);

$link: $primary;
$link-invert: $primary-invert;
$link-focus-border: $primary;

// Import Bulma and Buefy styles
@import "~bulma";
@import "~buefy/src/scss/buefy";
</style>




<script>

import Footer from '@/components/Footer'
import axios from 'axios'
import AltNav from '@/components/AltNav.vue';


export default {
  name: 'App',
  components: {
    Footer,
    AltNav
  },
  beforeCreate() {
    console.log('Инициализация')
    this.$store.commit('initializeStore')
    const token = this.$store.state.user.token
    if (token) {
      axios.defaults.headers.common['Authorization'] = 'Token ' + token
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  }
}
</script>