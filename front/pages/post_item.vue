<template>
  <div class="sign-up">
    <div class="sign-up__heading">
      <app-heading>商品出品</app-heading>
    </div>
    <item-post-form></item-post-form>
  </div>
</template>

<script>
import ItemPostForm from "~/components/organisms/forms/ItemPostForm";
import SiteIcon from "~/components/icons/SiteIcon";
import AppHeading from "@/components/atoms/headings/AppHeading";

export default {
  name: "postItem",
  components: {AppHeading, SiteIcon, ItemPostForm},
  layout: 'mypage'
}
</script>

<style scoped lang="scss">
.sign-up {
  max-width: 350px;
  margin: 0 auto;
  &__heading {
    margin-bottom: $large-margin;
    text-align: left;
  }
}

</style>