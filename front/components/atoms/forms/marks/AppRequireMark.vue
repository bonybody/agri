<template>
  <div class="require-mark">
    必須
  </div>
</template>

<script>
export default {
name: "AppRequireMark",
}
</script>

<style scoped lang="scss">
.require-mark {
  @include border-radius-box();
  display: inline-block;
  background-color: $accent-color;
  color: $accent-color-on-font-color;
  padding: 2px 3px;
  margin-bottom: 3px;
}
</style>