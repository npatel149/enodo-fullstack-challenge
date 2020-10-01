<template>
  <div class="home">
    <h1>To Get Other Attractive Properties.
      <el-button
        type="warning">
        <router-link
          :to="{name:'PropertyList'}"
        >
          Please, Click Here!
        </router-link>
      </el-button>
    </h1>
    <div>
      <PropertySearchSuggestions/>
    </div>
  </div>
</template>

<script>
  // @ is an alias to /src
  import PropertySearchSuggestions from "@/components/PropertySearchSuggestions.vue";

  export default {
    name: 'Home',
    components: {
      PropertySearchSuggestions,
    }
  }
</script>
