<template>
  <button class="favorite-button" :class="{'favorite': getState, 'no-favorite': !getState}" @click="click()">
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
      default: false
    }
  },
  data() {
    return {
      thisState: undefined
    }
  },
  methods: {
    click() {
      if (this.thisState === undefined) {
        this.thisState = this.state
      }
      this.thisState = !this.thisState


      this.$emit('myClick')
    }
  },
  computed: {
    getState() {
      if (this.thisState === undefined) {
        return this.state
      }
      return this.thisState
    }
  }
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