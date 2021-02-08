<template>
  <select class="app-select" v-model="inputValue" :name="name">
    <slot></slot>
  </select>
</template>

<script>
import input from "~/mixins/input";

export default {
  name: "AppSelect",
  mixins: [ input ],
  props: {
    name: {
      type: String,
      default: 'select'
    }
  }
}
</script>

<style scoped lang="scss">
.app-select {
  display: block;
  height: 30px;
  padding: 0 8px;
  text-align: left;
  color: $main-font-color;
  background-color: $main-background-color;
  appearance: auto;
  @include border-radius-box();
}
</style>