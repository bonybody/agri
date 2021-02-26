<template>
  <div>
    <div class="header">
      <the-header></the-header>
    </div>
    <Nuxt/>
  </div>
</template>

<style scoped lang="scss">
.header {
  margin-bottom: 30px;
}
</style>
<script>
import TheHeader from "~/components/organisms/commons/TheHeader";

export default {
  components: {TheHeader}
}
</script>