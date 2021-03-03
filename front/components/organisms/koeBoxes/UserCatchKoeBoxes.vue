<template>
  <div class="favorite-koe-boxes">
    <template v-for="koe in koeLists">
      <div class="favorite-koe-boxes__box">
        <koe-box
            :id="koe.id"
            :user-id="koe.user.id"
            :user-name="koe.user.name"
            :item-id="koe.item.id"
            :item-name="koe.item.name"
            :koe-title="koe.title"
            :koe-text="koe.text"
        />
      </div>
    </template>
  </div>
</template>

<script>
import KoeBox from "~/components/molecules/koe/KoeBox";

export default {
  name: "UserCatchKoeBoxes",
  components: {KoeBox},
  async fetch() {
    const res = await this.$api['koe'].getByCatchUser(this.$myAuth.user().id).then(({data}) => {
      this.koeLists = data.entries
      this.state = data.state
      console.log(data.entries)
      // console.log(data.entries[0].images[0])
    })
  },
  data() {
    return {
      koeLists: [],
    }
  }

}
</script>

<style scoped lang="scss">
.favorite-koe-boxes {
  display: flex;
  flex-wrap: wrap;
  justify-content: left;

  &__box {
    margin-right: 20px;
    margin-bottom: 20px;
  }

}
</style>