<template>
  <div class="wrapper">
      <el-col :span="12">
        <div class="sub-title">list suggestions when activated</div>
        <el-autocomplete
          class="inline-input"
          v-model="search"
          :fetch-suggestions="querySearch"
          placeholder="Please Input"
          @select="handleSelect"
        ></el-autocomplete>
      </el-col>
    <el-input placeholder="Search By Address" v-model="search"></el-input>
    <div v-for="propertyInfo in propertyList" :key="propertyInfo.id">
      <PropertyCard :property-info="propertyInfo"/>
    </div>
  </div>
</template>

<script>
  import PropertyCard from "./PropertyCard";

  export default {
    components: {
      PropertyCard,
    },
    data() {
      return {
        links: [],
        search: '',
      };
    },
    computed: {
      propertyList() {
        if (this.search) {
          this.$store.commit('SEARCH_BY_KEYWORD', this.search);
          return this.$store.getters.filteredList;
        }
        return this.$store.getters.propertyList;
      },
    },
    methods: {
      querySearch(queryString, cb) {
        var links = this.links;
        var results = queryString ? links.filter(this.createFilter(queryString)) : links;
        cb(results);
      },
      createFilter(queryString) {
        return (link) => {
          return (link.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
        };
      },
      loadAll() {
        let links = this.$store.getters.propertyList;
        let i;
        for (i = 0; i < links.length; i++) {
          links[i]['value'] = links[i]['full_address'];
        }
        return links
      },
      handleSelect(item) {
        console.log(item);
      },
    },
    mounted() {
      if (!this.propertyList) {
        this.$store.dispatch('fetchPropertyList');
      }
      this.links = this.$store.getters.suggestionsLinks;
    }
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