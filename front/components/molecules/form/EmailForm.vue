<template>
  <div class="email-form">
    <p class="email-form__label">
      <label for="email">メールアドレス</label>
    </p>
    <app-input-text
        :type="'email'"
        :name="'email'"
        :placeholder="'メールアドレスを入力してください。'"
        v-model="inputValue"
    />

  </div>
</template>

<script>
import AppInputText from "~/components/atoms/forms/AppInputText";

export default {
  name: "EmailForm",
  components: {AppInputText},
  props: {
    value: {
      type: String,
      default: ''
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