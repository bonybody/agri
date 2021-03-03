<template>
  <div class="wrap">
    <div class="mypage-menu">
      <my-page-menu/>
    </div>

    <div class="transaction">
      <div class="transaction__heading">
        <app-heading>取引詳細画面</app-heading>
      </div>
      <div class="transaction__detail">
        <transaction-item-detail
            :id="transaction.id"
            :state="transaction.state"
            :name="transaction.item.name"
            :price="transaction.item.price * transaction.set_count"
            :volume="transaction.item.volume + '×' + transaction.set_count"
            :image="transaction.item.images[0].url"
            :buyer_id="transaction.buyer.id"
            :seller_id="transaction.seller.id"
        />
      </div>
    </div>
  </div>
</template>

<script>
import AppHeading from "~/components/atoms/headings/AppHeading";
import TransactionItemDetail from "~/components/molecules/item/TransactionItemDetail";
import MyPageMenu from "~/components/molecules/menu/MyPageMenu";

export default {
  components: {MyPageMenu, TransactionItemDetail, AppHeading},
  async asyncData({params, $api}) {
    let result = {}
    await $api['item-transaction'].getById(params.id).then(
        ({data}) => {
          console.log(data)
          result = data.entries
        })
    return {
      transaction: result
    }
  },
}
</script>

<style scoped lang="scss">
.wrap {
  max-width: 1024px;
  margin: 0 auto;
  display: flex;
}

.transaction {
  margin: 0 auto;

  &__heading {
    margin-bottom: $medium-parts-margin;
  }
}
</style>