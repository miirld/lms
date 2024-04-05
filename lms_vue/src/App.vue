<template>
  <Nav v-if="$store.state.user.isAuthenticated" />
  <router-view />
  <Footer v-if="$store.state.user.isAuthenticated"/>
</template>


<script>
import Nav from '@/components/Nav'
import Footer from '@/components/Footer'
import axios from 'axios'
export default {
  name: 'App',
  components: {
    Nav,
    Footer,
  },
  methods: {
    authInit() {

    }

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
    //   console.log(this.$store.state.user.isAuthenticated)
    //   if (!this.$store.state.user.isAuthenticated) {

    //   this.$router.push('/log-in')
    // }
    
  }
}
</script>

<style lang="scss">
@import '../bulma-custom.css';
</style>
