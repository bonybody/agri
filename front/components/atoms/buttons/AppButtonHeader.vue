<template>
  <div>
    <button v-if="type === 'button'" @click="$emit('myClick')" class="link"
            :class="{'primary': primary, 'notPrimary': !primary }">
      <slot></slot>
    </button>
    <nuxt-link v-if="type === 'link'" :to="to" class="link" :class="{'primary': primary, 'notPrimary': !primary }">
      <slot></slot>
    </nuxt-link>
  </div>
</template>

<script>
export default {
  name: "AppButtonHeader",
  props: {
    type: {
      type: String,
      default: 'button'
    },
    to: {
      type: String,
      default: '/'
    },
    primary: {
      type: Boolean,
      default: false
    },
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

  &:hover {
    opacity: $hover-opacity;
  }
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