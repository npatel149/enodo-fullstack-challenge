<template>
  <div>
    <h2>Find Best Property!</h2>
    <PropertySearchSuggestions/>
  </div>
</template>

<script>
  import PropertySearchSuggestions from '@/components/PropertySearchSuggestions.vue';

  export default {
    components: {
      PropertySearchSuggestions,
    },
  };
</script>
