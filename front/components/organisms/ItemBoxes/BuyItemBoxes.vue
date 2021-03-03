<template>
  <div class="buy-item-boxes">
    <template v-for="item in items">
      <div class="buy-item-boxes__item">
        <transaction-item-box
            :id="item.id"
            :volume="item.item.volume"
            :price="item.item.price"
            :item-id="item.item.id"
            :name="item.item.name"
            :image="item.item.images[0].url"
            :state="item.state"
            :area="item.item.area"
            :set_count="item.set_count"
        />
      </div>
    </template>
  </div>
</template>

<script>
import TransactionItemBox from "~/components/molecules/item/TransactionItemBox";

export default {
  name: "BuyItemBoxes",
  components: {TransactionItemBox},
  props: {
    items: {
      type: Array,
      require: true
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