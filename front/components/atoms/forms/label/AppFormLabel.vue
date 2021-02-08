<template>
  <label class="myLabel" :for="name">
    <slot></slot>
  </label>
</template>

<script>
export default {
  name: "AppFormLabel",
  props: {
    name: {
      type: String,
      default: ''
    }
  }
}
</script>

<style scoped lang="scss">
.myLabel {
  display: inline-block;
  margin-bottom: 5px;
  font-weight: bold;
  color: $main-font-color;
}
</style>