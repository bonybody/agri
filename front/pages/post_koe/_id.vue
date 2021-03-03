<template>
  <div class="koe-post">
    <div class="koe-post__item">
      <item-about
          :item-id="item.id"
          :item-name="item.name"
          :item-image="item.images[0].url"
          :volume="item.volume"
          :period="item.period"
          :price="item.price"
          :remaining_days="item.remaining_days"
          :remaining_format="item.remaining_format.name"
          :description="item.description"
          :set-count.sync="setCount"
          :category-id="item.category.id"
          :category-name="item.category.name"
          :address="item.area"
          :user-name="item.user.display_name"
          :user-id="item.user.id"
          :user-image="item.user.image"
          @edit="edit()"
      />
    </div>
    <div class="koe-post__form">
      <koe-post-form
          :item-id="item.id"
      />
    </div>
  </div>
</template>

<script>
import KoePostForm from "~/components/organisms/forms/KoePostForm";
import ItemText from "~/components/molecules/item/ItemText";
import ItemAbout from "~/components/molecules/item/ItemAbout";
export default {
  components: {ItemAbout, ItemText, KoePostForm},
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

}
</script>

<style scoped lang="scss">
.koe-post {
  width: 1024px;
  margin: 0 auto;
  display: flex;
  justify-content: space-around;
  &__form {
    width: 400px;
  }
}
</style>