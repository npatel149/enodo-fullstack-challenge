<template>
  <el-table
    :data="tableData"
  >
    <el-table-column
      prop="full_address"
      label="Full Address"
      width="300">
    </el-table-column>
    <el-table-column
      prop="class_description"
      label="Class Description"
      width="300">
    </el-table-column>
    <el-table-column
      label="Operations"
      width="250">
      <template slot-scope="scope">
        <el-button
          size="mini"
          @click="handleDetail(scope.$index, scope.row)">Detail</el-button>
        <el-button
          size="mini"
          type="danger"
          @click="handleDelete(scope.$index, scope.row)">Delete</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
  export default {
    computed: {
      tableData() {
          return this.$store.state.propertyinfo.selectedPropertyList;
        }
    },
    mounted() {
      if (!this.tableData) {
        this.$store.dispatch('fetchPropertyList');
      }
    },
    methods: {
      handleDetail(index, row) {
        console.log(index, row);
        this.$router.push({ name: 'PropertyListDetail', params: { id: String(row.id) }})
      },
      handleDelete(index, row) {
        console.log(index, row);
        this.$store.dispatch('toggleIsSelected', row);
      }
    },
  }
</script>