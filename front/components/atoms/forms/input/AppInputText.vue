<template>
  <input
      class="input__text"
      :type="type"
      :name="name"
      v-model="inputValue"
      :placeholder="placeholder"
      :disabled="disabled"
  >
</template>

<script>
export default {
  name: "AppInputText",
  props: {
    name: {
      type: String,
      default: "text"
    },
    value: {
      type: String | Number,
      default: ""
    },
    placeholder: {
      type: "",
      default: "文字を入力してください。"
    },
    type: {
      type: String,
      default: 'text'
    },
    disabled: {
      type: Boolean,
      default: false
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
  padding: 0 8px;
  text-align: left;
  color: $main-font-color;
  background-color: $main-background-color;
  @include border-radius-box()
}
</style>