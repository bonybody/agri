<template>
  <div class="my-page-menus">
    <p class="my-page-menus__title">
      <app-heading>マイページメニュー</app-heading>
    </p>
    <div class="my-page-menus__content">
      <template v-for="menu in menus">
        <div class="my-page-menu" :key="menu.id">
          <p class="my-page-menu__label">
            <app-menu-label>{{ menu.name }}</app-menu-label>
          </p>
          <div class="my-page-menu__links">
            <template v-for="link in menu.links">
              <div class="my-page-menu__link">
                <app-menu-link :link="link.link">{{ link.text }}</app-menu-link>
              </div>
            </template>
          </div>
        </div>
      </template>
    </div>
  </div>
</template>

<script>
import AppMenuLabel from "~/components/atoms/menu/AppMenuLabel";
import AppMenuLink from "~/components/atoms/menu/AppMenuLink";
import AppSeparation from "~/components/atoms/separations/AppSeparation";
import AppHeading from "~/components/atoms/headings/AppHeading";

export default {
  name: "MyPageMenu",
  components: {AppHeading, AppSeparation, AppMenuLink, AppMenuLabel},
  data() {
    return {
      menus: [
        {
          id: 1,
          name: '一般',
          links: [
            {id: 1, text: 'マイページ', link: {path: '/mypage'}},
            {id: 2, text: 'プロフィール', link: {path: '/user/' + this.$myAuth.user().id}},
            {id: 3, text: 'お気に入り', link: {path: '/mypage/favorite'}},
            {id: 4, text: 'お知らせ', link: {path: '/mypage/notice'}},
            {id: 5, text: 'フォローユーザー', link: {path: '/mypage/follow'}},
          ]
        },
        {
          id: 2,
          name: '購入',
          links: [
            {id: 1, text: '購入履歴', link: {path: '/mypage/buy_history'}},
            {id: 2, text: '購入履歴 - 取引中', link: {path: '/mypage/buy_history', query: {now: true}}},
          ]
        },
        {
          id: 3,
          name: '販売',
          links: [
            {id: 1, text: '商品を出品する', link: {path: '/mypage'}},
            {id: 2, text: '売上管理', link: {path: '/user/' + this.$myAuth.user().id}},
            {id: 3, text: '出品商品', link: {path: '/favorite'}},
            {id: 4, text: '出品商品 - 取引中', link: {path: '/notice'}},
          ]
        },
        {
          id: 4,
          name: 'コエ',
          links: [
            {id: 1, text: '投稿したコエ', link: {path: '/mypage'}},
            {id: 2, text: '届いたコエ', link: {path: '/user/' + this.$myAuth.user().id}},
          ]
        },
        {
          id: 5,
          name: '設定',
          links: [
            {id: 1, text: 'お支払い設定', link: {path: '/mypage'}},
            {id: 2, text: 'お届け先住所', link: {path: '/user/' + this.$myAuth.user().id}},
          ]
        }
      ]
    }
  }
}
</script>

<style scoped lang="scss">

.my-page-menus {
  width: 200px;
  margin: 0 auto;

  &__title {
    margin-bottom: $semi-large-margin;
  }

  &__content {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
}

.my-page-menu {
  margin-bottom: $semi-large-margin;

  &__links {

  }

  &__link {
    width: 200px;
    height: 35px;
    border-bottom: 1px solid $weak-font-color;

    &:last-child {
      border-bottom: none;
    }
  }
}
</style>