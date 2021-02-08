<template>
  <div class="user-name-form">
    <div class="user-name-form__label">
      <app-form-label :name="'display_name'">表示名</app-form-label>
      <app-require-mark v-show="require"/>
    </div>
    <app-input-text
        :type="'text'"
        :placeholder="'１５文字以内で入力してください。'"
        :name="'display_name'"
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
  name: "DisplayNameForm",
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
.user-name-form {
  @include form-section-mixin;

  &__label {
    @include left-right-alignment-mixin;
  }
}
</style>