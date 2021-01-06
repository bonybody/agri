<template>
  <button>
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: "AppHeaderButton"
}
</script>

<style scoped lang="scss">
button {
  display: inline-block;
  height: 40px;
  border: 1px solid $base-font-color;
  border-radius: 10px;
}
</style>