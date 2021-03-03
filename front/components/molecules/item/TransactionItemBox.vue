<template>
  <div class="buy-item-box">
    <div class="buy-item-box__image">
      <app-square-image :src="image" :alt="name"/>
    </div>
    <div class="buy-item-box__detail detail">
      <div class="detail__heading">
        <p class="detail__area">
          <map-icon/>
          {{ area }}
        </p>
        <p class="detail__state">{{ getStateText }}</p>
      </div>
      <p class="detail__name">{{ name }}</p>
      <div class="detail__buy-content">
        <span class="detail__price">{{ price * set_count }}</span>
        <span class="detail__volume">{{ volume }} × {{ set_count }}</span>
      </div>
    </div>
    <div class="buy-item-box__buttons buttons">
      <!--      <div class="buttons__button">-->
      <!--        <app-link-button>aaa</app-link-button>-->
      <!--      </div>-->
      <div class="buttons__button">
        <app-link-button :link="{ path: '/item/' + itemId }">商品画面へ</app-link-button>
      </div>
      <div class="buttons__button">
        <app-link-button :link="{ path: '/transaction/' + id }">取引画面へ</app-link-button>
      </div>
      <div class="buttons__button">
        <app-link-button :link="{ path: '/post_koe/' + id }">コエを投稿する</app-link-button>
      </div>
    </div>
  </div>
</template>

<script>
import MapIcon from "~/components/icons/MapIcon";
import AppSquareImage from "~/components/atoms/images/AppSquareImage";
import AppButton from "~/components/atoms/buttons/AppButton";
import AppLinkButton from "~/components/atoms/buttons/AppLinkButton";

export default {
  name: "TransactionItemBox",
  components: {AppLinkButton, AppButton, AppSquareImage, MapIcon},
  props: {
    id: {
      type: Number,
      default: 1
    },
    itemId: {
      type: Number,
      default: 1
    },
    name: {
      type: String,
      default: 'aaa'
    },
    image: {
      type: String,
      default: null
    },
    area: {
      type: String,
      default: '愛知県名古屋市'
    },
    state: {
      type: Number,
      default: '受け取り確認をして下さい'
    },
    volume: {
      type: String,
      default: '10kg'
    },
    set_count: {
      type: Number,
      default: '1'
    },
    price: {
      type: Number,
      default: 300
    }
  },
  computed: {
    getStateText() {
      switch (this.state) {
        case 0:
          return '発送確認待ち'
        case 1:
          return '受け取り確認待ち'
        case 2:
          return '取引完了'
      }
    }
  }
}
</script>

<style scoped lang="scss">
.buy-item-box {
  width: 700px;
  height: 100px;
  background-color: $main-background-color;
  box-sizing: border-box;
  border-radius: $box-border-radius;
  margin-bottom: $medium-parts-margin;

  display: flex;
  justify-content: space-between;
  padding: 10px;


  &__image {
    width: 80px;
    height: 80px;
    margin-right: $medium-parts-margin;
  }

  &__detail {
    margin-right: $medium-parts-margin;
    flex-grow: 10;
  }

  &__buttons {
  }
}

.detail {
  position: relative;

  &__heading {
    display: flex;
    justify-content: space-between;
    margin-bottom: $min-parts-margin;
  }

  &__state {
    color: $accent-color;
  }

  &__name {
    font-size: $large-font-size;
    font-weight: bold;
  }

  &__buy-content {
    position: absolute;
    bottom: 3px;
    //display: flex;
    //justify-content: left;
  }

  &__price {
    font-size: 1.5em;
    font-weight: bold;
  }

  &__volume {
    //vertical-align: bottom;
  }

  &__area {
    color: $weak-font-color;

    svg {
      height: 1.1em;
      fill: $weak-font-color;
      vertical-align: bottom;
    }

  }
}

.buttons {
  display: flex;
  flex-direction: column;
  justify-content: space-between;

  &__button {
    width: 100px;
    height: 22px;
    font-size: 0.8em;
  }
}
</style>