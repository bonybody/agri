<template>
  <div class="given-name-form">
    <app-form-label :name="'given_name'">名</app-form-label>
    <app-input-text
        :name="'given_name'"
        :type="'text'"
        :placeholder="'例：太郎'"
    />
  </div>
</template>

<script>
import AppFormLabel from "~/components/atoms/forms/label/AppFormLabel";
import AppInputText from "~/components/atoms/forms/input/AppInputText";
import input from "~/mixins/input";
export default {
name: "GivenNameForm",
  components: {AppInputText, AppFormLabel},
  mixins: [ input ]
}
</script>

<style scoped lang="scss">
.given-name-form {
  @include form-section-mixin
}
</style>