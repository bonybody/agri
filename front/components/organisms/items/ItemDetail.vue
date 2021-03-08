<template>
  <div class="item-detail">
    <div class="item-detail__not-logged-in-modal">
      <login-require-window
          :show-modal="notLoggedInModal"
          @close-modal="closeModal"
      />
    </div>
    <div class="item-detail__content">
      <div class="item-detail__left">
        <div class="image-list">
          <image-list :images="item.images" :meaning="'item-image'"></image-list>
        </div>
        <div class="item-favorite">
          <favorite-detail-botton :state="getFavorite" @myClick="onClickFavorite"/>
        </div>
      </div>
      <div class="item-detail__right">
        <item-text
            :item-id="item.id"
            :item-name="item.name"
            :volume="item.volume"
            :period="item.period"
            :price="item.price"
            :remaining-sets="item.remaining_days"
            :remaining_format="item.remaining_format.name"
            :remaining-set-count="remainingSetCount"
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
  </div>
</template>

<script>
import ImageList from "~/components/molecules/images/ImageList";
import FavoriteDetailBotton from "~/components/atoms/buttons/FavoriteDetailBotton";
import ItemText from "~/components/molecules/item/ItemText";
import ModalWindow from "~/components/molecules/ModalWindow";
import AppLinkButton from "@/components/atoms/buttons/AppLinkButton";
import LoginRequireWindow from "@/components/organisms/modal_windows/LoginRequireWindow";

export default {
  name: "ItemDetail",
  components: {LoginRequireWindow, AppLinkButton, ModalWindow, ItemText, FavoriteDetailBotton, ImageList},
  data() {
    return {
      setCount: 1,
      notLoggedInModal: false,
      thisFavorite: {
        state: false,
        value: false
      }
    }
  },
  props: {
    item: {
      type: Object,
      require: false
    },
    remainingSetCount: {
      type: Number,
      require: true
    },
    favorite: {
      type: Boolean,
      require: true
    }
  },
  computed: {
    getFavorite() {
      if (this.thisFavorite.state) {
        return this.thisFavorite.value
      } else {
        return this.favorite
      }
    }
  },
  methods: {
    onClickFavorite: function () {
      if (!this.$myAuth.loggedIn()) {
        this.notLoggedInModal = true
        return
      }
      if (this.thisFavorite.state) {
        this.thisFavorite.value = !this.thisFavorite.value
      } else {
        this.thisFavorite.value = !this.favorite
        this.thisFavorite.state = true
      }
      this.$api['favorite'].postItem(this.$myAuth.user().id, this.item.id)
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
      }).then(({data}) => {
        if (data.state) {
          this.$router.push('/transaction/' + data.id)
        }
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
  max-width: 1024px;
  margin: 0 auto;
  &__content {
    width: 100%;
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
  }

  &__left {
    margin-right: 24px;
    margin-bottom: $large-margin;

    .item-favorite {
      margin-top: 30px;
      @include center-flex;
    }
  }
}
</style>