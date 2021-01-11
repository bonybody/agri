<template>

  <header>
    <div class="bar"></div>
    <div class="content">
      <nuxt-link :to="links.home"><h1>アグリー</h1></nuxt-link>
      <search-bar></search-bar>
      <app-button-header :to="links.signUp">新規登録</app-button-header>
      <app-button-header :to="links.login">ログイン</app-button-header>
    </div>
  </header>
</template>

<script>
import AppButtonHeader from "~/components/atoms/buttons/AppButtonHeader";
import SearchBar from "~/components/molecules/searchBar";

export default {
  name: "TheHeader",
  components: {SearchBar, AppButtonHeader},
  data() {
    return {
      links: {
        home: '/',
        login: '/login',
        signUp: '/signup'
      }
    }
  },
}
</script>

<style scoped lang="scss">
header {
  position: relative;
  background-color: $main-background-color;
  box-shadow: 0px 2px 2px 0px rgba(0, 0, 0, 0.3);
}

.content {
  width: 1024px;
  height: 45px;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  align-items: center;
}

h1 {
  font-weight: bold;
  font-size: 30px;
}

.bar {
  display: block;
  content: "";
  height: 5px;
  background: linear-gradient(90deg, $gradient-color-start, $gradient-color-end);
}
</style>