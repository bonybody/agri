<template>
  <input
      class="input__text"
      type="password"
      :name="name"
      :value="value"
      :placeholder="placeholder"
  >
</template>

<script>
export default {
  name: "AppInputPassword",
  props: {
    name: {
      type: String,
      default: "password"
    },
    value: {
      type: String,
      default: ""
    },
    placeholder: {
      type: "",
      default: "文字を入力してください。"
    }
  },
  computed: {
    inputValue: {
      get() {
        return this.value;
      },
      set(value) {
        this.$emit('input', value);
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.input__text {
  display: block;
  height: 30px;
  width: 100%;
  padding: 8px;
  text-align: left;
  color: $main-font-color;
  background-color: $main-background-color;
  @include border-radius-box()
}
</style>