<template>
  <div class="favorite-items">
    <template v-for="n in numbers">
      <div class="favorite-items__item">
        <item-box/>
      </div>
    </template>
  </div>
</template>

<script>
import ItemBox from "~/components/molecules/ItemBox";

export default {
  name: "FavoriteItemBoxes",
  components: {ItemBox},
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