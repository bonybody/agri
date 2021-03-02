<template>
  <div class="item-detail">
    <div class="item-detail__not-logged-in-modal">
      <modal-window :show="notLoggedInModal" @close-modal="closeModal"></modal-window>
    </div>
    <div class="item-detail__left">
      <div class="image-list">
        <image-list :images="item.images" :meaning="'item-image'"></image-list>
      </div>
      <div class="item-favorite">
        <favorite-detail-botton :state="favorite" @myClick="onClickFavorite"/>
      </div>
    </div>
    <div class="item-detail__right">
      <item-text
          :item-id="item.id"
          :item-name="item.name"
          :volume="item.volume"
          :period="item.period"
          :price="item.price"
          :remaining_days="item.remaining_days"
          :remaining_format="item.remaining_format.name"
          :description="item.description"
          :set-count.sync="setCount"
          :category="item.category"
          :address="item.area"
          :user-name="item.user.display_name"
          :user-id="item.user.id"
          :user-image="item.user.image"
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
import ModalWindow from "~/components/molecules/ModalWindow";

export default {
  name: "ItemDetail",
  components: {ModalWindow, ItemText, FavoriteDetailBotton, ImageList},
  data() {
    return {
      favorite: true,
      setCount: 1,
      notLoggedInModal: false
    }
  },
  props: {
    item: {
      type: Object,
      require: false
    },
  },
  methods: {
    onClickFavorite: function () {
      this.favorite = !this.favorite;
    },
    buy: function () {
      if (!this.$myAuth.loggedIn()) {
        this.notLoggedInModal = true
        return
      }
      this.$api['item-transaction'].post({
        item_id: this.item.id,
        seller_id: this.item.user.id,
        buyer_id: this.$myAuth.user().id,
        set_count: this.setCount
      })
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
    },
    closeModal() {
      this.notLoggedInModal = !this.notLoggedInModal
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