<template>
  <div class="container">
    <section class="new-item">
      <h1 class="section-header">新着商品</h1>
      <new-item-boxies/>
    </section>
    <section>
      <h1 class="section-header">新しいみんなのコエ</h1>
      <new-koe-boxes/>
    </section>
  </div>
</template>

<script>
import kuro334 from '../components/test/kuro334.vue';
import NewItemBoxies from "~/components/organisms/ItemBoxies/NewItemBoxies";
import NewKoeBoxes from "~/components/organisms/koeBoxies/NewKoeBoxes";

export default {
  auth: "guest",
  components: {NewKoeBoxes, NewItemBoxies, kuro334},
  mounted() {
    console.log(this.$auth.loggedIn);
  },
}
</script>

<style lang="scss">
.container {
  margin: 0 auto;
  width: 1024px;
}

section {
  margin-bottom: $large-margin;
}

.section-header {
  font-size: 1.2rem;
  font-weight: bold;
  margin-bottom: $large-margin;
}

</style>
