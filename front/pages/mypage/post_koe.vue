<template>
  <div class="post-koe">
    <div class="post-koe__heading">
      <app-heading>投稿したコエ</app-heading>
    </div>
    <div class="post-koe__items">
      <post-koe-boxes/>
    </div>
  </div>
</template>

<script>
import BuyItemBoxes from "~/components/organisms/ItemBoxes/BuyItemBoxes";
import AppHeading from "~/components/atoms/headings/AppHeading";
import PostKoeBoxes from "~/components/organisms/koeBoxes/PostKoeBoxes";

export default {
  name: "post_koe",
  layout: 'mypage',
  components: {PostKoeBoxes, AppHeading, BuyItemBoxes},

}
</script>

<style scoped lang="scss">
.post-koe {
  &__heading {
    margin-bottom: $medium-parts-margin;
  }
}
</style>