<template>
  <div class="post-koe">
    <div class="post-koe__heading">
      <app-heading>投稿したコエ</app-heading>
    </div>
    <div class="post-koe__items">
      <user-catch-koe-boxes/>
    </div>
  </div>
</template>

<script>
import BuyItemBoxes from "~/components/organisms/ItemBoxes/BuyItemBoxes";
import AppHeading from "~/components/atoms/headings/AppHeading";
import PostKoeBoxes from "~/components/organisms/koeBoxes/PostKoeBoxes";
import UserCatchKoeBoxes from "~/components/organisms/koeBoxes/UserCatchKoeBoxes";

export default {
  name: "catch_koe",
  layout: 'mypage',
  components: {UserCatchKoeBoxes, AppHeading},

}
</script>

<style scoped lang="scss">
.post-koe {
  &__heading {
    margin-bottom: $medium-parts-margin;
  }
}
</style>