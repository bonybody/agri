<template>
  <input
      class="input__text"
      type="text"
      :name="name"
      :value="value"
      :placeholder="placeholder"
  >
</template>

<script>
export default {
  name: "AppInputText",
  props: {
    name: {
      type: String,
      default: ""
    },
    value: {
      type: String,
      default: ""
    },
    placeholder: {
      type: "",
      default: "文字を入力してください。"
    }
  }
}
</script>

<style lang="scss" scoped>
.input__text {
  display: block;
  width: 100%;
  padding: 8px;
  text-align: left;
  color: $main-font-color;
  background-color: $main-background-color;
  @include border-radius-box()
}
</style>