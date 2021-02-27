<template>
  <div class="item-image-form">
    <div class="item-image-form__heading">
      <div class="item-image-form__label">
        <app-form-label :name="'image'">商品画像</app-form-label>
      </div>
      <div class="item-image-form__require">
        <app-require-mark v-show="!require"/>
      </div>
    </div>
    <div class="item-image-form__input">
      <app-input-image v-model="inputValue" />
    </div>
    <div class="item-image-form__error">
      <app-error-message>{{ error }}</app-error-message>
    </div>
  </div>
</template>

<script>
import AppFormLabel from "~/components/atoms/forms/label/AppFormLabel";
import AppRequireMark from "~/components/atoms/forms/marks/AppRequireMark";
import AppInputImage from "~/components/atoms/forms/input/AppInputImage";
import AppErrorMessage from "~/components/atoms/forms/error/AppErrorMessage";
import input from "~/mixins/input";

export default {
  name: "ItemImageForm",
  components: {AppErrorMessage, AppInputImage, AppRequireMark, AppFormLabel},
  mixins: [input],
  props: {
    require: {
      type: Boolean,
      default: false
    },
    error: {
      type: String,
      default: ''
    }
  }
}
</script>

<style scoped lang="scss">
.item-image-form {
  @include form-section-mixin;

  &__heading {
    @include left-right-alignment-mixin;
  }
  &__input {
    width: 100px;
    height: 50px;

  }
}
</style>