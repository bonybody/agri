<template>
    <button v-if="!state" class="tab-button" @click="$emit('myClick')">
      {{ value }}
    </button>
    <button v-else="state" class="tab-button active" disabled>
      {{ value }}
    </button>
</template>

<script>
export default {
  name: "AppTabButton",
  props: {
    state: {
      type: Boolean,
      default: false
    },
    value: {
      type: String,
      default: 'タブ'
    }
  },
}
</script>

<style scoped lang="scss">
.tab-button {
  display: block;
  text-align: center;
  vertical-align: middle;
  color: $primary-color;
  background-color: $main-background-color;
  border: 2px solid $primary-color;
  border-radius: 1000px;
  width: 100%;
  height: 100%;
}

.active {
  color: $primary-on-font-color;
  background-color: $primary-color;
}
</style>