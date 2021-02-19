<template>
  <div class="koe-box">
    <div class="heading">
      <div class="heading__left">
        <p class="user-icon">
          <user-icon
              :id="userId"
              :image="userImage"
          />
        </p>
        <div class="flex-vertical-wrap">
          <p class="user-name">{{ userName }}</p>
          <p class="post-day">{{ postDay }}</p>
        </div>
      </div>
      <div class="heading__right">
      </div>
    </div>
    <div class="header-text-separation">
    </div>
    <div class="body">
      <p class="body__title" v-line-clamp="2">{{ koeTitle }}</p>
      <p class="bony__text">{{ koeText }}</p>
    </div>
    <app-separation/>
    <div class="footer">
      <p class="footer__info" v-line-clamp="2">{{ itemName }}</p>
      <p class="footer__bottom">
        <app-form-button @my-click="itemLink">商品を見に行く</app-form-button>
      </p>
    </div>
  </div>
</template>

<script>
import UserIcon from "~/components/icons/UserIcon";
import AppSeparation from "~/components/atoms/separations/AppSeparation";
import AppFormButton from "~/components/atoms/forms/button/AppFormButton";

export default {
  name: "KoeBox",
  components: {AppFormButton, AppSeparation, UserIcon},
  props: {
    userId: {
      type: Number,
      default: 1,
    },
    userName: {
      type: String,
      default: 'テストユーザー',
    },
    userImage: {
      type: String,
      default: '',
    },
    postDay: {
      type: String | Date,
      default: '2020-01-01'
    },
    koeTitle: {
      type: String,
      default: '本当に美味しい！'
    },
    koeText: {
      type: String,
      default: '本当に美味しい！\n' +
          'こんな美味しい野菜を食べたのは初めてです！'
    },
    itemId: {
      type: Number,
      default: 1,
    },
    itemName: {
      type: String,
      default: '豊橋の美味しいキャベツ！あああああああああああああああああああああああ'
    },
  },
  methods: {
    itemLink: function () {
      this.$router.push({ name: 'item', query: { itemId: this.itemId } })
    }
  }
}
</script>

<style scoped lang="scss">

.koe-box {
  @include min-box-padding-mixin();
  background-color: $main-background-color;
  border-radius: $box-border-radius;
  width: 180px;

  .heading {
    @include left-right-alignment-mixin;

    &__left {
      @include center-flex;

      .user-icon {
        @include min-user-icon-mixin();
        margin-right: $min-parts-margin;
      }
    }

    &__right {
      .koe-title {
      }
    }
  }

  .header-text-separation {
    margin-top: $medium-parts-margin;
    margin-bottom: $medium-parts-margin;
  }

  .body {
    margin-top: $semi-large-margin;
    margin-bottom: $semi-large-margin;

    &__title {
      font-weight: bold;
      font-size: 1em;
      height: 2rem;
      margin-bottom: $medium-parts-margin;
    }

    &__text {
      white-space: pre-wrap;
    }
  }

  .footer {
    margin-top: $large-margin;

    &__info {
      margin-bottom: $min-parts-margin;
      text-align: left;
      font-weight: bold;
      //width: 300px;
      //white-space: nowrap;
      //text-overflow: ellipsis;
      //overflow: hidden;
    }

    &__buttom {

    }
  }
}
</style>