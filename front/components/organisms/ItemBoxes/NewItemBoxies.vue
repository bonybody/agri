<template>
  <div class="new-items">
    <template v-for="n in numbers">
      <div class="new-items__item">
        <item-box/>
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
      numbers: [1, 2, 3, 4, 5],
    }
  }
}
</script>

<style scoped lang="scss">
.new-items {
  display: flex;
  flex-wrap: wrap;
  justify-content: left;

  &__item {
    margin-right: 25px;
    margin-bottom: 25px;

    &:last-child {
      margin-right: 0;
    }
  }
}
</style>