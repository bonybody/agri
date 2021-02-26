<template>
  <div class="user-id">
    <user-detail/>
  </div>
</template>

<script>
import UserProfile from "~/components/molecules/user/UserProfile";
import UserDetail from "~/components/organisms/user/UserDetail";

export default {
  name: "_id",
  components: {UserDetail, UserProfile},
  auth: false,

}
</script>

<style scoped>

</style>