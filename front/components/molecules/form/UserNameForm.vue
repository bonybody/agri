<template>
  <div class="user-name-form">
    <app-form-label :name="'user_name'">ユーザー名</app-form-label>
    <app-input-text
        :type="'text'"
        :placeholder="'１５文字以内で入力してください。'"
        :name="'user_name'"
        v-model="inputValue"
    />
  </div>
</template>

<script>
import AppInputText from "~/components/atoms/forms/input/AppInputText";
import AppFormLabel from "~/components/atoms/forms/label/AppFormLabel";

export default {
  name: "UserNameForm",
  components: {AppFormLabel, AppInputText},
  props: {
    value: {
      type: String,
      default: ''
    }
  },
  computed: {
    inputValue: {
      get() {
        return this.value;
      },
      set(value) {
        this.$emit('input', value);
      }
    }
  }

}
</script>

<style scoped lang="scss">
.user-name-form {
  margin-bottom: $form-parts-margin-bottom;
}
</style>