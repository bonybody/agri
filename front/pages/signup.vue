<template>
  <div class="sign-up">
    <div class="site-icon">
      <site-icon></site-icon>
    </div>
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

.site-icon {
  width: 100px;
  height: 100px;
}
</style>