<template>
  <div>
    <h2>Selected Best Properties!</h2>
    <div class="container">
      <PropertyTableSelected/>
    </div>
  </div>

</template>

<script>
  import PropertyTableSelected from "@/components/PropertyTableSelected.vue";

  export default {
    components: {
      PropertyTableSelected
    },
  };
</script>

<style>
  .container {
    display: flex;
    margin: auto auto;
    max-width: 60%;
    padding-top: 12px;
    justify-content: center;
    align-items: center;
  }
</style>