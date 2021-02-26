<template>
  <div class="new-koe-boxes">
    <template v-for="n in numbers">
      <div class="new-koe-boxes__box">
        <koe-box/>
      </div>
    </template>
  </div>
</template>

<script>
import KoeBox from "~/components/molecules/KoeBox";

export default {
  name: "FavoriteKoeBoxes",
  components: {KoeBox},
  data() {
    return {
      numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    }
  }

}
</script>

<style scoped lang="scss">
.new-koe-boxes {
  display: flex;
  flex-wrap: wrap;
  justify-content: left;

  &__box {
    margin-right: 20px;
    margin-bottom: 20px;
  }

}
</style>