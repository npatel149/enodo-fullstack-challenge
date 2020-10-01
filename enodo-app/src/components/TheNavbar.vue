<template>

  <el-menu
    :default-active="activeIndex"
    class="el-menu-demo"
    mode="horizontal"
    @select="handleSelect"
    background-color="#545c64"
    text-color="#fff"
    active-text-color="#ffd04b">
    <el-menu-item index="2">
      <router-link :to="{name:'Home'}"><img src="../assets/logo_green.svg" height="40px" alt="enodo_logo"/></router-link>
    </el-menu-item>
    <el-menu-item index="3">
      <router-link :to="{name:'PropertyList'}">Property</router-link>
    </el-menu-item>
    <el-menu-item index="4">
      <router-link :to="{name:'PropertyListTable'}">Selected</router-link>
    </el-menu-item>
    <el-menu-item index="5">
      <router-link :to="{name:'About'}">About</router-link>
    </el-menu-item>
  </el-menu>
</template>

<script>
  export default {
    data() {
      return {
        activeIndex: '1',
        activeIndex2: '1'
      };
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
</script>

<style>
  a:link {
    text-decoration: none;
  }
</style>