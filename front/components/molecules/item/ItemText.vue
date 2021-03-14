<template>
  <div class="item-text">
    <div class="line-wrap line-wrap__between">
      <p class="remaining-and-period">{{ getRemainingAndPeriod }}</p>
      <div class="address">
        <map-icon/>
        {{ address }}
      </div>
    </div>
    <div class="line-wrap">
      <p class="name">{{ itemName }}</p>
    </div>
    <div class="line-wrap line-wrap__between">
      <div class="user-preview">
        <div class="user-preview__image">
          <user-icon :id="userId" :image="userImage"/>
        </div>
        <p class="user-preview__name">{{ userName }}</p>
      </div>
      <div class="tag-and-category">
        <div class="category">
          カテゴリ：
          <nuxt-link class="category__link" :to="{path: '/search', query: { category: category.id }}">{{
              category.name
            }}
          </nuxt-link>
        </div>
      </div>
    </div>
    <div class="line-wrap">
      <p class="line-wrap__heading">1セットあたり</p>
      <div class="value">
        <p class="value__quantity">内容量：{{ volume }}</p>
        <p class="value__price">&yen;{{ String(price) }}円 + 送料（{{ shippingFee > 0 ? shippingFee : '無料' }}）</p>
      </div>
      <div class="cart">
        <div class="set-count">
          <div class="set-count__input">
            <app-input-text
                type="number"
                name="set_count"
                v-model="inputSetCount"
                :max="(remainingSets - remainingSetCount)"
                :min="1"
            />
          </div>
          <label class="set-count__label" for="set_count">セット購入</label>
        </div>
      </div>

    </div>

    <div class="line-wrap">
      <p class="line-wrap__heading">商品説明</p>
      <p class="description">{{ description }}</p>
    </div>
    <div class="line-wrap">
      <p class="delivery-deadline">ご購入から発送まで約{{ shipment }}日程度</p>
    </div>
    <div class="line-wrap">
      <div class="sns-share">
        <div class="sns-share__icon">
          <app-twitter-share-button
              :url="getHostThisUrl"
              :title="itemName"
          />
        </div>
      </div>
    </div>
    <div class="line-wrap">
      <app-form-button :disabled="disableBuyButton" @my-click="$emit('buy')">購入する
      </app-form-button>
      <!--      <app-form-button v-if="getCurrentUser === userId" @my-click="$emit('edit')">内容を編集する-->
<!--      </app-form-button>-->
    </div>
  </div>
</template>

<script>
import AppItemFormatLabel from "~/components/atoms/labels/AppItemFormatLabel";
import MapIcon from "~/components/icons/MapIcon";
import UserIcon from "~/components/icons/UserIcon";
import AppFormButton from "~/components/atoms/forms/button/AppFormButton";
import AppInputText from "~/components/atoms/forms/input/AppInputText";
import AppTwitterShareButton from "~/components/atoms/buttons/AppTwitterShareButton";

export default {
  name: "ItemText",
  components: {AppTwitterShareButton, AppInputText, AppFormButton, UserIcon, MapIcon, AppItemFormatLabel},
  props: {
    period: {
      type: Number,
      default: 3
    },
    remainingSets: {
      type: Number,
      require: true
    },
    remaining_format: {
      type: String,
      default: '週'
    },
    remainingSetCount: {
      type: Number,
      require: true
    },
    address: {
      type: String,
      default: '愛知県碧南市'
    },
    itemName: {
      type: String,
      default: '【家庭用】フルーツにんじん10kg～'
    },
    itemId: {
      type: Number,
      default: 1
    },
    category: {
      type: Object,
      require: true
    },
    tags: {
      type: Array,
      default: () => {
        return [
          {id: 1, name: 'にんじん'},
        ]
      }
    },
    volume: {
      type: String,
      default: '10kg'
    },
    price: {
      type: Number | String,
      default: '2160'
    },
    shippingFee: { // 送料
      type: Number,
      default: 200
    },
    setCount: {
      type: Number | String,
      default: 1
    },
    description: {
      type: String,
      default: '美味しいです。'
    },
    userId: {
      type: Number,
      default: 1
    },
    userName: {
      type: String,
      default: 'テストユーザー',
    },
    userImage: {
      type: String,
      default: ''
    },
    shipment: {
      type: Number,
      default: 2
    }
  },
  computed: {
    getRemainingAndPeriod: function () {
      const result = {}
      if (this.period == 0) {
        result.period = '据え置き';
      } else {
        result.period = '残り' + this.period + '日';
      }
      const remainingSets = this.remainingSets - this.remainingSetCount
      switch (this.remaining_format) {
        case 'whole':
          result.remaining = '全期間残り：' + remainingSets
          break
        case 'day':
          result.remaining = '本日残り：' + remainingSets
          break
        case 'week':
          result.remaining = '今週残り：' + remainingSets
          break
        case 'month':
          result.remaining = '今月残り：' + remainingSets
      }
      return result.period + '：' + result.remaining
    },
    disableBuyButton() {
      if (this.remainingSets - this.remainingSetCount === 0) {
        return true
      }
      if (this.getCurrentUser === this.userId) {
        return true
      }
      return false
    },
    inputSetCount: {
      get() {
        return this.setCount;
      },
      set(value) {
        this.$emit('update:setCount', Number(value));
      }
    },
    getHostThisUrl() {
      return process.env.HostFrontUrl + this.$router.history.base + this.$route.path
    },
    getCurrentUser() {
      if (this.$myAuth.loggedIn()) {
        return this.$myAuth.user().id
      }
      return false
    }
  }
}
</script>

<style scoped lang="scss">
.item-text {
  @include default-padding-mixin();
  background-color: $main-background-color;
  width: 400px;

  .line-wrap {
    margin-bottom: 30px;

    &__between {
      @include left-right-alignment-mixin;
    }

    &__heading {
      margin-bottom: 5px;
      font-weight: bold;
    }

    .name {
      font-weight: bold;
      font-size: 1.3em;
    }

    .user-preview {
      display: flex;
      justify-content: center;
      align-items: center;
      max-width: 50%;

      &__image {
        width: 30px;
        height: 30px;
        margin-right: 5px;
      }

      &__name {

      }
    }

    .category {
      margin-bottom: 5px;

      &__link {
        @include link-style-mixin();
      }
    }

    .tags {
      &__link {
        @include link-style-mixin();
        margin: 3px;
      }
    }
  }

  .value {
    border-radius: 10px;
    border: 1px solid $shadow-color;
    @include min-box-padding-mixin();

    &__quantity {
      margin-bottom: 5px;
    }

    &__price {
      font-size: $large-font-size;
      font-weight: bold;
    }
  }

  .cart {
    margin-top: 10px;

    .set-count {
      display: flex;
      justify-content: flex-end;
      align-items: center;

      &__input {
        flex-basis: 15%;
        margin-right: 5px;
      }
    }
  }

  .delivery-deadline {
    text-align: center;
    font-size: $large-font-size;
  }
}

.remaining-and-period {
  display: inline-block;
  background-color: $main-background-color;
  border-radius: 100px;
  border: 1px solid $shadow-color;
  padding: 10px;
}

.address {
  svg {
    height: 1.1em;
    fill: $weak-font-color;
    vertical-align: bottom;
  }
}

.sns-share {
  display: flex;
  justify-content: flex-end;

  &__icon {
    width: 30px;
    height: 30px;
  }
}
</style>