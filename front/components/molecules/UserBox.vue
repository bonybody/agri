<template>
  <div :to="getLink" class="user-box">
    <div class="user-box__image">
      <user-icon :image="image"/>
    </div>
    <p class="user-box__name">{{ name }}</p>
    <div class="user-box__link">
      <app-form-button @my-click="userLink">プロフィール</app-form-button>
    </div>
  </div>
</template>

<script>
import UserIcon from "~/components/icons/UserIcon";

export default {
  name: "UserBox",
  components: {UserIcon},
  props: {
    id: {
      type: Number,
      default: 1
    },
    image: {
      type: String,
      default: ''
    },
    name: {
      type: String,
      default: 'テストユーザー'
    },
  },
  computed: {
    getLink() {
      return {
        path: '/user/' + this.id
      }
    }
  },
  methods: {
    userLink() {
      this.$router.push({ path: '/user/' + this.id})
    }
  }
}
</script>

<style scoped lang="scss">

.user-box {
  display: block;
  position: relative;
  width: 180px;
  height: 180px;
  background-color: $main-background-color;
  border-radius: $box-border-radius;
  box-sizing: border-box;
  padding: $medium-parts-margin;

  &__image {
    width: 60px;
    height: 60px;
    margin: 0 auto $medium-parts-margin auto;
  }

  &__name {
    text-align: center;
  }

  &__link {
    position: absolute;
    bottom: $medium-parts-margin;
    width: calc(100% - #{$medium-parts-margin} * 2);
  }
}

</style>