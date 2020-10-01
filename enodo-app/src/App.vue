<template>
  <div id="app">
    <TheNavbar/>
    <router-view :key="$route.path"/>
    <TheFooter />
  </div>
</template>

<script>
  import TheNavbar from '@/components/TheNavbar.vue';
  import TheFooter from '@/components/TheFooter.vue';

  export default {
    components: {
      TheNavbar,
      TheFooter
    },
    mounted() {
      this.$store.dispatch('fetchPropertyList');
    }
  }
</script>

<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

</style>
