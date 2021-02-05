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

<style scoped>
.myLabel {
  padding-bottom: 3px;
}
</style>