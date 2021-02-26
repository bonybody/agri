<template>
  <div class="follow-user-boxes">
    <template v-for="n in numbers">
      <div class="follow-user-boxes__box">
        <user-box/>
      </div>
    </template>
  </div>
</template>

<script>
import KoeBox from "~/components/molecules/KoeBox";
import UserBox from "~/components/molecules/user/UserBox";

export default {
  name: "FollowUserBoxes",
  components: {UserBox, KoeBox},
  data() {
    return {
      numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    }
  }

}
</script>

<style scoped lang="scss">
.follow-user-boxes {
  display: flex;
  flex-wrap: wrap;
  justify-content: left;

  &__box {
    margin-right: 20px;
    margin-bottom: 20px;
  }

}
</style>