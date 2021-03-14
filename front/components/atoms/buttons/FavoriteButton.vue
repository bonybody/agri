<template>
  <button type="button" class="favorite-button" :class="{'favorite': state, 'no-favorite': !state}" @click="$emit('myClick')">
    <heart-icon></heart-icon>
  </button>
</template>

<script>
import HeartIcon from "~/components/icons/HeartIcon";

export default {
  name: "FavoriteButton",
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
.favorite-button {
  height: 100%;

  svg {
    height: 100%;
    transition: all 0.2s;
  }
}

.favorite {
  svg {
    fill: $accent-color;
  }
}

.no-favorite {
  svg {
    fill: $shadow-color;
  }
}
</style>