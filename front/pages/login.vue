<template>
  <div>
    <login-form></login-form>
    <input type="text" v-model="email">
    <input type="password" v-model="password">
    <button @click="login">ログイン</button>
  </div>
</template>

<script>
import LoginForm from "~/components/organisms/form/login/LoginForm";
export default {
  name: "login",
  components: {LoginForm},
  data() {
    return {
      password: 'user1',
      email: 'user1'
    }
  },
  methods: {
    async login() {
      await this.$myAuth.login(this.email, this.password)
    }
  }
}
</script>

<style scoped>

</style>