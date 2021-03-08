<template>
  <div class="login-form">
    <div>
      <app-form-heading>ログイン</app-form-heading>
    </div>
    <div class="login-form__form">
      <email-form v-model="email"/>
    </div>
    <div class="login-form__form">
      <password-form v-model="password"/>
    </div>
    <div class="login-form__button">
      <app-form-button @my-click="login()">ログイン</app-form-button>
    </div>
  </div>
</template>

<script>
import AppInputText from "~/components/atoms/forms/input/AppInputText";
import EmailForm from "~/components/molecules/forms/EmailForm";
import PasswordForm from "~/components/molecules/forms/PasswordForm";
import AppFormButton from "~/components/atoms/forms/button/AppFormButton";
import AppFormHeading from "~/components/atoms/headings/AppFormHeading";

export default {
  name: "LoginForm",
  components: {AppFormHeading, AppFormButton, PasswordForm, EmailForm, AppInputText},
  data() {
    return {
      email: 'guest0@test.com',
      password: 'password'
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
  @include form-box-style;
  &__form {
    margin-bottom: $semi-large-margin;
  }
}
</style>