<template>
  <div class="page">
    <div class="page__heading">
      <app-heading>注文ボックス</app-heading>
    </div>
    <div class="page__tabs">
<!--      <div class="page__tab page__tab&#45;&#45;item">-->
<!--        <app-tab-button-->
<!--            @myClick="tabChange('all')"-->
<!--            :state="tabs.all.state"-->
<!--        >すべて-->
<!--        </app-tab-button>-->
<!--      </div>-->
      <div class="page__tab page__tab--item">
        <app-tab-button
            @myClick="tabChange('shipment')"
            :state="tabs.shipment.state"
        >発送待ち
        </app-tab-button>
      </div>
      <div class="page__tab page__tab--koe">
        <app-tab-button
            @myClick="tabChange('receipt')"
            :state="tabs.receipt.state"
        >受取待ち
        </app-tab-button>
      </div>
      <div class="page__tab page__tab--koe">
        <app-tab-button
            @myClick="tabChange('close')"
            :state="tabs.close.state"
        >取引完了
        </app-tab-button>
      </div>
    </div>
    <div class="page__content">
      <div v-if="tabs.shipment.state" class="page__items">
        <buy-item-boxes :items="items" :show="0"/>
      </div>
      <div v-if="tabs.receipt.state" class="page__item">
        <buy-item-boxes :items="items" :show="1"/>
      </div>
      <div v-if="tabs.close.state" class="page__item">
        <buy-item-boxes :items="items" :show="2"/>
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
  name: "order_box",
  layout: 'mypage',
  components: {AppHeading, BuyItemBoxes, AppTabButton},
  async asyncData({params, $api, $myAuth}) {
    let items = {}
    const res = await $api['item-transaction'].getBySellerId($myAuth.user().id).then(
        ({data}) => {
          console.log(data)
          items = data.entries
        }
    )
    return {items: items}
  },
  data() {
    return {
      tabs: {
        shipment: {state: true},
        receipt: {state: false},
        close: {state: false}
      }
    }
  },
  methods: {
    tabChange(type) {
      if (type === 'shipment') {
        this.tabs.shipment.state = !this.tabs.shipment.state
        this.tabs.receipt.state = false
        this.tabs.close.state = false
      }
      if (type === 'receipt') {
        this.tabs.receipt.state = !this.tabs.receipt.state
        this.tabs.shipment.state = false
        this.tabs.close.state = false
      }
      if (type === 'close') {
        this.tabs.close.state = !this.tabs.close.state
        this.tabs.receipt.state = false
        this.tabs.shipment.state = false
      }
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