<template>
  <button :class="{ active: state }" @click="$emit('click')">
    <span><slot></slot></span>
  </button>
</template>

<script>
export default {
  name: "BaseTabButton",
  data: () => {
    state: true
  }
}
</script>

<style scoped>
button {
  font-size: 16px;
}
</style>
