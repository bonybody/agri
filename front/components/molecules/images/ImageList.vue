<template>
  <div class="image-list">
    <template v-for="image in getImages">
      <p v-if="image.id === images.length"
         class="image-list__image-wrap image-list__image-wrap--first">
        <app-square-image :src="image.image" :alt="meaning + image.id"/>
      </p>
      <p v-if="image.id !== images.length" class="image-list__image-wrap">
        <app-square-image :src="image.image" :alt="meaning + image.id"/>
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
  computed: {
    getImages() {
      const resultImages = []
      this.images.forEach((value, index) => {
        resultImages.push({image: value, id: index + this.images.length})
      });
      return resultImages;
    }

  },
}
</script>

<style scoped lang="scss">
.image-list {
  width: 400px;
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;

  &__image-wrap {
    width: 80px;
    height: 80px;

    &--first {
      width: 400px;
      height: 400px;
      margin-bottom: 20px;

    }

  }
}
</style>