<template>
  <div class="user-name-form">
    <div class="user-name-form__label">
      <app-form-label :name="'display_name'">商品説明</app-form-label>
      <app-require-mark v-show="require"/>
    </div>
    <div class="user-name-form__input">
      <app-text-area
          v-model="inputValue"
          :placeholder="'商品の説明'"
          :name="'item_description'"
      />
    </div>
    <app-error-message>{{ error }}</app-error-message>
  </div>
</template>

<script>
import AppInputText from "~/components/atoms/forms/input/AppInputText";
import AppFormLabel from "~/components/atoms/forms/label/AppFormLabel";
import input from "~/mixins/input";
import AppRequireMark from "~/components/atoms/forms/marks/AppRequireMark";
import AppErrorMessage from "~/components/atoms/forms/error/AppErrorMessage";
import AppTextArea from "~/components/atoms/forms/textarea/AppTextArea";

export default {
  name: "ItemDescriptionForm",
  components: {AppTextArea, AppErrorMessage, AppRequireMark, AppFormLabel, AppInputText},
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

  &__input {
    width: 100%;
    height: 50px;
  }
}
</style>