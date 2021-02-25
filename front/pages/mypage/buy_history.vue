<template>
  <div class="buy-history">
    <div class="buy-history__items">
      <buy-item-boxes/>
    </div>
  </div>
</template>

<script>
import BuyItemBoxes from "~/components/organisms/ItemBoxes/BuyItemBoxes";

export default {
  name: "buy_history",
  layout: 'mypage',
  components: {BuyItemBoxes}
}
</script>

<style scoped>

</style>