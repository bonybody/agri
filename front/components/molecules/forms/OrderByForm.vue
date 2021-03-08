<template>
  <div class="order-by-form">
    <div class="order-by__header">
      <div class="order-by__label">
        <app-form-label :name="'item_category'">並び順</app-form-label>
      </div>
      <div class="order-by__label__require">
        <app-require-mark v-show="!require"/>
      </div>
    </div>
    <div class="order-by__input">
      <app-select v-model="inputValue" :options="selects" :name="'item_category'"></app-select>
    </div>
    <div class="order-by__error">
      <app-error-message>{{ error }}</app-error-message>
    </div>
  </div>
</template>

<script>
import AppSelect from "~/components/atoms/forms/selects/AppSelect";
import AppFormLabel from "~/components/atoms/forms/label/AppFormLabel";
import AppRequireMark from "~/components/atoms/forms/marks/AppRequireMark";
import input from "~/mixins/input";
import AppErrorMessage from "~/components/atoms/forms/error/AppErrorMessage";

export default {
  name: "OrderByForm",
  components: {AppErrorMessage, AppRequireMark, AppFormLabel, AppSelect},
  mixins: [input],
  data() {
    return {
      selects: [
        {value: 1, label: '新着順'},
        {value: 2, label: '価格が高い順'},
        {value: 3, label: '価格が安い順'}
      ],
    }
  },
  props: {
    error: {
      type: String,
      require: true,
    },
    require: {
      type: Boolean,
      default: false
    }
  }
}
</script>

<style scoped lang="scss">
.order-by {
  @include form-section-mixin

  &__header {
    @include left-right-alignment-mixin
  }
}

</style>