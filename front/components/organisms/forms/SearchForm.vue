<template>
  <div class="search">
    <form @submit.prevent="$emit('search', {
        text: text.value,
        category: category.value,
        orderBy: orderBy.value })">
      <div class="search__text">
        <search-bar @click="" v-model="text.value"/>
      </div>
      <div class="search__select">
        <item-category-form v-model="category.value" :select-null="true" :require="false"/>
      </div>
      <div class="search__select">
        <order-by-form v-model="orderBy.value" :require="false"/>
      </div>
    </form>

  </div>
</template>

<script>
import SearchBar from "@/components/molecules/SearchBar";
import ItemCategoryForm from "@/components/molecules/forms/ItemCategoryForm";
import OrderByForm from "@/components/molecules/forms/OrderByForm";
import AppTabButton from "@/components/atoms/buttons/AppTabButton";

export default {
  name: "SearchForm",
  components: {AppTabButton, OrderByForm, ItemCategoryForm, SearchBar},
  created() {
    if (this.$route.query.text) {
      this.text.value = this.$route.query.text
    }
    if (this.$route.query.category) {
      this.category.value = this.$route.query.category
    }
    if (this.$route.query.orderBy) {
      this.orderBy.value = this.$route.query.orderBy
    }
  },
  data() {
    return {
      text: {
        value: null,
        require: true
      },
      category: {
        value: null,
        require: false
      },
      orderBy: {
        value: 1,
        require: false
      },
    }
  },
}
</script>

<style scoped lang="scss">
.search {
  background-color: $main-background-color;
  border-radius: $box-border-radius;
  box-sizing: border-box;
  padding: $medium-parts-margin;
  margin: 0 auto;

  &__text {
    margin-bottom: $semi-large-margin;
  }

  &__select {
    display: inline-block;
    width: 40%;
  }
}
</style>