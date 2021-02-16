<template>
  <nuxt-link :to="{ path: 'item', query: { itemId: itemId } }" class="item-box">
    <p class="item-box__state">
      残り{{ format }}日
    <p/>
    <div class="item-box__content-wrap">
      <div class="item-box__image-area">
        <p class="item-box__item-image-wrap">
          <img v-if="image" class="item-box__item-image" src="" alt="">
        </p>
        <nuxt-link :to="'nuxt'" class="item-box__user-image-wrap">
          <img v-if="userImage" class="item-box__user-image" src="" alt="">
        </nuxt-link>
      </div>
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
        <div class="line-wrap">
          <p class="item-box__name">{{ name }}</p>
        </div>
        <div class="line-wrap">
          <p class="item-box__price">&yen;{{ price }}~</p>
          <p class="item-box__format">{{ state }}</p>
        </div>
        <div class="tags">
          <p class="tag"></p>
        </div>
      </div>

    </div>
  </nuxt-link>
</template>

<script>
import MapIcon from "~/components/icons/MapIcon";
import HeartIcon from "~/components/icons/HeartIcon";
import FavoriteButton from "~/components/atoms/buttons/FavoriteButton";
import PasswordForm from "~/components/molecules/forms/PasswordForm";

export default {
  name: "ItemBox",
  components: {PasswordForm, FavoriteButton, HeartIcon, MapIcon},
  data() {
    return {
      thisFavorite: false
    }
  },
  props: {
    userId: {
      type: Number,
      default: 0
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
      default: false
    },
    state: {
      type: String,
      default: '今週残り1つ'
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
    format: {
      type: String,
      default: '1'
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
      this.thisFavorite = !this.thisFavorite
    }
  },
  computed: {
    getFavorite() {
      return this.thisFavorite
    }
  }
}
</script>

<style scoped lang="scss">
.item-box {
  width: 180px;
  margin: 10px;
  text-align: right;


  &__state {
    display: inline-block;
    position: relative;
    z-index: 100;
    box-sizing: border-box;
    box-shadow: $box-shadow;
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
    box-shadow: $box-shadow;
    border-radius: 4px 0 4px 4px;
  }

  &__image-area {
    border-radius: 4px 0 0 0;
    width: 180px;
    height: 180px;
    background-color: $shadow-color;
    color: $primary-on-font-color;
    position: relative;
  }

  &__item-image {
    width: 100%;
    height: 100%;
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
    fill: $shadow-color;
    height: 1.3em;
  }

  &__name {
    text-align: left;
    font-weight: bold;
  }

  &__text-wrap {
    padding: 5px;
  }

  &__format {
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