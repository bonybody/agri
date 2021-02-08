<template>
  <div class="login">
    <site-icon/>
    <login-form></login-form>
  </div>
</template>

<script>
import LoginForm from "~/components/organisms/forms/LoginForm";
import SiteIcon from "~/components/icons/SiteIcon";

export default {
  name: "login",
  components: {SiteIcon, LoginForm},
  data() {
    return {
      password: 'user1',
      email: 'user1'
    }
  },
  methods: {
    async login() {
      await this.$myAuth.login(this.email, this.password)
    },

  },

}
</script>

<style scoped>
.login {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
}

.login > div {
  margin: 30px 0;
}
</style>