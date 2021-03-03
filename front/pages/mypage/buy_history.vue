<template>
  <div class="buy-history">
    <div class="buy-history__heading">
      <app-heading>購入履歴</app-heading>
    </div>
    <div class="buy-history__items">
      <buy-item-boxes :items="items"/>
    </div>
  </div>
</template>

<script>
import BuyItemBoxes from "~/components/organisms/ItemBoxes/BuyItemBoxes";
import AppHeading from "~/components/atoms/headings/AppHeading";

export default {
  name: "buy_history",
  layout: 'mypage',
  components: {AppHeading, BuyItemBoxes},
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

}
</script>

<style scoped lang="scss">
.buy-history {
  &__heading {
    margin-bottom: $medium-parts-margin;
  }
}
</style>