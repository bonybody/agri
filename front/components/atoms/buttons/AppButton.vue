<template>
  <button
      type="button"
      class="link-button"
      :class="{ 'none': none }"
      @click="$emit('myClick')"
      :disabled="none"
  >
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: "AppButton",
  props: {
    none: {
      type: Boolean,
      default: false
    }
  }
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

.none {
  background-color: $weak-font-color;
  color: $primary-on-font-color;
  border-color: $weak-font-color;
}
</style>