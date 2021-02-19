<template>
  <div class="sign-up">
    <site-icon></site-icon>
    <product-up-form></product-up-form>
  </div>
</template>

<script>
import ProductUpForm from "~/components/organisms/forms/ProductUpForm";
import SiteIcon from "~/components/icons/SiteIcon";
export default {
  name: "signup",
  components: {SiteIcon, ProductUpForm},
  auth: "guest"
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