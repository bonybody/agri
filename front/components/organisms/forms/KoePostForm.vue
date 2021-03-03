<template>
  <div class="koe-post-form">
    <div class="koe-post-form__heading">
      <app-form-heading>コエ投稿</app-form-heading>
    </div>
    <div class="koe-post-form__section">
      <koe-title-form v-model="title"/>
    </div>
    <div class="koe-post-form__section">
      <koe-text-form v-model="text"/>
    </div>
    <div class="koe-post-form__button">
      <app-form-button v-if="type === 'post'" @my-click="post">コエ投稿</app-form-button>
      <app-form-button v-if="type === 'edit'" @my-click="edit">コエ編集</app-form-button>
    </div>
  </div>
</template>

<script>
import AppFormHeading from "~/components/atoms/headings/AppFormHeading";
import KoeTitleForm from "~/components/molecules/forms/KoeTitleForm";
import KoeTextForm from "~/components/molecules/forms/KoeTextForm";
import AppFormButton from "~/components/atoms/forms/button/AppFormButton";

export default {
  name: "KoePostForm",
  components: {AppFormButton, KoeTextForm, KoeTitleForm, AppFormHeading},
  props: {
    itemId: {
      type: Number,
      require: true
    },
    type: {
      type: String,
      default: 'post'
    },
  },
  data() {
    return {
      title: '',
      text: '',
    }
  },
  methods: {
    async post() {
      const res = await this.$api['koe'].post({
        title: this.title,
        text: this.text,
        item_id: this.itemId,
        user_id: this.$myAuth.user().id
      }).then(({data}) => {
        console.log(data)
      })
    },
    edit() {

    }
  }
}
</script>

<style scoped lang="scss">
.koe-post-form {
  @include form-box-style;

  &__section {
    @include form-section-mixin;
  }
}

</style>