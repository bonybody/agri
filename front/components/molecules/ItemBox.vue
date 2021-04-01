<template>
  <div class="item-box">
    <div>
      <login-require-window
          :show-modal="notLoggedInModal"
          @close-modal="closeModal"
      />
    </div>
    <p class="item-box__period">
      {{ getPeriod }}
    <p/>
    <div class="item-box__content-wrap">
      <div class="item-box__image-area">
        <nuxt-link :aria-label="name" :to="getItemDetailLink" class="item-box__item-image-wrap">
          <img rel="prefetch" v-if="image" class="item-box__item-image" :src="image" :alt="name">
        </nuxt-link>
        <div class="item-box__user-image-wrap">
          <user-icon :image="userImage"/>
        </div>
      </div>
      <div class="item-box__text-wrap">
        <div class="line-wrap">
          <div class="item-box__address">
            <map-icon></map-icon>
            {{ address }}
          </div>
          <div class="item-box__favorite-button">
            <favorite-button :state="getFavorite" @myClick="changeFavorite"></favorite-button>
          </div>
        </div>
        <div class="line-wrap">
          <nuxt-link :to="getItemDetailLink" class="item-box__name"><span v-line-clamp="2">{{ name }}</span></nuxt-link>
        </div>
        <div class="line-wrap">
          <p class="item-box__price">&yen;{{ price }}~</p>
          <p class="item-box__format">{{ getRemaining }}</p>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import MapIcon from "~/components/icons/MapIcon";
import FavoriteButton from "~/components/atoms/buttons/FavoriteButton";
import UserIcon from "~/components/icons/UserIcon";
import LoginRequireWindow from "@/components/organisms/modal_windows/LoginRequireWindow";

export default {
  name: "ItemBox",
  components: {LoginRequireWindow, UserIcon, FavoriteButton, MapIcon},
  data() {
    return {
      thisFavorite: {
        state: false,
        value: false
      },
      notLoggedInModal: false
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
      default: false
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
    },
    setCount: {
      type: Number,
      require: true
    }
  },
  methods: {
    changeFavorite() {
      if (!this.$myAuth.loggedIn()) {
        this.notLoggedInModal = true
        return
      }
      if (this.thisFavorite.state === false) {
        this.thisFavorite.value = !this.favorite
        this.thisFavorite.state = true
      } else {
        this.thisFavorite.value = !this.thisFavorite.value
      }
      this.$api['favorite'].changeFavorite(this.$myAuth.user().id, this.itemId)
    },
    closeModal() {
      this.notLoggedInModal = !this.notLoggedInModal
    }
  },
  computed: {
    getPeriod: function () {
      const result = {}
      if (this.period === 0) {
        result.period = '据え置き';
      } else {
        result.period = '残り' + this.period + '日';
      }
      return result.period
    },
    getFavorite() {
      if (!this.thisFavorite.state) {
        return this.favorite
      }
      if (this.thisFavorite.state) {
        return this.thisFavorite.value
      }
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
      switch (this.remaining_format) {
        case 'whole':
          remaining_text = '全期間残り：' + String(this.remaining - this.setCount) + '個'
          break
        case 'day':
          remaining_text = '本日残り：' + (this.remaining - this.setCount) + '個'
          break
        case 'week':
          remaining_text = '今週残り：' + (this.remaining - this.setCount) + '個'
          break
        case 'month':
          remaining_text = '今月残り：' + (this.remaining - this.setCount) + '個'
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


  &__period {
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

  }

  &__item-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 4px 0 0 0;

  }

  &__item-image-wrap {
    display: block;
    border-radius: 4px 0 0 0;
    background-color: $shadow-color;
    color: $primary-on-font-color;
    width: 180px;
    height: 180px;

    &:hover {
      opacity: $hover-opacity;
    }

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

    &:hover {
      opacity: $hover-opacity;
    }
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