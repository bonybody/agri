<template>
  <p class="menu-label">
  <slot></slot>
  </p>
</template>

<script>
export default {
  name: "AppMenuLabel"
}
</script>

<style scoped lang="scss">
.menu-label {
  font-size: $semi-large-font-size;
  font-weight: bold;
  margin-bottom: $min-parts-margin;
}
</style>