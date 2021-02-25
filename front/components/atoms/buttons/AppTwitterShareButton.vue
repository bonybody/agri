<template>
  <div class="twitter-share-button">
    <ShareNetwork
        network="twitter"
        :url="url"
        :title="title"
        :description="description"
        :quote="quote"
    >
      <twitter-icon/>
    </ShareNetwork>
  </div>
</template>

<script>
import TwitterIcon from "~/components/icons/TwitterIcon";

export default {
  name: "AppTwitterShareButton",
  components: {TwitterIcon},
  props: {
    url: {
      type: String,
      default: ''
    },
    title: {
      type: String,
      default: ''
    },
    description: {
      type: String,
      default: ''
    },
    quote: {
      type: String,
      default: ''
    }
  }
}
</script>

<style scoped lang="scss">
.twitter-share-button {
  width: 100%;
  height: 100%;

  img {
    width: 100%;
    height: 100%;
  }
}
</style>