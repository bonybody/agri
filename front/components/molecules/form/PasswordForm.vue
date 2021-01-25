<template>
  <div class="password-form">
    <label for="password">パスワード</label>
    <app-input-text
      :type="'password'"
      :name="'password'"
      :placeholder="'パスワードを入力してください。'"
      v-model="inputValue"
    />
  </div>
</template>

<script>
import AppInputText from "~/components/atoms/forms/AppInputText";
export default {
name: "PasswordForm",
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