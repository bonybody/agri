<template>
  <div class="item-categories-form">
    <div class="item-categories-form__header">
      <div class="item-categories-form__label">
        <app-form-label :name="'item_category'">カテゴリ</app-form-label>
      </div>
      <div class="item-categories-form__label__require">
        <app-require-mark v-show="require"/>
      </div>
    </div>
    <div class="item-categories-form__input">
      <app-select v-model="inputValue" :options="categories" :name="'item_category'"></app-select>
    </div>
    <div class="item-categories-form__error">
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
  name: "ItemCategoryForm",
  components: {AppErrorMessage, AppRequireMark, AppFormLabel, AppSelect},
  mixins: [input],
  data() {
    return {
      categories: [
        {id: 1, value: 'aaa', label: 'aaaa'}
      ],
      require: {
        type: Boolean,
        default: false
      },
    }
  },
  props: {
    error: {
      type: String,
      require: true,
    }

  }
}
</script>

<style scoped lang="scss">
.item-categories-form {
  @include form-section-mixin

  &__header {
    @include left-right-alignment-mixin
  }
}

</style>