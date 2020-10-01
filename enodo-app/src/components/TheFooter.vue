<template>
  <el-container>
    <el-footer>
      <router-link :to="{name:'Home'}">
        <img
          src="../assets/wordmark_logo_wht.svg"
          alt="enodo_logo"
          height="50px" /> </router-link>
      © 2020 Enodo. All Right Reserved | Terms and Conditions
    </el-footer>
  </el-container>
</template>

<style scoped>
  .el-footer {
  background-color: #263238 !important;
  color: #6A6A6A;
  text-align: center;
  line-height: 60px;
  }
</style>
