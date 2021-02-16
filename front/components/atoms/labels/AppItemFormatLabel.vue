<template>
  <div class="item-format-label">
    {{ '残り' +　format + '日' }}
  </div>
</template>

<script>
export default {
  name: "AppItemFormatLabel",
  props: {
    format: {
      type: String,
      default: '単品'
    }
  }
}
</script>

<style scoped lang="scss">
.item-format-label {
  border-radius: 100px;
  display: block;
  padding: 3px 10px;
  box-sizing: content-box;
  color: $primary-on-font-color;
}

.single {
  background-color: $accent-color;
}

.week {
  background-color: $primary-color;
}
</style>