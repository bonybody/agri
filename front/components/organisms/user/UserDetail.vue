<template>
  <div class="user-detail">
    <div class="user-detail__profile">
      <user-profile

      />
    </div>
    <div class="user-detail__tabs">
      <div class="user-detail__tab">
        <app-tab-button
            :state="tabs.item.state"
            @myClick="tabChange"
        >{{ tabs.item.value }}</app-tab-button>
      </div>
      <div class="user-detail__tab">
        <app-tab-button
            :state="tabs.koe.state"
            @myClick="tabChange"
        >{{ tabs.koe.value }}</app-tab-button>
      </div>
    </div>
    <div v-if="tabs.item.state" class="user-detail__items">
      <user-item-boxes/>
    </div>
    <div v-if="tabs.koe.state" class="user-detail__koe">
      <user-catch-koe-boxes/>
    </div>
  </div>
</template>

<script>
import UserProfile from "~/components/molecules/user/UserProfile";
import AppTabButton from "~/components/atoms/buttons/AppTabButton";
import UserItemBoxes from "~/components/organisms/ItemBoxes/UserItemBoxes";
import UserCatchKoeBoxes from "~/components/organisms/koeBoxes/UserCatchKoeBoxes";

export default {
  name: "UserDetail",
  components: {UserCatchKoeBoxes, UserItemBoxes, AppTabButton, UserProfile},
  data() {
    return {
      tabs: {
        item: {
          state: true,
          value: 'この人の商品'
        },
        koe: {
          state: false,
          value: 'この人に集まったコエ'
        }
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
.user-detail {

  &__profile {
    margin-bottom: $large-margin;
  }
  &__tabs {
    display: flex;
    justify-content: center;
  }

  &__tab {
    margin: 0 $medium-parts-margin;
    width: 200px;
    height: 40px;
  }

  &__items {
    max-width: 1024px;
    box-sizing: content-box;
    padding: 0 12px;
    margin: $large-margin auto;
  }
  &__koe {
    max-width: 1024px;
    box-sizing: content-box;
    padding: 0 12px;
    margin: $large-margin auto;
  }
}
</style>