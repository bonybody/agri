<template>
  <div class="delivery-fee-form">
    <div class="delivery-fee-form__heading">
      <div class="delivery-fee-form__label">
        <app-form-label :name="'delivery_fee'">配送料</app-form-label>
      </div>
      <div class="delivery-fee-form__require">
        <app-require-mark v-show="require"/>
      </div>
    </div>
    <div class="delivery-fee-form__input">
      <app-select v-model="inputValue" :options="deliveryFees" name="'delivery_fee'"></app-select>
    </div>
    <div class="delivery-fee-form__error">
      <app-error-message>{{ error }}</app-error-message>
    </div>
  </div>
</template>

<script>
import AppFormLabel from "~/components/atoms/forms/label/AppFormLabel";
import AppRequireMark from "~/components/atoms/forms/marks/AppRequireMark";
import AppSelect from "~/components/atoms/forms/selects/AppSelect";
import input from "~/mixins/input";
import AppErrorMessage from "~/components/atoms/forms/error/AppErrorMessage";

export default {
  name: "DeliveryFeeForm",
  components: {AppErrorMessage, AppSelect, AppRequireMark, AppFormLabel},
  mixins: [input],
  data() {
    return {
      deliveryFees: [
        {id: 1, value: 'aaa', label: 'aaaa'}
      ]
    }
  },
  props: {
    error: {
      type: String,
      default: ''
    }
  }
}
</script>

<style scoped lang="scss">
.delivery-fee-form {
  @include form-section-mixin;

  &__heading {
    @include left-right-alignment-mixin;
  }
}
</style>