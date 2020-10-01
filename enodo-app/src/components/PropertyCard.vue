<template>
  <el-card shadow="hover" class="card" @click="handleDetail">
    <div @click="handleDetail">
    <a v-bind:href="propertyInfo.link" target="_blank">
<!--      <img :alt=propertyInfo.id src="../assets/logo.png"/>-->
      <img :alt=propertyInfo.id :src="`https://robohash.org/${propertyInfo.id}?200x200`"/>

      <small>posted by: Enodo {{ propertyInfo.city }}</small>
      {{ propertyInfo.full_address }}
    </a>
    </div>
    <div @click="toggleIsSelected()">
      <el-button
      type="primary"
      class="button"
      v-if="!propertyInfo.is_selected"
      round id="select_button">Select</el-button>
      <el-button
      type="success"
      class="button"
      v-else
      round id="selected_button">Selected</el-button>

    </div>

  </el-card>
</template>

<script>
  export default {
    props: {
      propertyInfo: {
        type: Object,
        required: true,
      }
    },
    methods: {
      toggleIsSelected() {
        this.$store.dispatch('toggleIsSelected', this.propertyInfo);
      },
      handleDetail() {
        this.$router.push({ name: 'PropertyListDetail', params: { id: String(this.propertyInfo.id) }})
      }
    },
  };
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

  .card {
    box-shadow: rgba(0, 0, 0, 0.117647) 0px 1px 6px, rgba(0, 0, 0, 0.117647) 0px 1px 4px;
    max-width: 200px;
    margin: 12px;
    transition: .15s all ease-in-out;
    display: inline-block;

    &:hover {
      transform: scale(1.1);
    }

    a {
      text-decoration: none;
      padding: 12px;
      color: #03A9F4;
      font-size: 24px;
      display: flex;
      flex-direction: column;
      align-items: center;

      img {
        height: 200px;
      }

      small {
        font-size: 10px;
        padding: 4px;
      }
    }
  }

  .hotpink {
    background: hotpink;
  }

  .green {
    background: green;
  }

  .box {
    width: 100px;
    height: 100px;
    border: 1px solid rgba(0, 0, 0, .12);
  }
</style>