<template>
  <div class="favorite">
    <div class="favorite__heading">
      <app-heading>お気に入り</app-heading>
    </div>
    <div class="favorite__tabs">
      <div class="favorite__tab favorite__tab--item">
        <app-tab-button
            @myClick="tabChange"
            :state="tabs.item.state"
        >商品
        </app-tab-button>
      </div>
      <div class="favorite__tab favorite__tab--koe">
        <app-tab-button
            @myClick="tabChange"
            :state="tabs.koe.state"
        >コエ
        </app-tab-button>
      </div>
    </div>
    <div class="favorite__content">
      <div v-if="tabs.item.state" class="favorite__items">
        <favorite-item-boxes/>
      </div>
      <div v-if="tabs.koe.state" class="favorite__koe-list">
        <favorite-koe-boxes/>
      </div>
    </div>
  </div>
</template>

<script>
import AppHeading from "~/components/atoms/headings/AppHeading";
import AppTabButton from "~/components/atoms/buttons/AppTabButton";
import FavoriteItemBoxes from "~/components/organisms/ItemBoxes/FavoriteItemBoxes";
import FavoriteKoeBoxes from "~/components/organisms/koeBoxes/FavoriteKoeBoxes";

export default {
  name: "favorite",
  components: {FavoriteKoeBoxes, FavoriteItemBoxes, AppTabButton, AppHeading},
  layout: 'mypage',
  data() {
    return {
      tabs: {
        item: {state: true},
        koe: {state: false}
      }
    }
  },
  methods: {
    tabChange() {
      this.tabs.item.state = !this.tabs.item.state
      this.tabs.koe.state = !this.tabs.koe.state
    }
  }

}
</script>

<style scoped lang="scss">
.favorite {

  &__heading {
    margin-bottom: $large-margin;
  }

  &__tabs {
    display: flex;
    justify-content: left;
    margin-bottom: $semi-large-margin;
  }

  &__tab {
    width: 200px;
    height: 40px;
    margin-right: $medium-parts-margin;
  }
}
</style>