<template>
  <div class="searchBar">
    <input v-model="text" class="searchBar__text" type="text" name="text" placeholder="文字を入力してください" maxlength="30">
    <nuxt-link class="searchBar__button" :to="searchTo">検索</nuxt-link>
  </div>
</template>

<script>

export default {
  name: "searchForm",
  data() {
    return {
      text: '',
      placeholder: '文字を入力してください。'
    }
  },
  computed: {
    searchTo() {
      const searchParam = {}
      searchParam.path = '/search';

      if (this.text) {
        searchParam.query = { text: this.text }
      }
      return searchParam
    }
  }
}
</script>

<style scoped lang="scss">

.searchBar {
  display: flex;
  flex-wrap: nowrap;
  justify-content: center;
}
.searchBar__text {
  width: 500px;
  display: block;
  border: 1px solid $main-font-color;
  line-height: 30px;
  padding: 0 10px;
  border-radius: 10px 0 0 10px;
}
.searchBar__button {
  display: block;
  border-radius: 0 10px 10px 0;
  border: 1px solid $main-font-color;
  border-left: 0;
  line-height: 30px;
  padding: 0 15px;
}
</style>