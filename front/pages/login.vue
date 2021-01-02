<template>
  <div>
    <input type="text" v-model="email">
    <input type="password" v-model="password">
    <button @click="loginWithAuthModule">ログイン</button>
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
    async loginWithAuthModule() {
      await this.$auth.loginWith('local', {
        data: {
          username: this.email,
          password: this.password
        }
      })
          .then((response) => {
                console.log("成功");
                console.log(response);
                console.log(this.$auth.loggedIn);
                return response
              },
              (error) => {
                return error
              })
    }
  }
}
</script>

<style scoped>

</style>