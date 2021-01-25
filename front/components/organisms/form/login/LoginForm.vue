<template>
  <div class="login-form">
    <app-input-text
        :name="'email'"
        :placeholder="'メールアドレスを入力してください。'"
    />
  </div>
</template>

<script>
import AppInputText from "~/components/atoms/forms/AppInputText";
export default {
name: "LoginForm",
  components: {AppInputText}
}
</script>

<style lang="scss" scoped>
.login-form {
  display: block;
  max-width: 500px;
  margin: 0 auto;
  @include border-radius-box()
  box-sizing: content-box;
  padding: 25px;
}
</style>