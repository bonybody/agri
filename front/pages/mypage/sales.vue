<template>
  <div class="page">
    <div class="page__heading">
      <app-heading>売上管理</app-heading>
    </div>
    <div class="page__content">
      <div class="page__detail detail">
        <div class="detail__heading">
          <app-heading>売上詳細</app-heading>
        </div>
        <div class="detail__row" v-if="salesDetail">
          売上残高：{{ salesDetail }}円（うち手数料{{ salesDetail * 0.3 }}円）
        </div>
        <div class="detail__row detail__buttons">
          <div class="detail__button">
            <app-button>振り込み申請</app-button>
          </div>
          <div class="detail__button">
            <app-button>振り込み申請</app-button>
          </div>
        </div>
      </div>
      <div class="page__sold sold">
        <div class="sold__heading heading">
          <span class="heading__main"><app-heading>販売履歴</app-heading></span>
          <span class="heading__notes">　※取引が完了しているもの</span>
        </div>
        <div class="sold__items">
          <buy-item-boxes :items="soldItems"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import AppHeading from "@/components/atoms/headings/AppHeading";
import AppButton from "@/components/atoms/buttons/AppButton";
import BuyItemBoxes from "@/components/organisms/ItemBoxes/BuyItemBoxes";

export default {
  components: {BuyItemBoxes, AppButton, AppHeading},
  layout: 'mypage',
  async asyncData({params, $api, $myAuth}) {
    const soldItems = await $api['item-transaction'].getBySellerIdStateSold($myAuth.user().id).then(
        ({data}) => {
          console.log(data)
          return data.entries
        }
    )
    const saleDetail = await $api['item-transaction'].getSalesDetailBySellerId($myAuth.user().id).then(
        ({data}) => {
          console.log(data)
          return data.entries
        }
    )
    return {soldItems: soldItems, salesDetail: saleDetail}
  },

}
</script>

<style scoped lang="scss">
.page {
  &__heading {
    margin-bottom: $large-margin;
  }

}

.detail {
  width: 500px;
  margin-right: auto;
  margin-bottom: $large-margin;
  background-color: $main-background-color;
  border-radius: $box-border-radius;
  box-sizing: border-box;
  padding: $large-margin;

  &__heading {
    margin-bottom: $medium-parts-margin;
  }

  &__row {
    margin-bottom: $medium-parts-margin;
  }

  &__buttons {
    margin-top: $large-margin;
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
  }

  &__button {
    width: 150px;
    height: 40px;
  }
}

.sold {
  &__heading {
    margin-bottom: $large-margin;
    display: flex;
    justify-content: left;
    align-items: flex-end;
  }
}
</style>