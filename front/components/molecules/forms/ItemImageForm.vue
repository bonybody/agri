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
    <div class="item-image-form__input-box">
      <template v-for="(image, index) in images">
        <div class="item-image-form__input" :key="index">
          <app-input-image @changeValue="change($event, index)"/>
        </div>
      </template>
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
  data() {
    return {
      images: [
        null,
        null,
        null,
        null,
        null
      ]
    }
  },
  methods: {
    change(event, index) {
      this.images[index] = event
      this.$emit('input', this.images)
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

  &__input-box {
    overflow-x: auto;
    white-space: nowrap;
    -webkit-overflow-scrolling: touch;
    padding: 0;
  }

  &__input {
    width: 200px;
    height: 200px;
    margin-right: $medium-parts-margin;
    display: inline-block;
  }
}
</style>