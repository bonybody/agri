<template>
  <button
      @click="$emit('myClick')"
      class="user-follow-button"
      :class="{ 'follow': state, 'not-follow': !state }"
  >
    {{ getText }}
  </button>
</template>

<script>
export default {
  name: "AppUserFollowButton",
  props: {
    state: {
      type: Boolean,
      default: false
    }
  },
  computed: {
    getText() {
      if (this.state) {
        return 'フォロー中'
      }
      if (!this.state) {
        return 'フォローする'
      }
    }
  }
}
</script>

<style scoped lang="scss">
.user-follow-button {
  display: inline-block;
  width: 100%;
  height: 100%;
  background-color: $main-background-color;
  text-align: center;
  vertical-align: middle;
  border: 2px solid $primary-color;
  border-radius: 1000px;
}

.follow {
  background-color: $primary-color;
  color: $primary-on-font-color;
}

.not-follow {
  color: $primary-color;
}
</style>