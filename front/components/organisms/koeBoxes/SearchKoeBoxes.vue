<template>
  <div class="favorite-koe-boxes">
    <template v-for="koe in koeLists">
      <div class="favorite-koe-boxes__box">
        <koe-box
            :id="koe.id"
            :user-id="koe.user.id"
            :user-name="koe.user.name"
            :item-id="koe.item.id"
            :item-name="koe.item.name"
            :koe-title="koe.title"
            :koe-text="koe.text"
            :post-day="koe.created_at"
        />
      </div>
    </template>
  </div>
</template>

<script>
import KoeBox from "~/components/molecules/koe/KoeBox";

export default {
  name: "SearchKoeBoxes",
  components: {KoeBox},
  props: {
    koeLists: {
      type: Array,
      require: true
    }
  }


}
</script>

<style scoped lang="scss">
.favorite-koe-boxes {
  display: flex;
  flex-wrap: wrap;
  justify-content: left;

  &__box {
    margin-right: 20px;
    margin-bottom: 20px;
  }

}
</style>