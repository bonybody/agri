<template>
  <button
      class="link-button"
      @click="$emit('myClick')"
  >
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: "AppButton",
}
</script>

<style scoped lang="scss">
.link-button {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  background-color: $primary-color;
  color: $primary-on-font-color;
  text-align: center;
  vertical-align: middle;
  border: 2px solid $primary-color;
  border-radius: 1000px;
}

</style>