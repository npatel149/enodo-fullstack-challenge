<template>
  <div>
    <div class="wrapper">
      <el-input placeholder="Search By Address" v-model="search"></el-input>
      <div v-for="propertyInfo in propertyList" :key="propertyInfo.id">
        <PropertyCard :property-info="propertyInfo"/>
      </div>
    </div>
  </div>
</template>

<script>

  import PropertyCard from "./PropertyCard";

  export default {
    data() {
      return {
        search: '',
      };
    },
    components: {
      PropertyCard,
    },
    computed: {
      // search() {
      //   return this.$store.state.search;
      // },
      propertyList() {
        if (this.search) {
          this.$store.commit('SEARCH_BY_KEYWORD', this.parentsearch);
          return this.$store.getters.filteredList;
        }
        return this.$store.getters.propertyList;
      },
    },
    mounted() {
      if (!this.propertyList) {
        this.$store.dispatch('fetchPropertyList');
      }
    },
  }
</script>

<style lang="scss">

  .wrapper {
    display: flex;
    margin: 0 auto;
    max-width: 1200px;
    flex-wrap: wrap;
    padding-top: 12px;
    justify-content: center;
    align-items: center;
  }

</style>