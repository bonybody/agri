<template>
  <div>
    <div class="header">
      <the-header></the-header>
    </div>
    <main>
      <Nuxt/>
    </main>
  </div>
</template>

<style scoped lang="scss">
.header {
  margin-bottom: $large-margin;
}
</style>
<script>
import TheHeader from "~/components/organisms/commons/TheHeader";

export default {
  components: {TheHeader}
}
</script>