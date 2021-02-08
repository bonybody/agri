<template>
  <p class="error-message">
    <slot></slot>
  </p>
</template>

<script>
export default {
  name: "AppErrorMessage"
}
</script>

<style scoped lang="scss">
.error-message {
  color: $accent-color;
  margin-bottom: 3px;
}
</style>