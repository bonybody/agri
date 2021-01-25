<template>
  <header>
    <div class="header__bar"></div>
    <div class="header__content">
      <nuxt-link :to="links.home"><h1>アグリー</h1></nuxt-link>
      <search-bar></search-bar>

      <div v-if="getLoggedIn" class="logged-in">
        <nuxt-link to="/notifications" class="notifications logged-in__item">
          <p class="notifications__img">
            <notification-icon></notification-icon>
          </p>
          <p class="notifications__number">
            <span v-text="notification"></span>
          </p>
        </nuxt-link>
        <nuxt-link to="/setting/profile" class="logged-in__item">
          <p class="profile__img">
            <img src="" alt="">
          </p>
        </nuxt-link>
      </div>

      <div v-if="!getLoggedIn" class="not-logged-in">
        <app-button-header :to="links.login">ログイン</app-button-header>
        <app-button-header :to="links.signUp" :primary="true">新規登録</app-button-header>
      </div>
    </div>
  </header>
</template>

<script>

import AppButtonHeader from "~/components/atoms/buttons/AppButtonHeader";
import SearchBar from "~/components/molecules/searchBar";
import NotificationIcon from "~/components/icons/NotificationIcon";

export default {
  name: "TheHeader",
  components: {NotificationIcon, SearchBar, AppButtonHeader},
  data() {
    return {
      links: {
        home: '/',
        login: '/login',
        signUp: '/signup'
      },
      notification: 0
    }
  },
  computed: {
    getLoggedIn() {
      console.log(this.$myAuth.loggedIn())
      return this.$myAuth.loggedIn()
    },
  }
}
</script>

<style scoped lang="scss">
header {
  position: relative;
  background-color: $main-background-color;
  box-shadow: 0px 2px 2px 0px rgba(0, 0, 0, 0.3);
}

.header__content {
  max-width: 1024px;
  height: 45px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

h1 {
  font-weight: bold;
  font-size: 30px;
  margin: 0 20px;
}

.header__bar {
  display: block;
  content: "";
  height: 5px;
  background: linear-gradient(90deg, $gradient-color-start, $gradient-color-end);
}

.logged-in {
  display: flex;
  justify-content: space-around;
  align-items: center;
  box-sizing: content-box;
  padding: 0 20px;
}

.profile__img {
  height: 30px;
  width: 30px;
  border-radius: 100%;
  background-color: $primary-color;
}

.not-logged-in {
  display: flex;
  width: 200px;
  justify-content: space-around;
  align-items: center;
}

.notifications {
  height: 30px;
  padding: 3px;
  background-color: $primary-color;
  color: $primary-on-font-color;
  display: flex;
  justify-content: space-around;
  align-items: center;
  border-radius: 4px;
}

.notifications__img {
  padding: 3px;
  height: 100%;
  background-color: $primary-on-font-color;
  border-radius: 4px;
  fill: $primary-color;
}

.notifications__number {
  margin-left: 5px;
}

.logged-in__item {
  margin: 0 10px;
}
</style>