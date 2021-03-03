<template>
  <select class="app-select" v-model="inputValue" :name="name">
    <template v-for="(option, index) in options">
      <option :value="option.value">{{ option.label }}</option>
    </template>
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
    },
    options: {
      type: Array,
      require: false
    }
  }
}
</script>

<style scoped lang="scss">
.app-select {
  display: block;
  width: 100%;
  height: 30px;
  padding: 0 8px;
  text-align: left;
  color: $main-font-color;
  background-color: $main-background-color;
  appearance: auto;
  @include border-radius-box();
}
</style>