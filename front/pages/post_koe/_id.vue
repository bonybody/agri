<template>
  <div class="koe-post">
    <div class="koe-post__item">
      <item-box
          :item-id="record.item.id"
          :image="record.item.images[0].url"
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
    <div class="koe-post__form">
      <koe-post-form
          :item-id="record.item.id"
      />
    </div>

  </div>
</template>

<script>
import KoePostForm from "~/components/organisms/forms/KoePostForm";
import ItemText from "~/components/molecules/item/ItemText";
import ItemAbout from "~/components/molecules/item/ItemAbout";
import ItemDetail from "@/components/organisms/items/ItemDetail";
import ItemBox from "@/components/molecules/ItemBox";

export default {
  components: {ItemBox, ItemDetail, ItemAbout, ItemText, KoePostForm},
  layout: 'mypage',
  async asyncData({params, $api}) {
    let record = {}
    const res = await $api['item'].getById(params.id).then(
        ({data}) => {
          console.log(data)
          record = data.entries
        }
    )
    return {record: record}
  },
  data() {
    return {
      record: {}
    }
  }
}
</script>

<style scoped lang="scss">
.koe-post {
  display: flex;
  justify-content: space-around;

  &__item {
  }

  &__form {
    width: 400px;
    margin-bottom: $large-margin;
  }
}
</style>