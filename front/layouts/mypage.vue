<template>
  <div class="my-page-layout">
    <div class="header">
      <the-header></the-header>
    </div>
    <div class="my-page-layout__content">
      <div class="my-page-menu">
        <my-page-menu/>
      </div>
      <main class="my-page-layout__main">
        <Nuxt/>
      </main>
    </div>
  </div>
</template>

<script>
import MyPageMenu from "~/components/molecules/menu/MyPageMenu";

export default {
  name: "mypage",
  components: {MyPageMenu}
}
</script>

<style scoped lang="scss">
.header {
  margin-bottom: 30px;
}

.my-page-layout {
  &__content {
    margin: 0 auto;
    max-width: 1024px;
    display: flex;
    justify-content: space-between;
  }

  &__main {
    width: 800px;
  }
}

</style>