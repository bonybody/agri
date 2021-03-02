<template>
  <div class="item">
    <div class="item__detail">
      <item-detail :item="item"></item-detail>
    </div>
    <div class="item__catch-koe">
      <div class="koe">
        <div class="item__heading">
          <app-heading>この商品に届いたコエ</app-heading>
        </div>
        <div class="koe-lists">
          <item-catch-koe-boxes/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ItemDetail from "~/components/organisms/items/ItemDetail";
import ItemCatchKoeBoxes from "~/components/organisms/koeBoxes/ItemCatchKoeBoxes";
import AppHeading from "~/components/atoms/headings/AppHeading";

export default {
  components: {AppHeading, ItemCatchKoeBoxes, ItemDetail},
  auth: false,
  async asyncData({params, $api}) {
    let item = {}
    const res = await $api['item'].getById(params.id).then(
        ({data}) => {
          console.log(data)
          item = data.entries
        }
    )
    return {item: item}
  },
  mounted() {
    console.log(this.item)
  }
}
</script>

<style scoped lang="scss">
.item {
  max-width: 1024px;
  margin: 0 auto;

  &__detail {
    margin-bottom: $large-margin;
  }

  &__heading {
    margin-bottom: $semi-large-margin;
  }

  &__catch-koe {
  }
}

</style>