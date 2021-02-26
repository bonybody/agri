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
      <div class="user-profile__button user-profile__follow"
           v-if="!verifyUserId"
      >
        <app-user-follow-button
            @myClick="followClick"
            :state="userFollow"
        />
      </div>
      <div class="user-profile__button user-profile__edit"
           v-if="verifyUserId"
      >
        <app-link-button :link="'/setting/profile'">プロフィールを編集する</app-link-button>
      </div>
    </div>
    <p class="user-profile__description">{{ userDescription }}</p>
    <div class="sns-share">
      <div class="sns-share__icon">
        <app-twitter-share-button/>
      </div>
    </div>
  </div>
</template>

<script>
import UserIcon from "~/components/icons/UserIcon";
import AppUserFollowButton from "~/components/atoms/buttons/AppUserFollowButton";
import AppLinkButton from "~/components/atoms/buttons/AppLinkButton";
import AppTwitterShareButton from "~/components/atoms/buttons/AppTwitterShareButton";

export default {
  name: "UserProfile",
  components: {AppTwitterShareButton, AppLinkButton, AppUserFollowButton, UserIcon},
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
  },
  computed: {
    verifyUserId() {
      if (this.$myAuth.loggedIn()) {
        if (this.$myAuth.user().id === this.userId) {
          return true
        }
        return false
      }
      return false
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

  &__button {
    margin: 0 auto;
    width: 200px;
    height: 30px;

  }

  &__follow {
  }

  &__description {
    white-space: pre-wrap;
  }
}
.sns-share {
  display: flex;
  justify-content: flex-end;
  &__icon {
    width: 30px;
    height: 30px;
  }
}
</style>