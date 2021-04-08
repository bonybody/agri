<template>
  <div class="my-page">
    <my-page-menu></my-page-menu>
  </div>
</template>

<script>
import MyPageMenu from "~/components/molecules/menu/MyPageMenu";
export default {
  name: 'index',
  components: {MyPageMenu},
  transition: 'page'
}
</script>

<style scoped>

</style>