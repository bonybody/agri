<template>
  <nuxt-link :to="link" class="menu-link">
    <div class="menu-link__text">
      <slot></slot>
    </div>
    <div class="menu-link__arrow" aria-label="link-arrow"></div>
  </nuxt-link>
</template>

<script>
export default {
  name: "AppMenuLink",
  props: {
    link: {
      type: Object,
      default() {
        return {}
      }
    }
  }
}
</script>

<style scoped lang="scss">
.menu-link {
  font-size: $base-font-size;
  display: flex;
  width: 100%;
  height: 100%;
  box-sizing: border-box;
  padding: 0 $min-parts-margin;
  justify-content: space-between;
  align-items: center;
  background-color: $main-background-color;
  color: $main-font-color;

  &__text {
    color: $main-font-color;
  }

  &__arrow {
    display: block;
    width: 5px;
    height: 5px;
    border-top: solid 1px $shadow-color;
    border-right: solid 1px $shadow-color;
    -webkit-transform: rotate(45deg);
    transform: rotate(45deg);
  }

}
</style>