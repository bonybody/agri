<template>
  <div class="sign-up">
    <site-icon></site-icon>
    <sign-up-form></sign-up-form>
  </div>
</template>

<script>
import SignUpForm from "~/components/organisms/forms/SignUpForm";
import SiteIcon from "~/components/icons/SiteIcon";
export default {
  name: "signup",
  components: {SiteIcon, SignUpForm},
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