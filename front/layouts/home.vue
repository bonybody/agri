<template>
  <div>
    <div class="header">
      <the-header></the-header>
    </div>
    <p class="heading-images">
      <img rel="prefetch" src="~assets/images/index-swiper/swiper3.jpeg" alt="">
    </p>
    <Nuxt/>
  </div>
</template>

<style scoped lang="scss">
.heading-images {
  margin-bottom: 30px;
}

.heading-images {
  width: 100%;
  height: 300px;

  img {
    width: 100%;
    height: 300px;
    object-fit: cover;
  }
}

</style>
<script>
import TheHeader from "~/components/organisms/commons/TheHeader";

export default {
  name: 'home',
  components: {TheHeader}
}
</script>