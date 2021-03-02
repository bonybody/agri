<template>
  <div class="item">
    <div class="item__catch-koe">
      <div class="koe">
        <div class="item__heading">
          <app-heading>コエ一覧</app-heading>
        </div>
        <div class="koe__change">
          <app-form-button @my-click="koepost">投稿したコエ</app-form-button>
          <div class="koe__main">
            <app-form-button @my-click="koereach">届いたコエ</app-form-button>
          </div>
        </div>
        <div class="koe-lists">
          <reach-koe-boxes/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ReachKoeBoxes from "~/components/organisms/koeBoxes/ReachKoeBoxes";
import AppHeading from "~/components/atoms/headings/AppHeading";

export default {
  name: "koe",
  components: {AppHeading, ReachKoeBoxes},
  auth: false
}
</script>

<style scoped lang="scss">
.item {
  max-width: 1024px;
  margin: 0 auto;

  &__detail {
    margin-bottom: $large-margin;
  }

  &__heading {
    margin-bottom: $semi-large-margin;
    text-align: center;
  }

  &__catch-koe {
  }
}
.koe {
  &__change {
    width: 150px;
    margin-top: $large-margin;
    margin-bottom: $large-margin;
  }

  &__main {
  }
}

</style>