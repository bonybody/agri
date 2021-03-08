<template>
  <div class="tran-item-detail">
    <p class="tran-item-detail__state tran-item-detail__section">
      {{ getStateText }}
    <p/>
    <div class="tran-item-detail__image tran-item-detail__section">
      <app-square-image :src="image" :alt="name"/>
    </div>
    <div class="tran-item-detail__user tran-item-detail__section">
      <div></div>
    </div>
    <p class="tran-item-detail__name tran-item-detail__section">{{ name }}</p>
    <p class="tran-item-detail__price tran-item-detail__section">価格：{{ price }}</p>

    <p class="tran-item-detail__volume tran-item-detail__section">内容量：{{ volume }}</p>
    <div class="tran-item-detail__actions button tran-item-detail__section">
      <template v-if="getCurrentUser === buyer_id">
        <div class="actions__button">
          <app-button v-if="state === 0" :none="state === 0" @myClick="receive()">商品発送までお待ち下さい</app-button>
          <app-button v-if="state === 1" @myClick="receive()">商品受け取り完了</app-button>
          <app-button v-if="state === 2" :none="state === 2" @myClick="receive()">取引完了</app-button>
        </div>
      </template>
      <template v-if="getCurrentUser === seller_id">
        <div class="actions__button">
          <app-button :none="state >= 1" @myClick="shipment()">商品発送完了</app-button>
        </div>
      </template>
    </div>
  </div>
</template>

<script>
import AppSquareImage from "~/components/atoms/images/AppSquareImage";
import AppButton from "~/components/atoms/buttons/AppButton";

export default {
  name: "TransactionItemDetail",
  components: {AppButton, AppSquareImage},
  props: {
    id: {
      type: Number,
      require: true
    },

    state: {
      type: Number,
      require: true
    },
    image: {
      type: String,
      require: true
    },
    name: {
      type: String,
      require: true
    },
    volume: {
      type: String,
      require: true
    },
    price: {
      type: Number,
      require: true
    },
    buyer_id: {
      type: Number,
      require: true
    },
    seller_id: {
      type: Number,
      require: true
    }

  },
  methods: {
    receive() {
      this.$api['item-transaction'].receive(this.id).then(
          ({data}) => {
            console.log(data)
          }
      )
    },
    shipment() {
      this.$api['item-transaction'].shipment(this.id).then(
          ({data}) => {
            console.log(data)
          }
      )

    }
  },
  computed: {
    getCurrentUser() {
      console.log(this.seller_id)
      return this.$myAuth.user().id
    },
    getStateText() {
      let res = ''
      switch (this.state) {
        case 0:
          res = '発送確認待ち'
          break
        case 1:
          res = '受け取り確認待ち'
          break
        case 2:
          res = '取引完了'
          break
      }
      return res
    }
  }
}
</script>

<style scoped lang="scss">
.tran-item-detail {
  width: 400px;
  box-sizing: border-box;
  padding: $medium-parts-margin;
  background-color: $main-background-color;
  border-radius: $box-border-radius;

  &__section {
    margin-bottom: $medium-parts-margin;
  }

  &__state {
    text-align: center;
    color: $accent-color;
    font-size: $large-font-size;
  }

  &__image {
    width: 200px;
    height: 200px;
    margin: 0 auto;
  }

  &__name {
    font-size: $semi-large-font-size;
    font-weight: bold;
  }
}

.actions {
  &__button {
    width: 200px;
    height: 30px;
    margin: 0 auto $medium-parts-margin auto;
  }
}
</style>