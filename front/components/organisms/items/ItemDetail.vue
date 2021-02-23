<template>
  <div class="item-detail">
    <div class="item-detail__left">
      <div class="image-list">
        <image-list :meaning="'item-image'"></image-list>
      </div>
      <div class="item-favorite">
        <favorite-detail-botton :state="favorite" @myClick="onClickFavorite"/>
      </div>
    </div>
    <div class="item-detail__right">
      <item-text
          :set-count.sync="setCount"
          @buy="buy()"
          @edit="edit()"
      />
    </div>
  </div>
</template>

<script>
import ImageList from "~/components/molecules/images/ImageList";
import FavoriteDetailBotton from "~/components/atoms/buttons/FavoriteDetailBotton";
import ItemText from "~/components/molecules/item/ItemText";

export default {
  name: "ItemDetail",
  components: {ItemText, FavoriteDetailBotton, ImageList},
  data() {
    return {
      favorite: true,
      setCount: 1
    }
  },
  methods: {
    onClickFavorite: function () {
      this.favorite = !this.favorite;
    },
    buy: function () {
      console.log("--購入--");
      console.log("購入確認ダイアログを表示");
      console.log("ダイアログの確認ボタンを押せば購入処理（Axios）");
      console.log("ダイアログのキャンセルボタンを押せばダイアログを閉じる");
      console.log("--購入終わり--");
    },
    edit: function () {
      console.log("--編集--");
      console.log("商品編集画面に移行");
      console.log("--編集終わり--");
    }
  }
}
</script>

<style scoped lang="scss">
.item-detail {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  max-width: 1024px;
  margin: 0 auto;

  &__left {
    margin-right: 24px;

    .item-favorite {
      margin-top: 30px;
      @include center-flex;
    }
  }
}
</style>