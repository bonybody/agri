<template>
  <div class="new-items">
    <template v-for="n in numbers">
      <item-box/>
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
      item: {
        name: '【今週限りの販売】豊橋の美味しいキャベツ',
      }
    }
  }
}
</script>

<style scoped>
.new-items {
  display: flex;
  flex-wrap: wrap;
  justify-content: left;
}
</style>