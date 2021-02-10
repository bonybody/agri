<template>
  <div class="family-name-ruby-form">
    <app-form-label>性カナ</app-form-label>
    <app-input-text
        :type="'text'"
        :name="'family_name_ruby'"
        :placeholder="'例：ヤマダ'"
        v-model="inputValue"
    />
  </div>
</template>

<script>
import AppInputText from "~/components/atoms/forms/input/AppInputText";
import AppFormLabel from "~/components/atoms/forms/label/AppFormLabel";
import input from "~/mixins/input";

export default {
  name: "FamilyNameRubyForm",
  components: {AppFormLabel, AppInputText},
  mixins: [input]
}
</script>

<style scoped lang="scss">
.family-name-ruby-form {
  @include form-section-mixin;
}

</style>