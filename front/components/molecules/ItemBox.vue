<template>
  <div  class="item-box">
    <p class="item-box__state">
      残り{{ period }}日
    <p/>
    <div class="item-box__content-wrap">
      <nuxt-link :to="getItemDetailLink" class="item-box__image-area">
        <p class="item-box__item-image-wrap">
          <img v-if="image" class="item-box__item-image" :src="image" :alt="name">
        </p>
        <div class="item-box__user-image-wrap">
          <user-icon :image="userImage" />
        </div>
      </nuxt-link>
      <div class="item-box__text-wrap">
        <div class="line-wrap">
          <p class="item-box__address">
            <map-icon></map-icon>
            {{ address }}
          </p>
          <div class="item-box__favorite-button">
            <favorite-button :state="getFavorite" @myClick="favoriteClick()"></favorite-button>
          </div>
        </div>
        <div class="line-wrap" >
          <nuxt-link :to="getItemDetailLink" class="item-box__name" ><span v-line-clamp="2">{{ name }}</span></nuxt-link>
        </div>
        <div class="line-wrap">
          <p class="item-box__price">&yen;{{ price }}~</p>
          <p class="item-box__format">{{ getRemaining }}</p>
        </div>
        <div class="tags">
          <p class="tag"></p>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import MapIcon from "~/components/icons/MapIcon";
import HeartIcon from "~/components/icons/HeartIcon";
import FavoriteButton from "~/components/atoms/buttons/FavoriteButton";
import PasswordForm from "~/components/molecules/forms/PasswordForm";
import UserIcon from "~/components/icons/UserIcon";

export default {
  name: "ItemBox",
  components: {UserIcon, PasswordForm, FavoriteButton, HeartIcon, MapIcon},
  data() {
    return {
      thisFavorite: false
    }
  },
  props: {
    userId: {
      type: Number,
      default: 1
    },
    userImage: {
      type: String,
      default: ""
    },
    itemId: {
      type: Number,
      default: 1
    },
    favorite: {
      type: Boolean,
      default: true
    },
    remaining: {
      type: Number,
      default: 4
    },
    remaining_format: {
      type: String,
      require: true
    },
    image: {
      type: String,
      default: null
    },
    address: {
      type: String,
      default: '豊橋市'
    },
    name: {
      type: String,
      default: '豊橋産の美味しいキャベツを1kgから！'
    },
    price: {
      type: Number,
      default: 2000
    },
    period: {
      type: Number,
      default: 1
    },
    tags: {
      type: Object,
      default: () => {
        return {}
      }
    }
  },
  methods: {
    favoriteClick() {
      console.log('クリック')
      this.favorite = !this.favorite
    }
  },
  computed: {
    getFavorite() {
      return this.favorite
    },
    getItemDetailLink() {
      return {
        path: '/item/' + this.itemId
      }
    },
    getUserProfileLink() {
      return {
        path: '/user/' + this.userId
      }
    },
    getRemaining() {
      let remaining_text = ''
      switch (this.remaining_format){
        case 'whole':
          remaining_text = '全期間残り：' + this.remaining + '個'
          break
        case 'day':
          remaining_text = '本日残り：' + this.remaining + '個'
          break
        case 'week':
          remaining_text = '今週残り：' + this.remaining + '個'
          break
        case 'month':
          remaining_text = '今月残り：' + this.remaining + '個'
          break
      }
      return remaining_text
    }
  }
}
</script>

<style scoped lang="scss">
.item-box {
  display: block;
  width: 180px;
  text-align: right;


  &__state {
    display: inline-block;
    position: relative;
    z-index: 100;
    box-sizing: border-box;
    //box-shadow: $box-shadow;
    padding: 5px 10px;
    color: $primary-on-font-color;
    border-radius: 4px 4px 0 0;
    background-color: $primary-color;
  }

  &__content-wrap {
    position: relative;
    z-index: 101;
    text-align: center;
    background-color: $main-background-color;
    //box-shadow: $box-shadow;
    border-radius: 4px 0 4px 4px;
  }

  &__image-area {
    display: block;
    border-radius: 4px 0 0 0;
    width: 180px;
    height: 180px;
    background-color: $shadow-color;
    color: $primary-on-font-color;
    position: relative;

    &:hover {
      opacity: $hover-opacity;
    }
  }

  &__item-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 4px 0 0 0;

  }

  &__item-image-wrap {
    border-radius: 4px 0 0 0;
    background-color: $shadow-color;
    color: $primary-on-font-color;
    width: 180px;
    height: 180px;

  }

  &__user-image {
    width: 100%;
    height: 100%;
  }

  &__user-image-wrap {
    position: absolute;
    bottom: 10px;
    right: 10px;
    border-radius: 1000px;
    width: 30px;
    height: 30px;
    background-color: $primary-color;
  }

  &__address {
    color: $weak-font-color;

    svg {
      height: 1.1em;
      fill: $weak-font-color;
      vertical-align: bottom;
    }
  }

  &__favorite-button {
    position: relative;
    z-index: 999;
    fill: $shadow-color;
    height: 1.3em;
  }

  &__name {
    display: block;
    text-align: left;
    font-weight: bold;
    height: 2rem;

    &:hover {
      opacity: $hover-opacity;
    }
  }

  &__text-wrap {
    padding: 5px;
  }

  &__format {
    font-size: 0.8em;
    font-weight: bold;
    padding: 3px 10px;
    border-radius: 1000px;
    background-color: $accent-color;
    color: $accent-color-on-font-color;
  }

  &__price {
    color: $primary-color;
    font-size: 1.2em;
  }
}

.line-wrap {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 5px 0;
}
</style>