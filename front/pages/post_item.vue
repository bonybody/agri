<template>
  <div class="sign-up">
    <site-icon></site-icon>
    <item-post-form></item-post-form>
  </div>
</template>

<script>
import ItemPostForm from "~/components/organisms/forms/ItemPostForm";
import SiteIcon from "~/components/icons/SiteIcon";
export default {
  name: "postItem",
  components: {SiteIcon, ItemPostForm},
}
</script>

<style scoped lang="scss">
.sign-up {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
}
.sign-up > div {
  margin: 30px 0;
}

</style>