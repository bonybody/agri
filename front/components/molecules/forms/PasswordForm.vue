<template>
  <div class="password-form">
    <div class="password-form__label">
      <app-form-label :name="'password'">パスワード</app-form-label>
      <app-require-mark v-show="require"/>
    </div>
    <app-input-text
        :type="'password'"
        :name="'password'"
        :placeholder="'パスワードを入力してください。'"
        v-model="inputValue"
    />
    <app-error-message>{{ error }}</app-error-message>
  </div>
</template>

<script>
import AppInputText from "~/components/atoms/forms/input/AppInputText";
import AppFormLabel from "~/components/atoms/forms/label/AppFormLabel";
import input from "~/mixins/input";
import AppRequireMark from "~/components/atoms/forms/marks/AppRequireMark";
import AppErrorMessage from "~/components/atoms/forms/error/AppErrorMessage";

export default {
  name: "PasswordForm",
  components: {AppErrorMessage, AppRequireMark, AppFormLabel, AppInputText},
  mixins: [input],
  props: {
    require: {
      type: Boolean,
      default: false
    },
    error: {
      type: String,
      default: null
    }
  }
}
</script>

<style scoped lang="scss">
.password-form {
  @include form-section-mixin();
  &__label {
    @include left-right-alignment-mixin;
  }
}
</style>