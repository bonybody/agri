<template>
  <div class="user-items">
    <template v-for="n in numbers">
      <div class="user-items__item">
        <item-box/>
      </div>
    </template>
  </div>
</template>

<script>
import ItemBox from "~/components/molecules/ItemBox";

export default {
  name: "UserItemBoxes",
  components: {ItemBox},
  data() {
    return {
      numbers: [1, 2, 3, 4, 5],
    }
  }
}
</script>

<style scoped lang="scss">
.user-items {
  display: flex;
  flex-wrap: wrap;
  justify-content: left;

  &__item {
    margin-right: 20px;
    margin-bottom: 20px;

    &:last-child {
      margin-right: 0;
    }

  }


}
</style>