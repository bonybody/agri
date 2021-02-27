<template>
  <div class="item-price-form">
    <div class="item-price-form__heading">
      <div class="item-price-form__label">
        <app-form-label :name="'price'">価格</app-form-label>
      </div>
      <div class="item-price-form__require">
        <app-require-mark v-show="require" />
      </div>
    </div>
    <div class="item-price-form__input">
      <app-input-text
          :type="'number'"
          :name="'price'"
          :placeholder="'0 ～ 50,000'"
          v-model="inputValue"
      ></app-input-text>
    </div>
    <div class="item-price-form__error">
      <app-error-message>{{ error }}</app-error-message>
    </div>
    <div class="item-price-form__fee fee">
      <span class="fee__label">
        手数料
      </span>
      <span class="fee__number">
        &yen;{{ value * 0.3 }}
      </span>
    </div>
    <div class="item-price-form__profit profit">
      <span class="profit__label">販売利益</span>
      <span class="profit__number">&yen;{{ value- ( value * 0.3 ) }}</span>
    </div>
  </div>
</template>

<script>
import AppFormLabel from "~/components/atoms/forms/label/AppFormLabel";
import AppInputText from "~/components/atoms/forms/input/AppInputText";
import input from "~/mixins/input";
import AppErrorMessage from "~/components/atoms/forms/error/AppErrorMessage";
import AppRequireMark from "~/components/atoms/forms/marks/AppRequireMark";
export default {
  name: "ItemPriceForm",
  components: {AppRequireMark, AppErrorMessage, AppInputText, AppFormLabel},
  mixins: [input],
  props:{
    error: {
      type: String,
      default: ''
    },
    require: {
      type: Boolean,
      default: false
    }
  }

}
</script>

<style scoped lang="scss">
.item-price-form {
  @include form-section-mixin;

  &__heading {
    @include left-right-alignment-mixin;
  }
}
</style>