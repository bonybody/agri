<template>
  <div class="follow">
    <follow-user-boxes/>
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

<style scoped>

</style>