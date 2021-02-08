<template>
  <div class="month-form">
    <app-select :name="'month'" v-model="inputValue">
      <option v-for="n in 12" :value="n">
        {{ n }}
      </option>
    </app-select>
    <app-form-label :name="'month'">月</app-form-label>
  </div>
</template>

<script>
import AppSelect from "~/components/atoms/forms/selects/AppSelect";
import input from "~/mixins/input";
import AppFormLabel from "~/components/atoms/forms/label/AppFormLabel";

export default {
  name: "MonthForm",
  components: {AppFormLabel, AppSelect},
  mixins: [input]
}
</script>

<style scoped lang="scss">
.month-form {
  display: flex;
  align-items: center;
  @include form-section-mixin;

  :first-child {
    margin-right: 8px;
  }
}

</style>