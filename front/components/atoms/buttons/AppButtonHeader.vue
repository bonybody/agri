<template>
  <nuxt-link :to="to" class="link">
    <slot></slot>
  </nuxt-link>
</template>

<script>
export default {
  name: "AppButtonHeader",
  props: {
    to: {
      type: String,
      default: '/'
    }
  }
}
</script>

<style scoped lang="scss">
.link {
  @include center-flex();
  @include border-radius-box;
  height: 30px;
  vertical-align: middle;
  color: $main-font-color;
  padding: 0 10px;
}
</style>