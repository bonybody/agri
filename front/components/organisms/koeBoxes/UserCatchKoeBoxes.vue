<template>
  <div class="user-catch-koe-boxes">
    <template v-for="n in numbers">
      <div class="user-catch-koe-boxes__box">
        <koe-box/>
      </div>
    </template>
  </div>
</template>

<script>
export default {
  name: "UserCatchKoeBoxes",
  data() {
    return {
      numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    }
  }
}
</script>

<style scoped lang="scss">
.user-catch-koe-boxes {
  display: flex;
  flex-wrap: wrap;
  justify-content: left;

  &__box {
    margin-right: 25px;
    margin-bottom: 25px;

    &:last-child {
      margin-right: 0;
    }

  }

}

</style>