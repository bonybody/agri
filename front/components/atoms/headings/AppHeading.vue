<template>
  <p class="heading"><slot></slot></p>

</template>

<script>
export default {
name: "AppHeading"
}
</script>

<style scoped lang="scss">
.heading {
  font-size: $large-font-size;
  font-weight: bold;
}

</style>