<template>
  <div class="login-form">
    <h2 class="login-form__title">ログイン</h2>
    <email-form v-model="email"/>
    <password-form v-model="password"/>
    <app-form-button @my-click="login()">ログイン</app-form-button>
  </div>
</template>

<script>
import AppInputText from "~/components/atoms/forms/AppInputText";
import EmailForm from "~/components/molecules/form/EmailForm";
import PasswordForm from "~/components/molecules/form/PasswordForm";
import AppFormButton from "~/components/atoms/forms/AppFormButton";

export default {
  name: "LoginForm",
  components: {AppFormButton, PasswordForm, EmailForm, AppInputText},
  data() {
    return {
      password: 'user1',
      email: 'user1'
    }
  },
  methods: {
    async login() {
      await this.$myAuth.login(this.email, this.password)
    }
  }

}
</script>

<style lang="scss" scoped>
.login-form {
  display: block;
  width: 300px;
  @include border-radius-box()
  box-sizing: content-box;
  padding: 25px;
}

.login-form > div, button {
  margin: 20px 0;
}

.login-form__title {
  font-size: 2rem;
  text-align: center;
  font-weight: bold;
}
</style>