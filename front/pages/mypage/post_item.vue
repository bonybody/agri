<template>
  <div class="page">
    <div class="page__heading">
      <app-heading>出品商品</app-heading>
    </div>
    <div class="page__tabs">
      <div class="page__tab page__tab--item">
        <app-tab-button
            @myClick="changeShowState(100)"
            :state="showState ===100"
        >すべて
        </app-tab-button>
      </div>
      <div class="page__tab page__tab--item">
        <app-tab-button
            @myClick="changeShowState(1)"
            :state="showState === 1"
        >出品中
        </app-tab-button>
      </div>
      <div class="page__tab page__tab--koe">
        <app-tab-button
            @myClick="changeShowState(0)"
            :state="showState === 0"
        >出品停止中
        </app-tab-button>
      </div>
    </div>
    <div class="page__content">
      <div v-if="tabs.all.state" class="page__items">
        <post-item-boxes :show="showState"/>
      </div>
    </div>
  </div>
</template>

<script>
import BuyItemBoxes from "~/components/organisms/ItemBoxes/BuyItemBoxes";
import AppHeading from "~/components/atoms/headings/AppHeading";
import AppTabButton from "@/components/atoms/buttons/AppTabButton";
import PostItemBoxes from "@/components/organisms/ItemBoxes/PostItemBoxes";

export default {
  name: "post_item",
  layout: 'mypage',
  components: {PostItemBoxes, AppHeading, BuyItemBoxes, AppTabButton},
  async asyncData({params, $api, $myAuth}) {
    let items = {}
    const res = await $api['item'].getByUserIdAll($myAuth.user().id).then(
        ({data}) => {
          console.log(data)
          items = data.entries
        }
    )
    return {items: items}
  },
  data() {
    return {
      showState: 100,
      tabs: {
        all: {state: true},
        now: {state: false},
        close: {state: false}
      }
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