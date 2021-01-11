<template>
  <div>
    <input type="text" v-model="email">
    <input type="password" v-model="password">
    <button @click="login">ログイン</button>
  </div>
</template>

<script>
export default {
  name: "login",
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