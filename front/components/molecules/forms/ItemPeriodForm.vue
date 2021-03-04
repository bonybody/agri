<template>
  <div class="item-period-form">
    <div class="item-period-form__label">
      <app-form-label :name="'period'">販売期間（日単位）</app-form-label>
      <app-require-mark v-show="require"/>
    </div>
    <div class="item-period-form__input-number">
      <app-input-text
          :type="'number'"
          :name="'period'"
          :placeholder="'据え置き'"
          :value="getInputNumber"
          :disabled="value === 0"
          @input="$emit('input', value)"
      />
    </div>
    <div class="item-period-form__check-deferred">
      据え置き販売
      <div class="checkbox">
        <app-input-checkbox
            :value="getToggleValue"
            @input="$emit('clickCheckbox', value)"
        />
      </div>
    </div>
    <div class="item-period-form__error">
      <app-error-message>{{ error }}</app-error-message>
    </div>
  </div>
</template>

<script>
import AppFormLabel from "~/components/atoms/forms/label/AppFormLabel";
import AppRequireMark from "~/components/atoms/forms/marks/AppRequireMark";
import AppInputText from "~/components/atoms/forms/input/AppInputText";
import AppInputCheckbox from "~/components/atoms/forms/input/AppInputCheckbox";
import AppErrorMessage from "~/components/atoms/forms/error/AppErrorMessage";

export default {
  name: "ItemPeriodForm",
  components: {AppErrorMessage, AppInputCheckbox, AppInputText, AppRequireMark, AppFormLabel},
  props: {
    value: {
      type: Number,
      default: ''
    },

    require: {
      type: Boolean,
      default: false
    },
    error: {
      type: String,
      default: ''
    }
  },
  computed: {
    getInputNumber() {
      if (this.value == 0) {
        return null
      }
      return this.value
    },
    getToggleValue() {
      if (this.value === 0) {
        return true
      }
      return false
    }
  }
}
</script>

<style scoped lang="scss">
.checkbox {
  display: inline-block;
  width: 20px;
  height: 20px;
}


.item-period-form {
  @include form-section-mixin;

  &__label {
    @include left-right-alignment-mixin;
  }

  &__input-number {
    margin-bottom: $medium-parts-margin;
  }

  &__check-deferred {

  }
}


</style>