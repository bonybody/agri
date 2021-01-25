<template>
  <nuxt-link :to="to" class="link" :class="{'primary': primary, 'notPrimary': !primary }">
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
    },
    primary: {
      type: Boolean,
      default: false
    }
  },
}
</script>

<style scoped lang="scss">
.link {
  @include center-flex();
  height: 30px;
  font-size: 14px;
  font-weight: bold;
  vertical-align: middle;
  padding: 0 10px;
}

.primary {
  color: $primary-on-font-color;
  background-color: $primary-color;
  @include border-radius-box($primary-color);
}

.notPrimary {
  color: $main-font-color;
  @include border-radius-box($main-font-color);
}

</style>