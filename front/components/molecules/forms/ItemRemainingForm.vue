<template>
  <div class="item-remaining-form">
    <div class="item-remaining-form__label">
      <app-form-label :name="'remaining'">数量制限</app-form-label>
      <app-require-mark v-show="require"/>
    </div>
    <div class="item-remaining-form__input">
      <app-input-text
          :type="'number'"
          :name="'remaining'"
          :placeholder="'1'"
          :value="value"
          @input="$emit('input')"
      />
    </div>
    <div class="item-remaining-form__check">
      <div class="checkbox">
        <app-input-radio
            :name="'remainingFormat'"
            v-model="radio"
            :value="radio"
            :options="options"
        />
      </div>
    </div>

  </div>
</template>

<script>
import AppInputText from "~/components/atoms/forms/input/AppInputText";
import AppInputRadio from "~/components/atoms/forms/input/AppInputRadio";

export default {
  name: "ItemRemainingForm",
  components: {AppInputRadio, AppInputText},
  data() {
    return {
      pickFlg: {
        whole: true,
        day: false,
        week: false,
        month: false
      },
    }
  },
  props: {
    value: {
      type: Number,
      default: 1
    },
    picked: {
      type: String,
      default: ''
    },
    options: {
      type: Array,
      require: true
    }
  },
  computed: {
    radio: {
      get() {
        return this.picked
      },
      set(value){
        this.$emit('changeRadio', value)
      }
    }
  }
}
</script>

<style scoped lang="scss">
.item-remaining-form {

  &__label {
    @include left-right-alignment-mixin;
  }

  &__input {
    margin-bottom: $medium-parts-margin;
  }
  &__check {
    margin-bottom: $medium-parts-margin;
  }
}
</style>