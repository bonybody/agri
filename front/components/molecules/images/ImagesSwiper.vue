<template>
  <div class="images-swiper">
    <swiper>
      <swiper-slide><img src="~/assets/images/index-swiper/swiper1.jpeg" alt=""></swiper-slide>
      <swiper-slide><img src="~/assets/images/index-swiper/swiper2.jpeg" alt=""></swiper-slide>
      <swiper-slide><img src="~/assets/images/index-swiper/swiper3.jpeg" alt=""></swiper-slide>
      <swiper-slide><img src="~/assets/images/index-swiper/swiper4.jpeg" alt=""></swiper-slide>
    </swiper>
  </div>
</template>

<script>
export default {
  name: "ImagesSwiper",
  data() {
    return {
      swiperOption: {
        speed: 1000,//スライドの切り替わりスピード
        spaceBetween: 30,//各スライドの余白
        centeredSlides: true,//スライダーを真ん中に
        loop: true, //無限ループ
        autoplay: { //スライドの自動切り替え
          delay: 5000,//スライドの自動切り替えの秒数
          disableOnInteraction: false//何らかのアクション後の自動切り替えを再開
        }
      },
      pagination: { //ページネーション設定
        el: '.swiper-pagination',
        clickable: true
      },
      navigation: { //ナビゲーション設定
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev'
      }
    }
  }
}
</script>

<style scoped lang="scss">
img {
  width: 100%;
  height: 300px;
  object-fit: cover;
  object-position: center;
}
</style>