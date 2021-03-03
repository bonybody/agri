<template>
  <input
      class="input-check"
      type="checkbox"
      v-model="inputValue"
  ></input>
</template>

<script>
import Input from "~/mixins/input";
import input from "~/mixins/input";
export default {
  name: "AppInputCheckbox",
  components: {Input},
  mixins: [input],
  props: {
    required: {
      type: Boolean,
      default: true
    }
  }
}
</script>

<style scoped lang="scss">
.input-check {
  height: 100%;
  width: 100%;
  @include border-radius-box()

}
</style>