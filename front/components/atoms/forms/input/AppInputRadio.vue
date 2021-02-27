<template>
  <div class="">
    <template v-for="(option, index) in options">
      <label :key="index">
        <input
            type="radio"
            :name="name"
            :value="option.value"
            @change="updateValue"
            :checked="index == 0"
        />{{ option.label }}
      </label>
    </template>
  </div>
</template>

<script>
export default {
  name: "AppInputRadio",
  props: {
    value: {
      type: String,
      require: true
    },
    options: {
      type: Array,
      require: true
    },
    name: {
      type: String,
      default: ''
    },
  },
  methods: {
    updateValue(e) {
      this.$emit('input', e.target.value)
    }
  }
}
</script>

<style scoped>
label {
  margin-right: 10px;

}
</style>