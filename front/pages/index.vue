<template>
  <div class="container">
    <section class="categories">
      <h1 class="section-header">カテゴリから探す</h1>
      <div class="categories__content">
        <template v-for="category in categories">
          <nuxt-link
              :key="category.id"
              class="category"
              :to="{
                path: '/search',
                query: { category: category.id }
              }"
          >
            <img rel="prefetch" class="category__image" :src="category.image" :alt="category.name">
            <span class="category__name">{{ category.name }}</span>
          </nuxt-link>
        </template>
      </div>
    </section>
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
import NewItemBoxies from "~/components/organisms/ItemBoxes/NewItemBoxies";
import NewKoeBoxes from "~/components/organisms/koeBoxes/NewKoeBoxes";
import ImagesSwiper from "~/components/molecules/images/ImagesSwiper";

export default {
  name: 'index',
  transition: 'page',
  layout: 'home',
  auth: false,
  components: {ImagesSwiper, NewKoeBoxes, NewItemBoxies},
  data() {
    return {
      categories: [
        {
          id: 1,
          name: '米・穀物',
          image: require('~/assets/images/categories/grain.jpg')
        },
        {
          id: 2,
          name: '野菜',
          image: require('~/assets/images/categories/vegetables.jpg')
        },
        {
          id: 3,
          name: '果物',
          image: require('~/assets/images/categories/fruits.jpg')
        },
        {
          id: 4,
          name: 'その他',
          image: require('~/assets/images/categories/mushroom.jpg')
        }
      ]
    }
  },
  mounted() {
    console.log(this.$auth.loggedIn);
  },
}
</script>

<style lang="scss" scoped>
.container {
  margin: 0 auto;
  width: 1024px;
}

section {
  box-sizing: content-box;
  padding: 0 12px;

  margin-bottom: $large-margin;
}

.section-header {
  font-size: 1.2rem;
  font-weight: bold;
  margin-bottom: $large-margin;
}

.categories {
  &__content {
    display: flex;
    justify-content: space-between;
  }
}

.category {
  display: block;
  position: relative;
  width: 200px;
  height: 100px;
  &:hover {
    filter: brightness(60%);
  }


  &__image {
    position: absolute;
    z-index: 1;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: $box-border-radius;
    filter: brightness(40%);
  }

  &__name {
    position: absolute;
    display: inline-block;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    margin: auto;
    width: fit-content;
    height: fit-content;
    z-index: 2;
    color: $primary-on-font-color;
  }
}

</style>
