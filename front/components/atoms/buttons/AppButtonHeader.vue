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
  display: block;
  line-height: 30px;
  margin: 0 10px;
  border: 1px solid $main-font-color;
  border-radius: 10px;
  color: $main-font-color;
  padding: 0 10px;
}
</style>