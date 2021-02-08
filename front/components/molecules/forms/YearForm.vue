<template>
  <div class="year-form">
    <app-select :name="'year'" v-model="inputValue" >
      <option v-for="n in 50" :value="Number(n + 1980)">
        {{ n + 1980 }}
      </option>
    </app-select>
    <app-form-label :name="'year'">年</app-form-label>
  </div>
</template>

<script>
import AppSelect from "~/components/atoms/forms/selects/AppSelect";
import input from "~/mixins/input";
import AppFormLabel from "~/components/atoms/forms/label/AppFormLabel";
export default {
name: "YearForm",
  components: {AppFormLabel, AppSelect},
  mixins: [ input ],
  props: {

  }
}
</script>

<style scoped lang="scss">
.year-form {
  display: flex;
  align-items: center;
  @include form-section-mixin;

  :first-child {
    margin-right: 8px;
  }
}
</style>