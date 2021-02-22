<template>
  <nuxt-link
      :to="link"
      class="link-button"
  >
    <slot></slot>
  </nuxt-link>
</template>

<script>
export default {
  name: "AppLinkButton",
  props: {
    link: {
      type: Object,
      default() {
        return {}
      }
    }
  },
  computed: {

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

</style>