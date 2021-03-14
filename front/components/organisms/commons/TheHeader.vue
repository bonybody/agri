<template>
  <header>
    <div class="header__bar"></div>
    <div class="header__content">
      <nuxt-link :to="links.home">
        <h1 class="header__title title">
          <span class="title__icon"><site-icon/></span>
          <span class="title__text">アグリー</span>
        </h1>
      </nuxt-link>
      <div class="header__search-bar">
        <form action="/search" method="get">
        <search-bar @click="search()" v-model="text"></search-bar>
        </form>
      </div>

      <div v-if="getLoggedIn" class="logged-in">
        <nuxt-link to="/mypage" class="logged-in__item">
          <div class="profile__img" :class="{'image': getUserImage, 'noImage': !getUserImage}">
            <img v-if="getUserImage" :src="getUserImage" alt="ユーザー画像">
            <no-user-image-icon v-if="!getUserImage"/>
          </div>
        </nuxt-link>
        <app-button-header type="button" @myClick="logout()">ログアウト</app-button-header>
      </div>

      <div v-if="!getLoggedIn" class="not-logged-in">
        <app-button-header :type="'link'" :to="links.login">ログイン</app-button-header>
        <app-button-header :type="'link'" :to="links.signUp" :primary="true">新規登録</app-button-header>
      </div>
    </div>
  </header>
</template>

<script>

import AppButtonHeader from "~/components/atoms/buttons/AppButtonHeader";
import SearchBar from "@/components/molecules/SearchBar";
import NotificationIcon from "~/components/icons/NotificationIcon";
import NoUserImageIcon from "~/components/icons/NoUserImageIcon";
import SiteIcon from "~/components/icons/SiteIcon";

export default {
  name: "TheHeader",
  components: {SiteIcon, NoUserImageIcon, NotificationIcon, SearchBar, AppButtonHeader},
  data() {
    return {
      links: {
        home: '/',
        login: '/login',
        signUp: '/signup'
      },
      notification: 0,
      text: null
    }
  },
  computed: {
    getLoggedIn() {
      console.log(this.$myAuth.loggedIn())
      return this.$myAuth.loggedIn()
    },
    getUserImage() {
      console.log(this.$myAuth.user())
      return this.$myAuth.user().image
    },
  },
  methods: {
    async logout() {
      await this.$myAuth.logout()
    },
    search() {
      this.$router.push({path: '/search', query: {
        text: this.text
        }})
    }
  }
}
</script>

<style scoped lang="scss">
header {
  position: relative;
  z-index: 1000;
  background-color: $main-background-color;
  box-shadow: 0px 2px 2px 0px rgba(0, 0, 0, 0.3);
}
.header__search-bar {
  width: 500px;
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

.title {
  &__icon {
    display: inline-block;
    height: 1.2em;
    width: 1.2em;
    vertical-align: bottom;
  }
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
  height: 35px;
  width: 35px;
  border-radius: 100%;
  background-color: $shadow-color;
  @include center-flex;

  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 100%;
  }
}

.profile__img svg {
  fill: $main-background-color;
}

.noImage {
  padding: 7px;
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