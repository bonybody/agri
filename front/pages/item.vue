<template>
  <div class="item">
    <item-detail></item-detail>
  </div>
</template>

<script>
import ItemDetail from "~/components/organisms/items/ItemDetail";
export default {
  name: "item",
  components: {ItemDetail},
  auth: 'guest'
}
</script>

<style scoped>

</style>