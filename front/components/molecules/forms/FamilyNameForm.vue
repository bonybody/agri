<template>
  <div class="family-name-form">
    <app-form-label :name="'family_name'">性</app-form-label>
    <app-input-text
        :type="'text'"
        :name="'family_name'"
        :placeholder="'例：山田'"
        v-model="inputValue"
    />
  </div>
</template>

<script>
import AppInputText from "~/components/atoms/forms/input/AppInputText";
import Input from '~/mixins/input.js'
import AppFormLabel from "~/components/atoms/forms/label/AppFormLabel";

export default {
  name: "FamilyNameForm",
  components: {AppFormLabel, AppInputText},
  mixins: [Input]
}
</script>

<style scoped lang="scss">
.family-name-form {
  @include form-section-mixin;
}
</style>