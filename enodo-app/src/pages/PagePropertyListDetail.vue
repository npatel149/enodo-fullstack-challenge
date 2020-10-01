<template>
  <div class="wrapper">
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>Property Details for {{ address }}</span>
      </div>
      <img :alt=propertyObj.id :src="`https://robohash.org/${propertyObj.id}?400x400`"/>
      <div v-for="(key, value, count) in propertyObj" :key="count" class="text item">
        {{ value }}: {{ key }}
      </div>
      <div @click="toggleIsSelected()">
        <el-button
          type="primary"
          class="button"
          v-if="!is_selected"
          round>Select
        </el-button>
        <el-button
          type="success"
          class="button"
          v-else
          round>Selected
        </el-button>
      </div>
    </el-card>
  </div>

</template>

<script>
  export default {
    props: {
      id: {
        type: String,
        required: true,
      },
      propertyData: {
        type: Object,
        required: false,
      },
    },
    computed: {
      propertyObj() {
        if (this.propertyData) {
          return this.propertyData;
        }
        return this.$store.getters.propertyList.find(obj => String(obj.id) === this.id);
      },
      address() {
        return this.propertyObj ? this.propertyObj.full_address : '';
      },
      is_selected() {
        return this.propertyObj ? this.propertyObj.is_selected : false;
      }
    },
    methods: {
      toggleIsSelected() {
        this.$store.dispatch('toggleIsSelected', this.propertyObj);
      },
    },
  };
</script>
<style>
  .text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 18px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }

  .clearfix:after {
    clear: both
  }

  .box-card {
    width: 480px;
  }

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