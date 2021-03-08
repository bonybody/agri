<template>
  <div class="items">
    <template v-for="record in records" v-if="records">
      <div class="items__item">
        <item-box
            :item-id="record.item.id"
            :image="record.item.images.length ? record.item.images[0].url : ''"
            :name="record.item.name"
            :address="record.item.area"
            :price="record.item.price"
            :remaining="record.item.remaining_days"
            :remaining_format="record.item.remaining_format.name"
            :period="record.item.period"
            :set-count="record.set_count"
            :favorite="Boolean(record.favorite)"
        />
      </div>
    </template>
  </div>
</template>

<script>
import ItemBox from "~/components/molecules/ItemBox";

export default {
  name: "SearchItemBoxes",
  components: {ItemBox},
  props: {
    records: {
      type: Array,
      require: true
    }
  }
}
</script>

<style scoped lang="scss">
.items {
  display: flex;
  flex-wrap: wrap;
  justify-content: left;

  &__item {
    margin-right: 20px;
    margin-bottom: 20px;
  }
}
</style>