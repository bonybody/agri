<template>
  <div class="given-name-ruby-form">
    <app-form-label :name="'given_name_ruby'">名カナ</app-form-label>
    <app-input-text
        :name="'given_name_ruby'"
        :type="'text'"
        :placeholder="'例：タロウ'"
    />
  </div>
</template>

<script>
import AppFormLabel from "~/components/atoms/forms/label/AppFormLabel";
import AppInputText from "~/components/atoms/forms/input/AppInputText";
import input from "~/mixins/input";

export default {
  name: "GivenNameRubyForm",
  components: {AppInputText, AppFormLabel},
  mixins: [ input ]
}
</script>

<style scoped lang="scss">
.given-name-ruby-form {
  @include form-section-mixin;
}
</style>