<template>
  <textarea class="text-area"
            v-model="inputValue"
            :name="name"
            :placeholder="placeholder"
  >

  </textarea>
</template>

<script>
import input from "~/mixins/input";

export default {
  name: "AppTextArea",
  mixins: [input],
  props: {
    name: {
      type: String,
      default: ''
    },
    placeholder: {
      type: String,
      default: ''
    }
  }
}
</script>

<style scoped lang="scss">
.text-area {
  height: 100%;
  width: 100%;
  color: $main-font-color;
  background-color: $main-background-color;
  @include border-radius-box()

}
</style>