<template>
  <div class="site-icon">
    <img src="~/assets/images/icon/site_logo.svg" alt="サイトロゴ">
  </div>
</template>

<script>
export default {
name: "SiteIcon"
}
</script>

<style scoped lang="scss">
.site-icon {
  width: 100%;
  height: 100%;
  @include center-flex();
  text-align: center;
  img {
    width: 100%;
    height: 100%;
  }
}
</style>