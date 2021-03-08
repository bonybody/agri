<template>
  <div class="user-id">
    <user-detail
    />
  </div>
</template>

<script>
import UserDetail from "~/components/organisms/user/UserDetail";

export default {
  name: "_id",
  components: {UserDetail},
  auth: false,
  async asyncData({ $api, $myAuth, param }) {
    const res = $api['user'].get
  }
}
</script>

<style scoped>

</style>