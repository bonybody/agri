<template>
  <h2 class="form-heading"><slot></slot></h2>
</template>

<script>
export default {
  name: "AppFormHeading"
}
</script>

<style scoped>
.form-heading {
  font-size: 2rem;
  text-align: center;
  font-weight: bold;
  margin-bottom: 30px;
}

</style>