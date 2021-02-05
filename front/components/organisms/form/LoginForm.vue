<template>
  <div class="login-form">
    <app-form-heading>ログイン</app-form-heading>
    <email-form v-model="email"/>
    <password-form v-model="password"/>
    <app-form-button @my-click="login()">ログイン</app-form-button>
  </div>
</template>

<script>
import AppInputText from "~/components/atoms/forms/input/AppInputText";
import EmailForm from "~/components/molecules/form/EmailForm";
import PasswordForm from "~/components/molecules/form/PasswordForm";
import AppFormButton from "~/components/atoms/forms/button/AppFormButton";
import AppFormHeading from "~/components/atoms/headings/AppFormHeading";

export default {
  name: "LoginForm",
  components: {AppFormHeading, AppFormButton, PasswordForm, EmailForm, AppInputText},
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
  @include form-box-style;
}
</style>