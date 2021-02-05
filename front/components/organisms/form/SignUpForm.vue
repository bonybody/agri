<template>
  <div class="sign-up-form">
    <app-form-heading>新規登録</app-form-heading>
    <user-name-form v-model="userName"/>
    <email-form v-model="email" />
    <password-form v-model="password" />
    <app-separation/>
    <app-form-button>新規登録</app-form-button>
  </div>
</template>

<script>
import AppFormHeading from "~/components/atoms/headings/AppFormHeading";
import UserNameForm from "~/components/molecules/form/UserNameForm";
import EmailForm from "~/components/molecules/form/EmailForm";
import PasswordForm from "~/components/molecules/form/PasswordForm";
import AppFormButton from "~/components/atoms/forms/button/AppFormButton";
import AppSeparation from "~/components/atoms/ separations/AppSeparation";

export default {
  name: "SignUpForm",
  components: {AppSeparation, AppFormButton, PasswordForm, EmailForm, UserNameForm, AppFormHeading},
  data() {
    return {
      userName: '',
      email: '',
      password: ''
    }
  }
}
</script>

<style scoped lang="scss">
.sign-up-form {
  @include form-box-style();
}
</style>