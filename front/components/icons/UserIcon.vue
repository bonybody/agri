<template>
  <nuxt-link :to="getToLink" class="user-profile-link">
    <div class="user-icon" :class="{'image': image, 'noImage': !image}">
      <img v-if="image" class="user-icon__icon user-icon__icon--image" :src="image" alt="ユーザー画像">
      <div class="user-icon__icon user-icon__icon--no-image">
        <no-user-image-icon v-if="!image"/>
      </div>
    </div>
  </nuxt-link>
</template>

<script>
export default {
  name: "UserIcon",
  props: {
    image: {
      type: String,
      default: ''
    },
    myProfile: {
      type: Boolean,
      default: false
    },
    id: {
      type: Number,
      default: 1
    }

  },
  computed: {
    getToLink: function () {
      if (this.myProfile === true) {
        return '/setting/profile'
      }
      return '/user/' + this.userId
    }
  }
}
</script>

<style scoped lang="scss">
.user-profile-link {
  display: block;
  height: 100%;
  width: 100%;
  border-radius: 100%;
  background-color: $shadow-color;
}

.user-icon {
  height: 100%;
  width: 100%;
  &__icon {
    height: 100%;
    width: 100%;
    &--image {

    }
    &--no-image {
      svg {
        fill: $main-background-color;
      }
    }
  }
}

.img svg {
}

.noImage {
  padding: 7px;
}

</style>