<template>
  <div class="container">
    <p class="section-header">新着商品</p>
    <new-item-boxies />
  </div>
</template>

<script>
import kuro334 from '../components/test/kuro334.vue';
import NewItemBoxies from "~/components/organisms/ItemBoxies/NewItemBoxies";
export default {
  auth: "guest",
  components: {NewItemBoxies, kuro334 },
  mounted() {
    console.log(this.$auth.loggedIn);
  },
}
</script>

<style lang="scss">
.container {
  //background-color: $primary-color;
  margin: 0 auto;
  width: 1024px;
}

.section-header {
  font-size: 1.2rem;
  font-weight: bold;
}

</style>
