<template>
  <div class="email-form">
    <div class="email-form__label">
    <app-form-label :name="'email'">メールアドレス</app-form-label>
      <app-require-mark v-show="require"/>
    </div>
    <app-input-text
        :type="'email'"
        :name="'email'"
        :placeholder="'メールアドレスを入力してください。'"
        v-model="inputValue"
    />

  </div>
</template>

<script>
import AppInputText from "~/components/atoms/forms/input/AppInputText";
import AppFormLabel from "~/components/atoms/forms/label/AppFormLabel";
import input from "~/mixins/input";
import AppRequireMark from "~/components/atoms/forms/marks/AppRequireMark";

export default {
  name: "EmailForm",
  components: {AppRequireMark, AppFormLabel, AppInputText},
  mixins: [input],
  props: {
    require: {
      type: Boolean,
      default: false
    }
  }
}
</script>

<style scoped lang="scss">
.email-form {
  @include form-section-mixin;
  &__label {
    @include left-right-alignment-mixin;
  }
}
</style>