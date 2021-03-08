<template>
  <div class="page">
    <div class="page__heading">
      <app-heading>購入履歴</app-heading>
    </div>
    <div class="page__tabs">
      <div class="page__tab page__tab--item">
        <app-tab-button
            @myClick="changeShowState(100)"
            :state="showState === 100"
        >すべて
        </app-tab-button>
      </div>
      <div class="page__tab page__tab--item">
        <app-tab-button
            @myClick="changeShowState(0)"
            :state="showState === 0"
        >発送待ち
        </app-tab-button>
      </div>
      <div class="page__tab page__tab--koe">
        <app-tab-button
            @myClick="changeShowState(1)"
            :state="showState === 1"
        >受取待ち
        </app-tab-button>
      </div>
      <div class="page__tab page__tab--koe">
        <app-tab-button
            @myClick="changeShowState(2)"
            :state="showState === 2"
        >取引済
        </app-tab-button>
      </div>
    </div>
    <div class="page__content">
      <div v-if="showState === 100" class="page__items">
        <buy-item-boxes :items="items" :show="showState"/>
      </div>
      <div v-if="showState === 0" class="page__item">
        <buy-item-boxes :items="items" :show="showState"/>
      </div>
      <div v-if="showState ===1" class="page__item">
        <buy-item-boxes :items="items" :show="showState"/>
      </div>
      <div v-if="showState === 2" class="page__item">
        <buy-item-boxes :items="items" :show="showState"/>
      </div>
    </div>

    <div class="page__items">
    </div>
  </div>
</template>

<script>
import BuyItemBoxes from "~/components/organisms/ItemBoxes/BuyItemBoxes";
import AppHeading from "~/components/atoms/headings/AppHeading";
import AppTabButton from "@/components/atoms/buttons/AppTabButton";

export default {
  name: "buy_history",
  layout: 'mypage',
  components: {AppHeading, BuyItemBoxes, AppTabButton},
  async asyncData({params, $api, $myAuth}) {
    let items = {}
    const res = await $api['item-transaction'].getByBuyerId($myAuth.user().id).then(
        ({data}) => {
          console.log(data)
          items = data.entries
        }
    )
    return {items: items}
  },
  data() {
    return {
      showState: 100
    }
  },
  methods: {
    changeShowState(num) {
      this.showState = num
    }
  }
}
</script>

<style scoped lang="scss">
.page {
  &__heading {
    margin-bottom: $medium-parts-margin;
  }

  &__tabs {
    display: flex;
    justify-content: left;
    margin-bottom: $semi-large-margin;
  }

  &__tab {
    width: 200px;
    height: 40px;
    margin-right: $medium-parts-margin;
  }

}
</style>