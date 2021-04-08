<template>
  <div class="new-items">
    <template v-for="item in items">
      <div class="new-items__item">
        <item-box
            :item-id="item.item.id"
            :name="item.item.name"
            :image="item.item.images.length ? item.item.images[0].url : ''"
            :address="item.item.address"
            :price="item.item.price"
            :remaining="item.item.remaining"
            :remaining_format="item.item.remaining_format.name"
            :period="item.item.period"
            :favorite="Boolean(item.favorite)"
            :set-count="item.set_count"
        />
      </div>
    </template>
  </div>
</template>

<script>
import ItemBox from "~/components/molecules/ItemBox";

export default {
  name: "UserItemBoxes",
  components: {ItemBox},
  async fetch() {
    const res = await this.$api['item'].getByUserIdAll(this.id)
        .then(({data}) => data)
        .catch(error => false)
    if (res) {
      console.log(res)
      this.items = res.entries
    }
  },
  props: {
    id: {
      type: Number,
      require: true,
    }
  },
  data() {
    return {
      items: []
    }
  },
}
</script>

<style scoped lang="scss">
.new-items {
  display: flex;
  flex-wrap: wrap;
  justify-content: left;

  &__item {
    margin-right: 20px;
    margin-bottom: 20px;
  }
}
</style>