<template>
  <div class="new-items">
    <template v-for="item in items" v-if="items !== []">
      <div class="new-items__item">
        <item-box
            :item-id="item.id"
            :image="item.images[0].url"
            :name="item.name"
            :address="item.area"
            :price="item.price"
            :remaining="item.remaining_days"
            :remaining_format="item.remaining_format.name"
            :period="item.period"
        />
      </div>
    </template>
  </div>
</template>

<script>
import ItemBox from "~/components/molecules/ItemBox";

export default {
  name: "NewItemBoxies",
  components: {ItemBox},
  data() {
    return {
      items: null
    }
  },
  async fetch() {
    const res = await this.$api['item'].getNewItems().then(({data}) => {
      this.items = data.entries
      this.state = data.state
      console.log(data.entries[0])
      // console.log(data.entries[0].images[0])
    })
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