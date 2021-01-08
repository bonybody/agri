<template>
  <app-input-text v-model="text" :placeholder="placeholder"/>
</template>

<script>
import AppInputText from "~/components/atoms/forms/AppInputText";

export default {
  name: "searchForm",
  components: {AppInputText},
  data() {
    return {
      text: '',
      placeholder: '文字を入力してください。'
    }
  }
}
</script>

<style scoped>

</style>