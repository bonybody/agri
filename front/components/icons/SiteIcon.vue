<template>
  <div class="site-icon">アイコン</div>
</template>

<script>
export default {
name: "SiteIcon"
}
</script>

<style scoped lang="scss">
.site-icon {
  width: 100px;
  height: 100px;
  background-color: $main-background-color;
  @include border-radius-box();
  @include center-flex();
  text-align: center;
}
</style>