<template>
  <button type="button" class="favorite-detail-button" :class="{'favorite': state, 'no-favorite': !state}" @click="$emit('myClick')">
    <heart-icon></heart-icon>
    <span v-if="!state" class="favorite-detail-button__text">お気に入り登録</span>
    <span v-else class="favorite-detail-button__text">お気に入り解除</span>
  </button>
</template>

<script>
import HeartIcon from "~/components/icons/HeartIcon";

export default {
  name: "FavoriteDetailBotton",
  components: {HeartIcon},
  props: {
    state: {
      type: Boolean,
      default: true
    }
  },
}
</script>

<style scoped lang="scss">
.favorite-detail-button {
  display: block;
  background-color: $main-background-color;
  padding: 10px;
  font-size: 1rem;
  border-radius: 100px;

  &:hover {
    opacity: $hover-opacity;
  }

  svg {
    height: 1em;
    transition: all 0.2s;
    vertical-align: bottom;
  }
}

.favorite {
  border: 1px solid $accent-color;

  svg {
    fill: $accent-color;
  }
}

.no-favorite {
  border: 1px solid $shadow-color;

  svg {
    fill: $shadow-color;
  }

}

</style>