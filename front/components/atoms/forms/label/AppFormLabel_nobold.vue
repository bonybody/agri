<template>
  <label class="myLabel" :for="name">
    <slot></slot>
  </label>
</template>

<script>
export default {
  name: "AppFormLabelNoBold",
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
  color: $main-font-color;
}
</style>