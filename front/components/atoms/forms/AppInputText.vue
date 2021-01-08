<template>
  <div>
    <input type="text"
           v-model="inputValue"
           :name="name"
           :maxlength="maxLength"
           :minlength="minLength"
           :placeholder="placeholder"
    >
  </div>
</template>

<script>
export default {
  name: "AppInputText",
  props: {
    value: {
      type: String,
      default: ''
    },
    name: {
      type: String,
      default: '',
    },
    maxLength: {
      type: Number,
      default: 100,
    },
    minLength: {
      type: Number,
      default: 0,
    },
    placeholder: {
      type: String,
      default: '文字を入力してください。'
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

<style scoped>

</style>