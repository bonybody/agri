<template>
  <div class="follow">
    <div class="follow__heading">
      <app-heading>フォローユーザー</app-heading>
    </div>

    <div class="follow__user-boxes">
      <follow-user-boxes/>
    </div>
  </div>
</template>

<script>
import FollowUserBoxes from "~/components/organisms/userBoxes/FollowUserBoxes";

export default {
  name: "follow",
  layout: 'mypage',
  components: {FollowUserBoxes}
}
</script>

<style scoped lang="scss">
.follow {
  &__heading {
    margin-bottom: $large-margin;
  }
}
</style>