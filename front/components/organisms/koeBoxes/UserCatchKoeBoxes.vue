<template>
  <div class="favorite-koe-boxes">
    <template v-for="koe in koeLists">
      <div class="favorite-koe-boxes__box">
        <koe-box
            :id="koe.id"
            :user-id="koe.userId"
            :user-name="koe.userName"
            :item-id="koe.itemId"
            :item-name="koe.itemName"
            :koe-title="koe.title"
            :koe-text="koe.text"
        />
      </div>
    </template>
  </div>
</template>

<script>
import KoeBox from "~/components/molecules/koe/KoeBox";

export default {
  name: "UserCatchKoeBoxes",
  components: {KoeBox},
  data() {
    return {
      koeLists: [
        {
          id: 1,
          title: '届いてビックリ！',
          text: ' 衛生的にキレイに並べられた人参にビックリしました。 みずみずしく、そして甘い。 歯ごたえも良く、美味しくいただきました',
          userId: 2,
          userName: 'テストユーザー2',
          itemId: 1,
          itemName: '【家庭用】フルーツにんじん10kg～',
        },
        {
          id: 2,
          title: '量がとにかくすごいです。',
          text: '夫婦2人なので多すぎないか心配していましたが、 多いだけではなくって 新鮮だからなのか、日持ちも長くて助かりました。',
          userId: 3,
          userName: 'テストユーザー3',
          itemId: 1,
          itemName: '【家庭用】フルーツにんじん10kg～',
        },
        {
          id: 3,
          title: '綺麗な美味しい人参でした',
          text: 'この季節でしたの、少々不安に思っていましたが、期待以上の綺麗な美味しい人参でした。クールで届けて下さいましたので、おすそ分けして、残りは冷蔵庫に直行しました。',
          userId: 4,
          userName: 'テストユーザー4',
          itemId: 1,
          itemName: '【家庭用】フルーツにんじん10kg～',
        },
        {
          id: 4,
          title: 'キレイなニンジンがたくさん届きました。',
          text: '質もとても良くて、ヒビやヨゴレなどもなく、味もとても美味しい、良いニンジンでした。また頼みたいです！',
          userId: 5,
          userName: 'テストユーザー5',
          itemId: 1,
          itemName: '【家庭用】フルーツにんじん10kg～',
        },
      ],
    }
  }

}
</script>

<style scoped lang="scss">
.favorite-koe-boxes {
  display: flex;
  flex-wrap: wrap;
  justify-content: left;

  &__box {
    margin-right: 20px;
    margin-bottom: 20px;
  }

}
</style>