<template>
  <div class="new-items">
    <template v-for="item in items">
      <div class="new-items__item">
        <item-box
            :item-id="item.id"
            :image="require('~/assets/images/test_images/item/' + item.image + '.jpg')"
            :name="item.name"
            :address="item.address"
            :price="item.price"
            :remaining="item.remaining"
            :period="item.period"
        />
      </div>
    </template>
  </div>
</template>

<script>
import ItemBox from "~/components/molecules/ItemBox";

export default {
  name: "NewItemBoxies",
  components: {ItemBox},
  data() {
    return {
      items: [
        {
          id: 1,
          image: 1,
          name: '【家庭用】フルーツにんじん10kg～',
          address: '愛知県碧南市',
          price: 2160,
          remaining: '今週残り4つ',
          period: 3
        },
        {
          id: 2,
          image: 2,
          name: 'とまと 8〜12個 約1kg',
          address: '群馬県',
          price: 2000,
          remaining: '残り7つ',
          period: 5
        },
        {
          id: 3,
          image: 3,
          name: '(馬鈴薯)種ジャガイモ【男爵薯】【1kg】ホクホクで美味しいジャガイモの定番',
          address: '福岡県',
          price: 315,
          remaining: '今週残り23つ',
          period: 30
        },
        {
          id: 4,
          image: 4,
          name: '8月下旬から発送生でも食べられるとうもろこし ゴールドラッシュ 20本～',
          address: '北海道夕張郡',
          price: 6645,
          remaining: '今週残り4つ',
          period: 10
        },
        {
          id: 5,
          image: 5,
          name: '令和2年産 にんにく 青森 500g～',
          address: '青森県',
          price: 1556,
          remaining: '今週残り2つ',
          period: 39
        },
        {
          id: 6,
          image: 6,
          name: 'ファンシー野菜　芽キャベツ グリーン 100g～',
          address: '愛知県碧南市',
          price: 923,
          remaining: '今週残り5つ',
          period: 14
        },
        {
          id: 7,
          image: 7,
          name: '坊ちゃんかぼちゃ 10玉入り(1玉 300g)～ 北海道産',
          address: '北海道',
          price: 3160,
          remaining: '今月残り10つ',
          period: 25
        },
        {
          id: 8,
          image: 8,
          name: '春の先採りアスパラガス',
          address: '福岡県',
          price: 3980,
          remaining: '残り13つ',
          period: 30
        },
        {
          id: 9,
          image: 9,
          name: '長崎県産!無農薬栽培の生姜1kg【しょうが】【ショウガ】',
          address: '長崎県',
          price: 2204,
          remaining: '残り12つ',
          period: 38
        },
        {
          id: 10,
          image: 10,
          name: '国産 レタス 1箱　10kg～',
          address: '愛知県',
          price: 4800,
          remaining: '今週残り5つ',
          period: 20
        },
      ],
    }
  }
}
</script>

<style scoped lang="scss">
.new-items {
  display: flex;
  flex-wrap: wrap;
  justify-content: left;

  &__item {
    margin-right: 20px;
    margin-bottom: 20px;
  }
}
</style>