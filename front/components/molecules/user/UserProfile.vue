<template>
  <div class="user-profile">
    <div class="user-profile__heading">
      <div class="user-profile__image">
        <user-icon
            :id="userId"
            :image="userImage"
        />
      </div>
      <p class="user-profile__name">{{ userName }}</p>
      <p class="user-profile__achievement">

      </p>
      <div class="user-profile__follow">
        <app-user-follow-button
            @myClick="followClick"
            :state="userFollow"
        />
      </div>
    </div>
    <p class="user-profile__description">{{ userDescription }}</p>
  </div>
</template>

<script>
import UserIcon from "~/components/icons/UserIcon";
import AppUserFollowButton from "~/components/atoms/buttons/AppUserFollowButton";

export default {
  name: "UserProfile",
  components: {AppUserFollowButton, UserIcon},
  props: {
    userImage: {
      type: String,
      default: ''
    },
    userName: {
      type: String,
      default: 'テストユーザー'
    },
    userId: {
      type: Number,
      default: 1
    },
    userFollow: {
      type: Boolean,
      default: false
    },
    userDescription: {
      type: String,
      default:
        'これはテストこれはテストこれはテストこれはテストa\nこれはテストこれはテストこれはテストこれはテスト'
    }
  },
  methods: {
    followClick() {
      this.userFollow = !this.userFollow
    }
  }
}
</script>

<style scoped lang="scss">
.user-profile {
  width: 600px;
  margin: 0 auto;
  padding: $large-margin;
  box-sizing: border-box;
  background-color: $main-background-color;


  &__heading {
    margin-bottom: $large-margin;
  }

  &__image {
    width: 100px;
    height: 100px;
    margin: 0 auto $large-margin auto;
  }

  &__name {
    text-align: center;
    margin-bottom: $large-margin;
  }

  &__follow {
    margin: 0 auto;
    width: 200px;
    height: 30px;
  }

  &__description {
    white-space: pre-wrap;
  }
}
</style>