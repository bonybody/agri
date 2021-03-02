<template>
<div class="form-parts">
  <div class="form-parts__heading">
    <div class="form-parts__label">
      <app-form-label :name="'image'">プロフィール画像</app-form-label>
    </div>
    <div class="form-parts__require">
      <app-require-mark v-show="require" />
    </div>
  </div>
  <div class="form-parts__input">
    <app-input-image @changeValue="change($event)"/>
  </div>
  <div class="form-parts__error">
    <app-error-message>{{ error }}</app-error-message>
  </div>
</div>
</template>

<script>
import AppFormLabel from "~/components/atoms/forms/label/AppFormLabel";
import AppRequireMark from "~/components/atoms/forms/marks/AppRequireMark";
import AppInputImage from "~/components/atoms/forms/input/AppInputImage";
import AppErrorMessage from "~/components/atoms/forms/error/AppErrorMessage";
export default {
name: "UserImageForm",
  components: {AppErrorMessage, AppInputImage, AppRequireMark, AppFormLabel},
  props: {
    require: {
      type: Boolean,
      default: false
    },
    error: {
      type: String,
      default: ''
    }
  },
  methods: {
    change(event) {
      this.$emit('input', event)
    }
  }

}
</script>

<style scoped lang="scss">
.form-parts {
  @include form-section-mixin;
  &__heading {
    @include left-right-alignment-mixin;
  }
  &__input {
    width: 100%;
    height: 200px;
  }
}

</style>