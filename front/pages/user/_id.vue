<template>
  <div class="user">
    <div class="user__profile">
      <user-profile
          :user-id="user.id"
          :user-name="user.display_name"
      />
    </div>
    <div class="user__tabs">
      <div class="user__tab">
        <app-tab-button
            :state="tabs.item.state"
            @myClick="tabChange"
        >{{ tabs.item.text }}</app-tab-button>
      </div>
      <div class="user__tab">
        <app-tab-button
            :state="tabs.koe.state"
            @myClick="tabChange"
        >{{ tabs.koe.text }}</app-tab-button>
      </div>
    </div>
    <div v-if="tabs.item.state" class="user__items">
      <user-item-boxes :id="Number($route.params.id)"/>
    </div>
    <div v-if="tabs.koe.state" class="user__koe">
      <user-catch-koe-boxes/>
    </div>

  </div>
</template>

<script>
import UserDetail from "~/components/organisms/user/UserDetail";
import UserProfile from "~/components/molecules/user/UserProfile";

export default {
  components: {UserProfile, UserDetail},
  auth: false,
  async asyncData({$api, $myAuth, params}) {
    let res
    await $api['user'].getById(params.id)
        .then(({data}) => {
          res = data
        })
        .catch(error => {
          res = false
        })
    if (res) {
      return {
        user: res
      }
    }
  },
  data() {
    return {
      user: {},
      tabs: {
        item: {
          state: true,
          text: 'このひとの商品'
        },
        koe: {
          state: false,
          text: 'この人に集まったコエ'
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
.user {
  max-width: 1024px;
  box-sizing: border-box;
  padding: 0 $min-parts-margin;
  margin: 0 auto;

  &__profile {
    margin-bottom: $medium-parts-margin;
  }
  &__tabs {
    display: flex;
    justify-content: center;
    margin-bottom: $medium-parts-margin;
  }

  &__tab {
    margin: 0 $medium-parts-margin;
    width: 200px;
    height: 40px;
  }

}
</style>