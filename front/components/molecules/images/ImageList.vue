<template>
  <div class="image-list">
    <div v-if="images.length === 0" class="image-list__no-image">画像なし</div>
    <template v-for="(image,index) in images">
      <p v-if="index === 0"
         class="image-list__image-wrap image-list__image-wrap--first">
        <app-square-image :src="image.url" :alt="meaning + image.id"/>
      </p>
      <p v-if="index !== 0" class="image-list__image-wrap">
        <app-square-image :src="image.url" :alt="meaning + image.id"/>
      </p>
    </template>
  </div>
</template>

<script>
import AppSquareImage from "~/components/atoms/images/AppSquareImage";

export default {
  name: "ImageList",
  components: {AppSquareImage},
  props: {
    images: {
      type: Array,
      default: () => {
        return [
          require('~/assets/images/test_images/item/1.jpg')
        ]
      }
    },
    meaning: {
      type: String,
      default: null
    },
  },
}
</script>

<style scoped lang="scss">
.image-list {
  width: 500px;
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;

  &__no-image {
    width: 500px;
    height: 500px;
    margin-bottom: 20px;
    background-color: $weak-font-color;
    text-align: center;
    line-height: 400px;
    font-size: large;
  }

  &__image-wrap {
    width: 80px;
    height: 80px;

    &--first {
      width: 500px;
      height: 500px;
      margin-bottom: 20px;

    }

  }
}
</style>