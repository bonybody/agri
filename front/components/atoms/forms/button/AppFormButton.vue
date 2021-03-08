<template>
    <button class="form-button" :class="{disable: disabled}" type="submit" @click="myClick()">
      <slot></slot>
    </button>
</template>

<script>
export default {
  name: "AppFormButton",
  props: {
    disabled: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    myClick() {
      this.$emit('my-click')
    }
  }
}
</script>

<style scoped lang="scss">
.form-button {
  text-align: center;
  height: 40px;
  border-radius: 4px;
  width: 100%;
  background-color: $primary-color;
  color: $primary-on-font-color;

  &:hover {
    opacity: $hover-opacity;
  }
}

.disable {
  pointer-events: none;
  background-color: $weak-font-color;
}
</style>