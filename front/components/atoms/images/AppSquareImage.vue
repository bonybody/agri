<template>
  <div class="square-image">
    <img v-if="src" class="square-image__image" :src="src" :alt="alt">
    <div v-else class="square-image__no-image"></div>
  </div>
</template>

<script>
export default {
  name: "AppSquareImage",
  props: {
    src: {
      type: String,
      default: null
    },
    alt: {
      type: String,
      default: null
    }
  }
}
</script>

<style scoped lang="scss">
.square-image {
  width: 100%;
  height: 100%;

  &__image {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  &__no-image {
    content: '';
    width: 100%;
    height: 100%;
    background-color: $shadow-color;
  }
}
</style>