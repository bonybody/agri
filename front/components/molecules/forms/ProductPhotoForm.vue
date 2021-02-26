<template>
  <div class="user-name-form">
    <div class="user-name-form__label">
      <app-form-label :name="'product_photo'">出品画像</app-form-label>
      <app-form-label-nobold :name="'product_photo'">最大5枚までアップロードできます。</app-form-label-nobold>
      <app-require-mark v-show="require"/>
    </div>
    <app-input-file
        :type="'file'"
        :name="'product_photo'"
        v-model="inputValue"
    />
    <app-error-message>{{ error }}</app-error-message>
  </div>
</template>

<script>
import AppInputFile from "~/components/atoms/forms/input/AppInputfile";
import AppFormLabel from "~/components/atoms/forms/label/AppFormLabel";
import AppFormLabel_nobold from '../../atoms/forms/label/AppFormLabel_nobold.vue';
import input from "~/mixins/input";
import AppRequireMark from "~/components/atoms/forms/marks/AppRequireMark";
import AppErrorMessage from "~/components/atoms/forms/error/AppErrorMessage";

export default {
  name: "ProductPhotoForm",
  components: {AppErrorMessage, AppRequireMark, AppFormLabel, AppFormLabel_nobold, AppInputFile},
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