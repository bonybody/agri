<template>
  <div class="day-form">
    <app-select :name="'day'" v-model="inputValue">
      <option v-for="n in getDays" :value="n">
        {{ n }}
      </option>
    </app-select>
    <app-form-label :name="'day'">日</app-form-label>
  </div>
</template>

<script>
import AppSelect from "~/components/atoms/forms/selects/AppSelect";
import input from "~/mixins/input";
import AppFormLabel from "~/components/atoms/forms/label/AppFormLabel";

export default {
  name: "DayForm",
  components: {AppFormLabel, AppSelect},
  mixins: [input],
  props: {
    year: {
      type: Number,
      default: 1981
    },
    month: {
      type: Number,
      default: 1
    }
  },
  computed: {
    getDays() {
      return new Date(this.year, this.month, 0).getDate();
    }
  }
}
</script>

<style scoped lang="scss">
.day-form {
  display: flex;
  align-items: center;
  @include form-section-mixin;
  :first-child {
    margin-right: 8px;
  }
}

</style>