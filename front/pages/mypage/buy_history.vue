<template>
  <div class="buy-history">
    <div class="buy-history__items">
      <buy-item-boxes :items="items"/>
    </div>
  </div>
</template>

<script>
import BuyItemBoxes from "~/components/organisms/ItemBoxes/BuyItemBoxes";

export default {
  name: "buy_history",
  layout: 'mypage',
  components: {BuyItemBoxes},
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

<style scoped>

</style>