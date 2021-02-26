<template>
  <div class="buy-item-boxes">
    <template v-for="n in numbers">
      <div class="buy-item-boxes__item">
        <buy-item-box/>
      </div>
    </template>
  </div>
</template>

<script>
import BuyItemBox from "~/components/molecules/item/BuyItemBox";

export default {
  name: "BuyItemBoxes",
  components: {BuyItemBox},
  data() {
    return {
      numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    }
  }
}
</script>

<style scoped lang="scss">
.favorite-items {
  display: flex;
  flex-wrap: wrap;
  justify-content: left;

  &__item {
    margin-right: 20px;
    margin-bottom: 20px;
  }
}
</style>